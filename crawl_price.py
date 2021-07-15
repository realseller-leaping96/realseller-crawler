import pandas as pd
from module.price.cetizen_cal import parse_by_telecom_maker #세티즌 가격크롤러
import module.db_module as db_module #db연결 정의모듈 (id,pw 로컬환경따라 다름)
import module.chrome_driver_module as chrome_driver_module #크롬드라이버 연결 정의모듈 (버전,경로 로컬환경따라 다름)
from module.price.rearrange_price_id import rearrange_price_id
import re

db_class = db_module.Database() #db연결 생성
driver = chrome_driver_module.ChromeDriver().driver #크롬드라이버 로드

#price_list 테이블 없을경우 정의해주기
try:    
    with db_class.db_conn.cursor() as cursor:
        sql =( """
            CREATE TABLE if not exists `price_list` (
            `price_id` INT(11) NOT NULL AUTO_INCREMENT,
            `model_name` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
            `model_code` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
            `price` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
            `storage` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
            PRIMARY KEY (`price_id`) USING BTREE
            )
        """ )
        cursor.execute(sql)
        db_class.db_conn.commit()
        
finally:
    pass

   #############################################
  #        세티즌 가격계산기 크롤링             #
 #  입력: 없음 / 출력: price_list테이블        #
#############################################

# 결과데이터 형식 정의
my_dict = {
    "통신사" : "",
    "모델명": "",
    "모델코드": "",
    "가격": ""
}
crawl_data = pd.DataFrame(my_dict,index=[0])

#세티즌 가격계산기사이트 접속하여 제조사&통신사별 크롤링
telecoms = ["SKT","KT","LG"]
makers = ["삼성전자", "애플", "LG전자"]
for telecom in telecoms:
    for maker in makers:
        crawl_data = parse_by_telecom_maker(telecom,maker,crawl_data,driver,my_dict)


# 백업데이터 형식 정의
df_input = crawl_data
my_dict = {
    "model_name": "",              #모델이름
    "model_code": "",              #모델코드
    "price": "",                       #가격
}
to_db = pd.DataFrame(my_dict,index=[0])

# 통신사별로 구분하여 데이터 정리

is_skt = crawl_data['통신사'] == 'SKT'
skt = crawl_data[is_skt]
is_kt = crawl_data['통신사'] == 'KT'
kt = crawl_data[is_kt]
is_lg = crawl_data['통신사'] == 'LG'
lg = crawl_data[is_lg]

join_keys = ['모델명'] #모델명으로 데이터 조인
df_OUTER_JOIN = pd.merge(skt, kt, left_on=join_keys, right_on=join_keys, how='outer')
df_OUTER_JOIN = pd.merge(df_OUTER_JOIN,lg, left_on=join_keys, right_on=join_keys, how='outer')
df_OUTER_JOIN = df_OUTER_JOIN.drop(df_OUTER_JOIN.columns[0], axis=1)
df_OUTER_JOIN.dropna(subset=['모델명'], inplace=True)
df_OUTER_JOIN['max_price'] = 0


price_column_1 = []
price_column_2 = []
price_column_3 = []
model_code_column = []
storage_column = []
model_name_column = []
for i, row in df_OUTER_JOIN.iterrows():
    #가격열 정수화하는 부분
    if not pd.isnull(row['가격']):
        cont = str(row['가격'])
        cont = cont.strip()
        cont = re.sub('[원, ]+',"",cont)
        price_column_1.append(int(cont))
    else:
        price_column_1.append(0)
    if not pd.isnull(row['가격_x']):
        cont = str(row['가격_x'])
        cont = cont.strip()
        cont = re.sub('[원, ]+',"",cont)
        price_column_2.append(int(cont))
    else:
        price_column_2.append(0)
    if not pd.isnull(row['가격_y']):
        cont = str(row['가격_y'])
        cont = cont.strip()
        cont = re.sub('[원, ]+',"",cont)
        price_column_3.append(int(cont))
    else:
        price_column_3.append(0)
    #모델코드열 문자열파싱
    if not pd.isnull(row['모델코드']):
        cont = str(row['모델코드'])
        cont = cont.replace("/","").replace(" ","")
        model_code_column.append(cont)
    else:
        model_code_column.append(None)
    #모델명에서 용량추출
    if not pd.isnull(row['모델명']):
        cont = str(row['모델명'])
        if cont.find("GB")!=-1 or cont.find("MB")!=-1:
            storage = re.search('\([0-9]+(G|M)(B)?\)',cont).group()
            cont = cont.replace(storage,"")
            storage = storage.replace("(","").replace(")","")
            storage_column.append(storage)
            cont = re.sub('[0-9]+(G|M)(B)?',"",cont)
            model_name_column.append(cont)
        else:
            storage = None
            storage_column.append(storage)
            model_name_column.append(cont)
    else:
        model_name_column.append(None)
        
df_OUTER_JOIN["가격"] = price_column_1
df_OUTER_JOIN["가격_x"] = price_column_2
df_OUTER_JOIN["가격_y"] = price_column_3
df_OUTER_JOIN["모델코드"] = model_code_column
df_OUTER_JOIN["모델명"] = model_name_column
df_OUTER_JOIN["용량"] = storage_column



max_price_column = []
for i, row in df_OUTER_JOIN.iterrows():
    price_1 = row['가격']
    price_2 = row['가격_x']
    price_3 = row['가격_y']
    max_price = max(price_1,price_2,price_3)
    max_price_column.append(max_price)

df_OUTER_JOIN["max_price"] = max_price_column

df_OUTER_JOIN = df_OUTER_JOIN.drop(['모델코드_x'],axis=1)
df_OUTER_JOIN = df_OUTER_JOIN.drop(['가격_x'],axis=1)
df_OUTER_JOIN = df_OUTER_JOIN.drop(['통신사_y'],axis=1)
df_OUTER_JOIN = df_OUTER_JOIN.drop(['모델코드_y'],axis=1)
df_OUTER_JOIN = df_OUTER_JOIN.drop(['가격_y'],axis=1)
df_OUTER_JOIN = df_OUTER_JOIN.drop(['통신사'],axis=1)
df_OUTER_JOIN = df_OUTER_JOIN.drop(['가격'],axis=1)


#기획상품인 기종 모델명으로 판단하여 삭제
del_inedx_list = []
for index, row in df_OUTER_JOIN.iterrows():
    #가격열 정수화하는 부분
    if not pd.isnull(row['모델명']):
        cont = str(row['모델명'])
        keywords = ["에디션","리패키지","리퍼","리패키징","애플워치",
        "리메뉴팩처","아이패드","워치스포츠","데모","지패드","갤럭시 워치",
        "edition","자급제","해외","editon","리메뉴팩쳐"]
        is_need_delete = 0
        for keyword in keywords:
            if cont.find(keyword)!=-1:
                is_need_delete = 1
        if is_need_delete == 1:
            del_inedx_list.append(index)
    else:
        pass
    
df_OUTER_JOIN = df_OUTER_JOIN.drop(del_inedx_list)
df_OUTER_JOIN.drop_duplicates(inplace=True)
# df_OUTER_JOIN = df_OUTER_JOIN.sort_values(by=['모델명'])

df_OUTER_JOIN.columns = ['model_name','model_code','price','storage']

price_list = pd.read_sql_table('price_list',db_class.engine_conn) #기존 price_list 테이블 로드
price_list = price_list.append(df_OUTER_JOIN, ignore_index=True)
price_list = price_list.drop(['price_id'],axis=1)
price_list = price_list.drop_duplicates(['model_name','model_code'], keep='last').sort_values(by=['model_name'])
price_list.to_csv("test_price.csv",encoding='utf-8-sig') 


#price_list 테이블 없을경우 정의해주기
try:    
    with db_class.cursor as cursor:
        cursor.execute("DELETE FROM price_list;")
        db_class.db_conn.commit()
        
finally:
     db_class.db_conn.close()
        

#price_list 테이블에 데이터 백업
price_list.to_sql(name='price_list', con=db_class.engine, if_exists='append', index=False)
db_class.engine_conn.close()

rearrange_price_id()