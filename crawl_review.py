import pandas as pd
import re
from module.review.st11_entique import parse_11_entique # 11번가 중고폰 리뷰크롤러
from module.review.st11_signup import parse_11_signup # 11번가 완납가입 리뷰크롤러
from module.review.naver_shopping import parse_naver_shopping #네이버쇼핑 리뷰크롤러
import pandas as pd
from datetime import datetime
import db_module #db연결 정의모듈 (id,pw 로컬환경따라 다름)
import chrome_driver_module #크롬드라이버 연결 정의모듈 (버전,경로 로컬환경따라 다름)

db_class = db_module.Database() #db연결 생성
driver = chrome_driver_module.ChromeDriver().driver

   ##########################################################
  #                리뷰 크롤링 코드                         # 
 #   입력:phone_list 테이블 / 출력:g5_phone_review 테이블  #
#########################################################

df_input = pd.read_sql_table('g5_phone_list',db_class.engine_conn) #g5_phone_list테이블에서 전체기종 데이터 로드

my_dict = { 
    #크롤링 결과데이터형식 정의
    "pl_id": "",                      #스펙테이블 아이디
    "pl_model_code": "",              #모델코드
    "pl_name": "",                    #모델영문명

    "star": "",                       #별점
    "market": "",                     #구입처(ex 인터파크, 11번가)
    "write_id": "",                   #작성자(일부가림처리)
    "upload_date": "",                #업로드날짜
    "title":"",                       #리뷰제목 
    "content": "",                    #리뷰내용 
}

crawl_data = pd.DataFrame(my_dict,index=[0])
crawl_data_none = pd.DataFrame(my_dict,index=[0])

# num = len(df_input) #테이블 총 행수만큼 크롤링 반복 => [EX] 270개면, 1~270까지 반복
num = 1 #테스트용

for i in range(0,num): #11번가- 중고폰 카테고리에서 리뷰크롤링
    crawl_data = crawl_data.append(parse_11_entique(driver,df_input,crawl_data_none,i,""))
    print(i)

for i in range(0,num): #11번가- 완납가입 카테고리에서 리뷰크롤링
    crawl_data = crawl_data.append(parse_11_signup(driver,df_input,crawl_data_none,i,""))
    print(i)

for i in range(0,num): #네이버쇼핑 리뷰 크롤링
    if i % 3 == 0 and i != 0:
        #네이버 쇼핑의 경우 비정상적인 로그감지를 피해서 3개 크롤링마다 크롬창 껏다키기        
        driver.quit()
        driver = chrome_driver_module.ChromeDriver().driver
    print(i)
    crawl_data = crawl_data.append(parse_naver_shopping(driver,df_input,crawl_data_none,i,"all"))
    

###############################
#       리뷰백업코드           #
#    g5_phone_review 테이블   #
###############################


#결과값 유실방지위해 csv파일로 백업 남기기
today = datetime.today()
crawl_data.to_csv(str(today.year) +"-"+ str(today.month) +"-"+ str(today.day)+"_review.csv", encoding = "utf-8-sig")



#g5_phone_review 테이블이 없을경우 생성해주기
cursor = db_class.cursor
sql =( """
CREATE TABLE if not exists `g5_phone_review` (
`pr_id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
`pr_model_code` VARCHAR(255) NULL DEFAULT NULL COMMENT '모델코드' COLLATE 'utf8_general_ci',
`pr_model_name` VARCHAR(255) NULL DEFAULT NULL COMMENT '모델이름' COLLATE 'utf8_general_ci',
`pr_star` FLOAT NULL DEFAULT NULL COMMENT '별점',
`pr_market` VARCHAR(50) NULL DEFAULT NULL COMMENT '게시 사이트' COLLATE 'utf8_general_ci',
`pr_write_id` VARCHAR(50) NULL DEFAULT NULL COMMENT '게시자 아이디' COLLATE 'utf8_general_ci',
`pr_upload_date` DATE NULL DEFAULT NULL COMMENT '게시 날짜',
`pr_title` VARCHAR(255) NULL DEFAULT NULL COMMENT '제목' COLLATE 'utf8_general_ci',
`pt_text` TEXT NULL DEFAULT NULL COMMENT '내용' COLLATE 'utf8_general_ci',
`pr_url` VARCHAR(255) NULL DEFAULT NULL COMMENT '리뷰 링크' COLLATE 'utf8_general_ci',
`pr_valid` VARCHAR(1) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
PRIMARY KEY (`pr_id`) USING BTREE
)
COMMENT='핸드폰 스펙정보'
COLLATE='utf8_general_ci'
ENGINE=MyISAM
AUTO_INCREMENT=5918
;
"""
)
cursor.execute(sql)
db_class.db_conn.commit()

#결과값에서 불필요한 컬럼제거
crawl_data.dropna(subset=['URL'], inplace=True) 
crawl_data = crawl_data.drop(['pl_id'], axis='columns')

#결과값 테이블 형식 지정
crawl_data['pr_valid'] = ''
crawl_data.columns = ['pr_model_code', 'pr_model_name','pr_star','pr_market','pr_write_id','pr_upload_date','pr_title','pr_text','pr_url','pr_valid']

#성능에 관련된 유효한 내용이 들었는지 판단하여 valid컬럼 작성
regex = """용량|색|사이즈|인치|화면|무게|센치|배터리|카메라|메모리|성능|출시|속도
        |[0-9]+기가|보급형|방수|무선충전|지문인식|스크린|디스플레이|스펙|내장
        |외장|컬러|버튼|단자|현상|듀얼|화소|내구성|발열|업데이트|C타입"""
valid_column = []
for i, row in crawl_data.iterrows():
    cont = str(row['pr_text'])
    if re.search(regex,cont) is not None: 
        crawl_data.loc[i,"pr_valid"] = "Y"
    else:
        crawl_data.loc[i,"pr_valid"] = "N"
    valid_column.append(crawl_data.iloc[i]['pr_valid'])
crawl_data["pr_valid"] = valid_column

#공백제거
text_column = []
for i, row in crawl_data.iterrows():
    cont = str(row['pr_text'])
    cont = cont.strip()
    cont = re.sub('([\\n\r\n]+[ ]+)',"",cont)
    text_column.append(cont)
crawl_data["pr_text"] = text_column

#테이블에 결과데이터 밀어넣기
crawl_data.to_sql(name='g5_phone_review', con=db_class.engine, if_exists='append', index=False)

#테이블내에서 중복된 리뷰 삭제후 pk값 새로 부여하기
df_input = pd.read_sql_table('g5_phone_review',db_class.engine_conn)
db_class.engine_conn.close()
duplicateDFRow = df_input[df_input.duplicated('pr_text',keep='last')]
if len(duplicateDFRow) > 0:
    del_list = duplicateDFRow['pr_id']
    for d in del_list:
        sql = "delete from g5_phone_review where pr_id=%s"
        cursor.execute(sql, d)
        db_class.db_conn.commit()

    sql2_1= """
    ALTER TABLE g5_phone_review AUTO_INCREMENT = 1;
    """
    cursor.execute(sql2_1)
    db_class.db_conn.commit()

    sql2_2="""
    SET @COUNT = 0;
    """
    cursor.execute(sql2_2)
    db_class.db_conn.commit()

    sql2_3="""
    UPDATE g5_phone_review SET pr_id = @COUNT:=@COUNT+1;
    """
    cursor.execute(sql2_3)
    db_class.db_conn.commit()
db_class.db_conn.close()

