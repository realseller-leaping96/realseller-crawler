import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re
import os

#######################내가 정의한 모듈##############################################


from module.namuwiki.checking import hasxpath #해당되는 xpath 요소 존재여부 확인하는 함수 => True/False로 리턴
from module.namuwiki.select_table import select_table #사양테이블 선택

from module.namuwiki.crawl_battery_row import crawl_battery_row
from module.namuwiki.crawl_biometrics_row import crawl_biometrics_row
from module.namuwiki.crawl_camera_row import crawl_camera_row
from module.namuwiki.crawl_color_row import crawl_color_row
from module.namuwiki.crawl_disp_row import crawl_disp_row
from module.namuwiki.crawl_etc_row import crawl_etc_row
from module.namuwiki.crawl_mem_row import crawl_mem_row
from module.namuwiki.crawl_network_row import crawl_network_row
from module.namuwiki.crawl_os_row import crawl_os_row
from module.namuwiki.crawl_proc_row import crawl_proc_row
from module.namuwiki.crawl_proximity_row import crawl_proximity_row
from module.namuwiki.crawl_satlite_row import crawl_satlite_row
from module.namuwiki.crawl_size_row import crawl_size_row
from module.namuwiki.crawl_terminal_row import crawl_terminal_row
from selenium import webdriver


def parse_namu(df_input, driver, df_output, a,b):
    for index in range(a,b):
        print(index,  df_input.iloc[index]['나무위키링크단품'] )
        temp_dict = dict()
            
        temp_dict["모델명"] = df_input.iloc[index]['pl_name']
        temp_dict["모델코드"] = df_input.iloc[index]['pl_model_code']
        temp_dict["제조회사"] = df_input.iloc[index]['pl_maker']

        if df_input.iloc[index]['나무위키링크단품'] != "":
            driver.get(df_input.iloc[index]['나무위키링크단품'])

            req = driver.page_source
            soup=BeautifulSoup(req, 'html.parser')

            table = select_table(soup)
                
            trs = table.select("tr")
            next_is_core_clock = 0
            for tr in trs:
                td = tr.select("td")
                if len(td) <= 0:
                    continue
            
                if td[0].text == "프로세서" and "AP종류" not in temp_dict:
                    temp_dict = crawl_proc_row(temp_dict, td)

                elif td[0].text == "메모리" and "시스템램" not in temp_dict:
                    temp_dict = crawl_mem_row(temp_dict, td)
                        
                elif td[0].text == "디스플레이" and "화면비" not in temp_dict:
                    temp_dict = crawl_disp_row(temp_dict, td)

                elif td[0].text == "네트워크" and "5G" not in temp_dict:
                    temp_dict = crawl_network_row(temp_dict, td) 
                        
                elif td[0].text == "근접통신" and "블루투스" not in temp_dict:
                    temp_dict = crawl_proximity_row(temp_dict, td)

                elif td[0].text == "위성항법" and "위성항법" not in temp_dict:
                    temp_dict = crawl_satlite_row(temp_dict, td)
                
                elif td[0].text == "카메라" and "전면카메라" not in temp_dict:
                    temp_dict = crawl_camera_row(temp_dict,td)
                    
                elif td[0].text == "배터리" and "배터리용량" not in temp_dict:
                    temp_dict = crawl_battery_row(temp_dict,td)
            
                elif td[0].text == "운영체제" and "운영체제" not in temp_dict:
                    temp_dict = crawl_os_row(temp_dict, td)
            
                elif td[0].text == "규격" :
                    temp_dict = crawl_size_row(temp_dict, td)
            
                elif td[0].text.find("색상") != -1 and "색상" not in temp_dict :
                    temp_dict = crawl_color_row(temp_dict, td)
            
                elif td[0].text == "단자정보" and "충전단자" not in temp_dict :
                    temp_dict = crawl_terminal_row(temp_dict, td)
        
                elif td[0].text == "생체인식":
                    temp_dict = crawl_biometrics_row(temp_dict,td)
            
                elif td[0].text == "기타":
                    temp_dict = crawl_etc_row(temp_dict, td)
        temp_dict['사이트명'] = "나무위키"
        df_output = df_output.append(pd.DataFrame(temp_dict,index=[0]))

    return df_output


def add(df_input, driver, df_output, a,b):
    for index in range(a,b):
        print(index,  df_input.iloc[index]['나무링크'] )
        temp_dict = dict()
            
        temp_dict["모델명"] = df_input.iloc[index]['pl_name']
        temp_dict["모델코드"] = df_input.iloc[index]['pl_model_code']
        temp_dict["제조회사"] = df_input.iloc[index]['pl_maker']

        if df_input.iloc[index]['나무링크'] != "" and df_input.iloc[index]['나무링크'] != None:
            driver  = webdriver.Chrome()
            driver.get(df_input.iloc[index]['나무링크'])
            
            req = driver.page_source
            soup=BeautifulSoup(req, 'html.parser')

            table = select_table(soup)
            if table != "":
                trs = table.select("tr")
                next_is_core_clock = 0
                for tr in trs:
                    td = tr.select("td")
                    if len(td) <= 0:
                        continue
                
                    if td[0].text == "프로세서" and "AP종류" not in temp_dict:
                        temp_dict = crawl_proc_row(temp_dict, td)

                    elif td[0].text == "메모리" and "시스템램" not in temp_dict:
                        temp_dict = crawl_mem_row(temp_dict, td)
                            
                    elif td[0].text == "디스플레이" and "화면비" not in temp_dict:
                        temp_dict = crawl_disp_row(temp_dict, td)

                    elif td[0].text == "네트워크" and "5G" not in temp_dict:
                        temp_dict = crawl_network_row(temp_dict, td) 
                            
                    elif td[0].text == "근접통신" and "블루투스" not in temp_dict:
                        temp_dict = crawl_proximity_row(temp_dict, td)

                    elif td[0].text == "위성항법" and "위성항법" not in temp_dict:
                        temp_dict = crawl_satlite_row(temp_dict, td)
                    
                    elif td[0].text == "카메라" and "전면카메라" not in temp_dict:
                        temp_dict = crawl_camera_row(temp_dict,td)
                        
                    elif td[0].text == "배터리" and "배터리용량" not in temp_dict:
                        temp_dict = crawl_battery_row(temp_dict,td)
                
                    elif td[0].text == "운영체제" and "운영체제" not in temp_dict:
                        temp_dict = crawl_os_row(temp_dict, td)
                
                    elif td[0].text == "규격" :
                        temp_dict = crawl_size_row(temp_dict, td)
                
                    elif td[0].text.find("색상") != -1 and "색상" not in temp_dict :
                        temp_dict = crawl_color_row(temp_dict, td)
                
                    elif td[0].text == "단자정보" and "충전단자" not in temp_dict :
                        temp_dict = crawl_terminal_row(temp_dict, td)
            
                    elif td[0].text == "생체인식":
                        temp_dict = crawl_biometrics_row(temp_dict,td)
                
                    elif td[0].text == "기타":
                        temp_dict = crawl_etc_row(temp_dict, td)
                temp_dict['사이트명'] = "나무위키"
                df_output = df_output.append(pd.DataFrame(temp_dict,index=[0]))

        driver.quit()
    
    return df_output

def URL(df_input,driver,crawl_data, a,b):
    for index in range(a,b):
        driver  = webdriver.Chrome()
        url1 = "https://namu.wiki/Search?q="
        driver.get(url1+df_input.iloc[index]['pl_model_code'])  
        if hasxpath(driver,'//*[@id="app"]/div/div[2]/article/div[2]/section/div/h4/a') == True:
            driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/article/div[2]/section/div/h4/a').click()
            driver.implicitly_wait(10)
            
            my_dict = {
                #기본정보
                "pl_id": df_input.iloc[index]['pl_id'],
                "pl_maker": df_input.iloc[index]['pl_maker'],
                "pl_model_code": df_input.iloc[index]['pl_model_code'],
                "pl_name": df_input.iloc[index]['pl_name'],
                "pl_model_name": df_input.iloc[index]['pl_model_name'],
                "나무링크": driver.current_url,
                
            }
            print(driver.current_url)
            crawl_data = crawl_data.append(pd.DataFrame(my_dict,index=[0]))
        else:
            my_dict = {
                #기본정보
                "pl_id": df_input.iloc[index]['pl_id'],
                "pl_maker": df_input.iloc[index]['pl_maker'],
                "pl_model_code": df_input.iloc[index]['pl_model_code'],
                "pl_name": df_input.iloc[index]['pl_name'],
                "pl_model_name": df_input.iloc[index]['pl_model_name'],
                "나무링크": None
            }
            crawl_data = crawl_data.append(pd.DataFrame(my_dict,index=[0]))
            pass
        driver.quit()
        
    return crawl_data

