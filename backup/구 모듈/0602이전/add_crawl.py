import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re
import os

#######################내가 정의한 모듈##############################################
from module.namuwiki.detail_df_init import df_init #출력할 데이터 프레임 형식 정의 =>  DataFrame 리턴

from module.cetizen import main as cetizen
from module.namuwiki import main as namu
from module.danawa import main as danawa
#######################입력 파일 로드################################

df_input = pd.read_csv('../input_add.csv')
df_input=df_input.fillna('')
#print(df_input.iloc[102])

#######################출력 형식 로드################################
df_output = df_init()

######################셀레니움 로드################################
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless")
# driver  = webdriver.Chrome(options = chrome_options)
driver  = webdriver.Chrome()
driver.implicitly_wait(3)

num = len(df_input)
num = 10
#######################크롤링 파트 (나무위키)################################
df_output = namu.add(df_input, driver, df_output,0,num)

#######################크롤링 파트 (세티즌)################################
df_output = cetizen.add(df_input, driver, df_output,0,num)

#######################크롤링 파트 (다나와)################################
df_output = danawa.add(df_input, driver, df_output,0,num)

#######################크롤링 데이터 저장################################

df_output = df_output.drop(["카메라 특징"], axis=1)

if "생체인식" in df_output.columns:
    df_output = df_output.drop(["생체인식"], axis=1)

df_output.to_csv("output_add.csv", encoding = "utf-8-sig")

os.system("pause")