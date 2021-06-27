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
from module.add_valid import fillter, fix # 리뷰크롤러 병합기
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

# num = len(df_input)
num = 1
#11번가- 중고
for i in range(0,num):
    crawl_data = crawl_data.append(parse_11_entique(driver,df_input,crawl_data_none,i,""))
    print(i)

#11번가- 완납가입
for i in range(0,num):
    crawl_data = crawl_data.append(parse_11_signup(driver,df_input,crawl_data_none,i,""))
    print(i)

#네이버쇼핑
for i in range(0,num):
    if i % 30 == 0 and i != 0:        
        time.sleep(60)
    #crawl_data.to_csv("test_r.csv", encoding = "utf-8-sig") => 네이버쇼핑은 크롤링감지시 막으므로 중간에 백업
    print(i)
    crawl_data = crawl_data.append(parse_naver_shopping(driver,df_input,crawl_data_none,i,"all"))

#crawl_data.to_csv("test_r.csv", encoding = "utf-8-sig")

###############################
#         백업코드            #
#    g5_phone_review 테이블   #
###############################

#a = pd.read_csv("test_r.csv")
crawl_data.dropna(subset=['URL'], inplace=True)

connection = pymysql.connect(host='localhost', user='root', password='123123', db='gidseller')
try:
    with connection.cursor() as cursor:
        sql =( "CREATE TABLE if not exists`review_list` ("+
              "`review_id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,"+
              "`pl_id` INT(10) UNSIGNED NOT NULL,"+
              "`pl_model_code` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',"+
              "`pl_name` VARCHAR(255) NULL DEFAULT NULL COMMENT '기' COLLATE 'utf8_general_ci',"+
              "`star` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',"+
              "`market` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',"+
              "`write_id` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',"+
              "`upload_date` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',"+
              "`title` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8_general_ci',"+
              "`content` TEXT NULL DEFAULT NULL COMMENT '리뷰1' COLLATE 'utf8_general_ci',"+
              "`URL` TEXT NULL DEFAULT NULL COMMENT '리뷰1' COLLATE 'utf8_general_ci',"+
              "`valid` VARCHAR(1) NULL DEFAULT NULL COLLATE 'utf8_general_ci',"+
              "PRIMARY KEY (`review_id`) USING BTREE"+
              ")COLLATE='utf8mb4_general_ci'"+
              "ENGINE=InnoDB;" 
             )
        cursor.execute(sql)

    connection.commit()

finally:
    connection.close()

#내DB에 백업
engine = create_engine("mysql+mysqldb://root:"+"123123"+"@localhost/gidseller", encoding='utf-8')
conn = engine.connect()
#crawl_data = crawl_data.drop(['Unnamed: 0'], axis='columns')
crawl_data.to_sql(name='review_list', con=engine, if_exists='append', index=False)

