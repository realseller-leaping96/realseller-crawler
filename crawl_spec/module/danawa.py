import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import re
import os

def hasxpath(driver,xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False

def parse_danawa(df_input, driver, crawl_data, a,b):
    for index in range(a,b):
        print(index)
        url1 = "http://search.danawa.com/dsearch.php?query="
        url2 = "&cate_c1=224&cate_c2=48419&volumeType=allvs&page=1&limit=40&sort=saveDESC&list=list&boost=true&addDelivery=N&recommendedSort=Y&defaultUICategoryCode=122514&defaultPhysicsCategoryCode=224%7C48419%7C48766%7C0&defaultVmTab=1363&defaultVaTab=1401402&tab=main"
        driver.get(url1+df_input.iloc[index]['pl_name']+url2)
    
        if hasxpath(driver,'//*[@id="productListArea"]/div[3]/ul/li[1]/div/div[1]/a[1]') == True:
            href = driver.find_element_by_xpath('//*[@id="productListArea"]/div[3]/ul/li[1]/div/div[1]/a[1]').get_attribute("href")
            driver.get(href)
            driver.implicitly_wait(10)
            
            
            temp_dict = dict()
            
            temp_dict["모델명"] = df_input.iloc[index]['pl_name']
            temp_dict["모델코드"] = df_input.iloc[index]['pl_model_code']
            temp_dict["제조회사"] = df_input.iloc[index]['pl_maker']
            
            
            req = driver.page_source
            soup=BeautifulSoup(req, 'html.parser')
            table = ""
            
            #일반 상세정보테이블
            if soup.select("#productDescriptionArea > .detail_cont > .prod_spec > .spec_tbl"):
                table = soup.select("#productDescriptionArea > .detail_cont > .prod_spec > .spec_tbl")[0]
            else:
                pass
            
            #다나와 제작CM도 해야하나???
            #print(table)
            if table != "":
                trs = table.select("tr")

                for tr in trs:
                    th = tr.select("th")
                    td = tr.select("td")
                    if len(th) == 0:
                        pass
                    elif len(th) == 1:
                        #print(th[0].text)
                        pass
                    elif len(th) == 2:
                        #print(th[0].text, th[1].text)
                        #print(td[0].text)
                        if th[0].text == "제조회사":
                            temp_dict["제조회사"] = td[0].text
                        elif th[0].text == "운영체제":
                            temp_dict["운영체제"] = td[0].text
                        elif th[0].text == "화면크기(인치)":
                            temp_dict["화면크기(인치)"] = td[0].text
                        elif th[0].text == "화면해상도":
                            temp_dict["화면해상도"] = td[0].text
                        elif th[0].text == "최대주사율":
                            temp_dict["최대주사율"] = td[0].text
                        elif th[0].text == "화면면적":
                            temp_dict["화면면적"] = td[0].text

                        elif th[0].text == "AP종류":
                            temp_dict["AP종류"] = td[0].text
                        elif th[0].text == "코어클럭":
                            temp_dict["코어클럭"] = td[0].text
                        elif th[0].text == "시스템램":
                            temp_dict["시스템램"] = td[0].text
                        elif th[0].text == "저장장치":
                            temp_dict["저장장치"] = td[0].text

                        elif th[0].text == "5G":
                            temp_dict["5G"] = td[0].text
                        elif th[0].text == "Wi-Fi주파수":
                            temp_dict["WI-FI주파수"] = td[0].text
                        elif th[0].text == "유심타입":
                            temp_dict["유심타입"] = td[0].text

                        elif th[0].text == "카메라타입":
                            temp_dict["카메라타입"] = td[0].text
                        elif th[0].text == "전면카메라":
                            temp_dict["전면카메라"] = td[0].text
                        elif th[0].text == "조리개값":
                            temp_dict["조리개 값"] = td[0].text
                            
                        elif th[0].text == "손떨림방지":
                            temp_dict["손떨림방지"] = td[0].text
                        elif th[0].text == "HDR촬영지원":
                            temp_dict["HDR촬영지원"] = td[0].text
                        elif th[0].text == "광학줌":
                            temp_dict["광학줌"] = td[0].text
                        elif th[0].text == "레이저 오토포커스":
                            temp_dict["레이저 오토포커스"] = td[0].text
                        elif th[0].text == "아웃 포커스":
                            temp_dict["아웃 포커스"] = td[0].text
                        elif th[0].text == "파노라마":
                            temp_dict["파노라마"] = td[0].text
                        elif th[0].text == "야간모드촬영":
                            temp_dict["야간모드 촬영"] = td[0].text
                            

                        elif th[0].text == "이어폰단자":
                            temp_dict["이어폰단자"] = td[0].text
                        elif th[0].text == "고음질재생":
                            temp_dict["고음질재생"] = td[0].text

                        elif th[0].text == "지문인식":
                            temp_dict["지문인식"] = td[0].text
                        elif th[0].text == "홍채인식":
                            temp_dict["홍채인식"] = td[0].text
                        elif th[0].text == "AI/인공지능":
                            temp_dict["AI/인공지능"] = td[0].text
                        elif th[0].text == "터치펜":
                            temp_dict["터치펜"] = td[0].text

                        elif th[0].text == "충전단자":
                            temp_dict["충전단자"] = td[0].text
                        elif th[0].text == "배터리장착방식":
                            temp_dict["배터리장착방식"] = td[0].text
                        elif th[0].text == "고속충전기술":
                            temp_dict["고속충전기술"] = td[0].text

                        elif th[0].text == "가로":
                            temp_dict["가로"] = td[0].text
                        elif th[0].text == "두께":
                            temp_dict["두께"] = td[0].text

                        ###########################################

                        if th[1].text == "출시일":
                            temp_dict["출시일"] = td[1].text
                        elif th[1].text == "판매방식":
                            temp_dict["판매방식"] = td[1].text

                        elif th[1].text == "패널종류":
                            temp_dict["패널종류"] = td[1].text
                        elif th[1].text == "ppi":
                            temp_dict["ppi"] = td[1].text
                        elif th[1].text == "화면비":
                            temp_dict["화면비"] = td[1].text
                        elif th[1].text == "HDR규격":
                            temp_dict["HDR규격"] = td[1].text

                        elif th[1].text == "코어갯수":
                            temp_dict["코어갯수"] = td[1].text
                        elif th[1].text == "그래픽코어":
                            temp_dict["그래픽코어"] = td[1].text
                        elif th[1].text == "내장메모리":
                            temp_dict["내장메모리"] = td[1].text
                        elif th[1].text == "외장메모리":
                            temp_dict["외장메모리"] = td[1].text

                        elif th[1].text == "4G":
                            temp_dict["4G"] = td[1].text
                        elif th[1].text == "블루투스":
                            temp_dict["블루투스"] = td[1].text
                        elif th[1].text == "듀얼유심":
                            temp_dict["듀얼유심"] = td[1].text

                        elif th[1].text == "후면카메라":
                            temp_dict["후면카메라"] = td[1].text
                        elif th[1].text == "동영상촬영":
                            temp_dict["동영상촬영"] = td[1].text
                        elif th[1].text == "손떨림보정":
                            temp_dict["손떨림보정"] = td[1].text
                            
                        elif th[1].text == "카메라플래시":
                            temp_dict["카메라플래시"] = td[1].text
                        elif th[1].text == "오토HDR":
                            temp_dict["오토HDR"] = td[1].text
                        elif th[1].text == "지오태그":
                            temp_dict["지오태그"] = td[1].text
                        elif th[1].text == "오토 포커스":
                            temp_dict["오토 포커스"] = td[1].text
                        elif th[1].text == "터치 포커스":
                            temp_dict["터치 포커스"] = td[1].text
                        elif th[1].text == "TOF센서":
                            temp_dict["TOF센서"] = td[1].text

                        elif th[1].text == "스피커":
                            temp_dict["스피커"] = td[1].text
                        elif th[1].text == "사운드기술":
                            temp_dict["사운드기술"] = td[1].text
                        elif th[1].text == "얼굴인식":
                            temp_dict["얼굴인식"] = td[1].text

                        elif th[1].text == "음성잠금해제":
                            temp_dict["음성잠금해제"] = td[1].text
                        elif th[1].text == "전자결제":
                            temp_dict["전자결제"] = td[1].text
                        elif th[1].text == "방수/방진":
                            temp_dict["방수/방진"] = td[1].text

                        elif th[1].text == "배터리용량":
                            temp_dict["배터리용량"] = td[1].text
                        elif th[1].text == "충전지원":
                            temp_dict["충전지원"] = td[1].text
                        elif th[1].text == "무선충전":
                            temp_dict["무선충전"] = td[1].text

                        elif th[1].text == "세로":
                            temp_dict["세로"] = td[1].text
                        elif th[1].text == "무게":
                            temp_dict["무게"] = td[1].text

                    
            temp_dict["타겟제품"] = driver.find_element_by_xpath('//*[@id="blog_content"]/div[2]/div[1]/h3').text
            temp_dict["사이트명"] = "다나와"
            crawl_data = crawl_data.append(pd.DataFrame(temp_dict,index=[0]))
    return crawl_data
                
                
                