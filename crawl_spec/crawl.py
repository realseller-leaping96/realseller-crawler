import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re
import os

#######################내가 정의한 모듈##############################################

from module.namuwiki.main_0 import parse_namu
from module.namuwiki.detail_df_init import df_init #출력할 데이터 프레임 형식 정의 =>  DataFrame 리턴
from module.cetizen import parse_cetizen
from module.danawa import parse_danawa
#######################입력 파일 로드################################

df_input = pd.read_csv('input_data_~0408.csv')
df_input=df_input.fillna('')
#print(df_input.iloc[102])

#######################출력 형식 로드################################
df_output = df_init()
#######################크롤링 파트 (나무위키)################################
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless")
driver  = webdriver.Chrome(options = chrome_options)
# driver  = webdriver.Chrome()
driver.implicitly_wait(3)

df_output = parse_namu(df_input, driver, df_output,0,len(df_input))

#######################크롤링 파트 (세티즌)################################
# df_output = parse_cetizen(df_input, driver, df_output,0,1)

#######################크롤링 파트 (다나와)################################
# df_output = parse_danawa(df_input, driver, df_output, 0,1)

#######################크롤링 데이터 저장################################
df_output.to_csv("test0414_s.csv", encoding = "utf-8-sig")

os.system("pause")