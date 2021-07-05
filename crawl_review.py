import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re
import os
from module.namuwiki.detail_df_init import df_init #출력할 데이터 프레임 형식 정의 =>  DataFrame 리턴
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
from selenium.webdriver.chrome.options import Options
import MySQLdb
import time
from module.st11_entique import parse_11_entique # 11번가 중고폰 리뷰크롤러
from module.st11_signup import parse_11_signup # 11번가 완납가입 리뷰크롤러
from module.naver_shopping import parse_naver_shopping #네이버쇼핑 리뷰크롤러
import pandas as pd
import numpy as np

engine = create_engine("mysql+mysqldb://root:"+"123123"+"@localhost/gidseller", encoding='utf-8')
conn = engine.connect()
df_input = pd.read_sql_table('g5_phone_list',conn)


my_dict = {
    "pl_id": "",                      #스펙테이블 아이디
    "pl_model_code": "",              #모델코드
    "pl_name": "",                    #모델영문명

    "star": "",                       #별점
    "market": "",                     #구입처(ex 인터파크, 11번가)
    "write_id": "",                   #작성자(일부가림처리)
    "upload_date": "",                 #업로드날짜
    "title":"",                       #리뷰제목 
    "content": "",                        #리뷰내용 
}

crawl_data = pd.DataFrame(my_dict,index=[0])
crawl_data_none = pd.DataFrame(my_dict,index=[0])


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless")
# driver  = webdriver.Chrome(options = chrome_options)
driver  = webdriver.Chrome()
driver.implicitly_wait(3)

num = len(df_input)
# num = 10
#11번가- 중고
for i in range(0,num):
    crawl_data = crawl_data.append(parse_11_entique(driver,df_input,crawl_data_none,i,""))
    print(i)

#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중
crawl_data.to_csv("test_r.csv", encoding = "utf-8-sig")
#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중

#11번가- 완납가입
for i in range(0,num):
    crawl_data = crawl_data.append(parse_11_signup(driver,df_input,crawl_data_none,i,""))
    print(i)

#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중
crawl_data.to_csv("test_r.csv", encoding = "utf-8-sig")
#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중

#네이버쇼핑
for i in range(0,num):
    if i % 3 == 0 and i != 0:        
        driver.quit()
        driver  = webdriver.Chrome()
    #crawl_data.to_csv("test_r.csv", encoding = "utf-8-sig") => 네이버쇼핑은 크롤링감지시 막으므로 중간에 백업
    print(i)
    crawl_data = crawl_data.append(parse_naver_shopping(driver,df_input,crawl_data_none,i,"all"))
    
#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중
crawl_data.to_csv("test_r.csv", encoding = "utf-8-sig")
#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중

###############################
#         백업코드            #
#    g5_phone_review 테이블   #
###############################

#a = pd.read_csv("test_r.csv")
crawl_data.dropna(subset=['URL'], inplace=True)

connection = pymysql.connect(host='localhost', user='root', password='123123', db='gidseller')
try:
    with connection.cursor() as cursor:
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

    connection.commit()
    
    #내DB에 백업
    engine = create_engine("mysql+mysqldb://root:"+"123123"+"@localhost/gidseller", encoding='utf-8')
    conn = engine.connect()
    crawl_data = crawl_data.drop(['pl_id'], axis='columns')

    crawl_data['pr_valid'] = ''
    #테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중
    crawl_data.to_csv("test_r.csv", encoding = "utf-8-sig")
    #테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중#테스트중
    crawl_data = crawl_data.drop(['upload_day'],axis=1)
    crawl_data = crawl_data.drop(['text'],axis=1)
    crawl_data.columns = ['pr_model_code', 'pr_model_name','pr_star','pr_market','pr_write_id','pr_upload_date','pr_title','pr_text','pr_url','pr_valid']
    
    

    regex = """용량|색|사이즈|인치|화면|무게|센치|배터리|카메라|메모리|성능|출시|속도
            |[0-9]+기가|보급형|방수|무선충전|지문인식|스크린|디스플레이|스펙|내장
            |외장|컬러|버튼|단자|현상|듀얼|화소|내구성|발열|업데이트|C타입"""

    #유효한 내용이 들었는지 판단하여 valid열 작성
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

    ##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중
    crawl_data.to_sql(name='g5_phone_review', con=engine, if_exists='append', index=False)
    crawl_data.to_csv("test_r.csv", encoding = "utf-8-sig")
    ##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중##테스트중

    #중복삭제
    with connection.cursor() as cursor:
        sql1 = """
        DELETE r2 FROM g5_phone_review r1, g5_phone_review r2 WHERE r1.pr_id <> r2.pr_id AND r1.pr_text = r2.pr_text
        """
        cursor.execute(sql1)
    connection.commit()

    #pk 새로부여
    with connection.cursor() as cursor:
        
        sql2_1= """
        ALTER TABLE g5_phone_review AUTO_INCREMENT = 1;
        """
        cursor.execute(sql2_1)
    connection.commit()

    with connection.cursor() as cursor:
        sql2_2="""
        SET @COUNT = 0;
        """
        cursor.execute(sql2_2)
    connection.commit()

    with connection.cursor() as cursor:
        sql2_3="""
        UPDATE g5_phone_review SET pr_id = @COUNT:=@COUNT+1;
        """
        cursor.execute(sql2_3)
    connection.commit()


finally:
    connection.close()