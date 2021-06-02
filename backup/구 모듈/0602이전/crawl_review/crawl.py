import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re
import os
import time
###############################################################3
from module.st11_entique import parse_11_entique
from module.st11_signup import parse_11_signup
from module.naver_shopping import parse_naver_shopping
from module.add_valid import fillter, fix

df_input = pd.read_csv('input_data_~0408.csv')

my_dict = {
    "pl_id": "",                      #스펙테이블 아이디
    "pl_model_code": "",              #모델코드
    "pl_name": "",                    #모델영문명
    
    "star": "",                       #별점
    "market": "",                     #구입처(ex 인터파크, 11번가)
    "write_id": "",                   #작성자(일부가림처리)
    "upload_day": "",                 #업로드날짜
    "title":"",                       #리뷰제목 
    "text": "",                        #리뷰내용 
    "Target":""                       #리뷰대상이 되는 상품!!(실제랑 다를 수 있으므로)
}

crawl_data = pd.DataFrame(my_dict,index=[0])
crawl_data_none = pd.DataFrame(my_dict,index=[0])


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless")
# driver  = webdriver.Chrome(options = chrome_options)
driver  = webdriver.Chrome()
driver.implicitly_wait(3)

#11번가- 중고
# for i in range(180,len(df_input)):
for i in range(3):
    crawl_data = crawl_data.append(parse_11_entique(driver,df_input,crawl_data_none,i,""))
    print(i)

crawl_data.to_csv("test0413_r.csv", encoding = "utf-8-sig")

#11번가- 완납가입
# for i in range(180,len(df_input)):
for i in range(3):
    crawl_data = crawl_data.append(parse_11_signup(driver,df_input,crawl_data_none,i,""))
    print(i)

crawl_data.to_csv("test0413_r.csv", encoding = "utf-8-sig")

#네이버쇼핑
# for i in range(181,len(df_input)):
for i in range(3):
    if i % 30 == 0 and i != 0:        
        time.sleep(60)
    crawl_data.to_csv("test0413_r.csv", encoding = "utf-8-sig")
    print(i)
    crawl_data = crawl_data.append(parse_naver_shopping(driver,df_input,crawl_data_none,i,"all"))



crawl_data = fix(crawl_data,'text')
crawl_data(crawl_data,'text')
crawl_data.to_csv("test0413_r.csv", encoding = "utf-8-sig")
os.system("pause")