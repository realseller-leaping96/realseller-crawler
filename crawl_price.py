import pandas as pd
from module.price.cetizen_cal import parse_by_telecom_maker #세티즌 가격크롤러
import pandas as pd
import module.db_module as db_module #db연결 정의모듈 (id,pw 로컬환경따라 다름)
import module.chrome_driver_module as chrome_driver_module #크롬드라이버 연결 정의모듈 (버전,경로 로컬환경따라 다름)

db_class = db_module.Database() #db연결 생성
driver = chrome_driver_module.ChromeDriver().driver #크롬드라이버 로드

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
for i in range(len(crawl_data)):
    price = ""
    #skt
    if df_input.iloc[i]['통신사'] == "SKT": 
        price = "SKT:"+df_input.iloc[i]['가격']

    #kt
    if df_input.iloc[i]['통신사'] == "KT" and price == "": 
        price = "KT:"+df_input.iloc[i]['가격'] 
    elif df_input.iloc[i]['통신사'] == "KT" and price != "":
        price = price +"|KT:"+df_input.iloc[i]['가격'] 

    #lg
    if df_input.iloc[i]['통신사'] == "LG" and price == "": 
        price = "LG:"+df_input.iloc[i]['가격'] 
    elif df_input.iloc[i]['통신사'] == "LG" and price != "":
        price = price +"|LG:"+df_input.iloc[i]['가격']   
    print(i)
    my_dict = {
        "model_name": df_input.iloc[i]['모델명'],                     #모델이름
        "model_code": df_input.iloc[i]['모델코드'].replace("/",""),   #모델코드
        "price": price.replace(",","").replace("원",""),             #가격
    }
    to_db = to_db.append(pd.DataFrame(my_dict, index=[0]))

#price_list 테이블 없을경우 정의해주기
try:    
    with db_class.cursor as cursor:
        sql =( "CREATE TABLE if not exists `price_list` (`price_id` INT(11) NOT NULL AUTO_INCREMENT,"+
              "`model_name` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',"+
              "`model_code` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',"+
              "`price` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',"+
              "PRIMARY KEY (`price_id`) USING BTREE"+
              ")COLLATE='utf8mb4_general_ci'"+
              "ENGINE=InnoDB;" 
             )
        cursor.execute(sql)
    db_class.db_conn.commit()
finally:
    db_class.db_conn.close()
    
#price_list 테이블에 데이터 백업
to_db.to_sql(name='price_list', con=db_class.engine, if_exists='append', index=False)