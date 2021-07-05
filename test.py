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
df_input = pd.read_sql_table('g5_phone_review',conn)

text_column = []
for i, row in df_input.iterrows():
    cont = str(row['pr_text'])
    cont = cont.strip()
    cont = re.sub('([\\n\r\n]+[ ]+)',"",cont)
    text_column.append(cont)
df_input["pr_text"] = text_column
df_input.to_sql(name='review_list_new', con=engine, if_exists='append', index=False)