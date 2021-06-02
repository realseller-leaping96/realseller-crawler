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

def collet_one(driver,xpath,option):
    result =  driver.find_element_by_xpath(xpath).text
    
    if option == "5G" and result.find("5G") != -1:
        result = "5G"

    if option == "5G" and result != "5G":
        result = ""

    if option == "4G" and result.find("4G") != -1:
        result = "4G"
    
    if option == "4G" and result.find("LTE") != -1:
        result = "4G"

    if option == "4G" and result == "":
        result = ""
        
    if option == "유심타입" and result.find("유심") != -1:
        result_list = result.split("/")
        for r in result_list:
            if r.find("유심") != -1:
                result = r
    
    if option == "충전단자" and result.find("유심") != -1:
        result_list = result.split("/")
        if len(result_list) > 1:
            for r in result_list:
                if r.find("유심") == -1:
                    result = r
        else:
            result = ""
    
    #동영상촬영일경우 해상도에다 촬영프레임정보 추가하기
    if option == "동영상촬영" :
        xpath = '//*[@id="product_specview"]/div[1]/form/div[18]/div[4]/span'
        result = result + driver.find_element_by_xpath(xpath).text
        
    #동영상해상도일경우 해상도에다 비디오프레임정보 추가하기
    if option == "동영상해상도" :
        xpath = '//*[@id="product_specview"]/div[1]/form/div[20]/div[2]/span'
        result = result +" "+ driver.find_element_by_xpath(xpath).text
        
    if option == "가로" and len(result.split('x'))>1 :
        result = result.split('x')[0]
        
    if option == "세로" and len(result.split('x'))>1:
        result = result.split('x')[1]
        
    if option == "두께" and len(result.split('x'))>1:
        result = result.split('x')[2]
        
    if option == "지문" and result.find("지문인식") != -1:
        result = "지문인식"

    if option == "지문" and result.find("지문인식") == -1:
        result = ""
        
    if option == "얼굴" and result.find("얼굴인식") != -1:
        result = "얼굴인식"

    if option == "얼굴" and result.find("얼굴인식") == -1:
        result = ""
        
    if option == "홍채" and result.find("홍채인식") != -1:
        result = "홍채인식"

    if option == "홍채" and result.find("홍채인식") == -1:
        result = ""
        
    return result

def parse_cetizen(df_input,driver,crawl_data, a,b):
    for index in range(a,b):
        url1 = "https://review.cetizen.com/review.php?q=phone&just_one=&just_one_name=&just_one_pcat=&keyword_p="
        url2 = "&p_data=3&p_split=&recnum=10"
        driver.get(url1+df_input.iloc[index][2]+url2)
        print(index,url1+df_input.iloc[index][2]+url2)
        if hasxpath(driver,'//*[@id="product_list"]/div/div[3]/div[1]/div[1]/div/a/span') == True:
            driver.find_element_by_xpath('//*[@id="product_list"]/div/div[3]/div[1]/div[1]/div/a/span').click()
            driver.implicitly_wait(10)
            
            my_dict = {
                #기본정보
                "모델명": collet_one(driver,'/html/body/div[10]/div[3]/div[1]/div[2]/div[1]/div[1]/div/a/span',""),
                "모델코드": df_input.iloc[index][2],
                "제조회사": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[1]/div[2]/span',""),
                "출시일": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[1]/div[4]/span',""),
                "운영체제": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[2]/div[4]/span',""),
                "판매방식": "",
                
                #화면정보
                "화면크기(센치)": "",
                "화면크기(인치)":collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[7]/div[2]/span',""),
                "패널종류": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[8]/div[4]/span',""),
                "화면해상도": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[7]/div[4]/span',"").replace(" 픽셀",""), 
                "ppi": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[8]/div[2]/span',"".replace(" ppi","")), 
                "최대주사율": "",
                "화면비": "",
                "화면면적": "",
                "화면폭": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[9]/div[2]/span',"").replace(" mm",""),
                "화면높이": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[9]/div[4]/span',"").replace(" mm",""),
                "HDR규격": "",
                
                #시스템
                "AP종류": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[11]/div[2]/span',""), 
                "코어갯수": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[12]/div[2]/span',""),
                "코어클럭": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[12]/div[4]/span',""), 
                "그래픽코어": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[13]/div[2]/span',""),
                "NPU & DSP": "",
                "Sensor Hub": "",
                "시스템램": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[13]/div[4]/span',""),
                "내장메모리": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[14]/div[2]/span',""),
                "저장장치": "",
                "외장메모리": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[14]/div[4]/span',""),
                
                #네트워크
                "5G": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[25]/div[4]/span',"5G"),
                "4G": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[25]/div[4]/span',"4G"),
                "WI-FI주파수": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[26]/div[2]/span',""),
                "블루투스": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[26]/div[4]/span',""),
                "위성항법": "",
                "유심타입": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[5]/div[4]/span',"유심타입"),
                "듀얼유심": "",
                
                #카메라
                "카메라타입": "",
                "후면카메라": "",
                "전면카메라": "",
                "동영상촬영": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[18]/div[2]/span',"동영상촬영"),
                "Flash": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[17]/div[2]/span',""),
                "사진촬영 해상도": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[17]/div[4]/span',""),
                "전면 해상도":  collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[19]/div[2]/span',""),
                # "전면 동영상 해상도": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[19]/div[4]/span',"동영상해상도"),
                "전면 동영상 해상도": "",
                "조리개 값": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[16]/div[4]/span',""),
                "카메라 특징": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[20]/div[4]/span',""),
                "손떨림보정": "",
                
                #카메라기능
                "손떨림방지": "",
                "카메라플래시": "",
                "HDR촬영지원": "",
                "오토HDR": "",
                "광학줌": "",
                "지오태그": "",
                "레이저 오토포커스": "",
                "오토 포커스": "",
                "아웃 포커스": "",
                "터치 포커스": "",
                "파노라마": "",
                "TOF센서": "",
                "야간모드 촬영": "",
                
                #사운드
                "이어폰단자": "",
                "스피커": "",
                "고음질재생": "",
                "사운드 기술": "",
                
                #보안/기능
                "지문인식": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[28]/div[4]/span',""),
                "얼굴인식": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[28]/div[4]/span',""),
                "홍채인식": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[28]/div[4]/span',""),
                "음성잠금해제": "",
                "AI/인공지능": "",
                "전자결제": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[29]/div[2]/span',""),
                "터치펜": "",
                "방수/방진": "",
                
                #배터리
                "기타": "",
                "충전단자": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[5]/div[4]/span',"충전단자"),
                "배터리용량": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[22]/div[2]/span',"").replace(" mAh",""),
                "배터리타입": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[22]/div[4]/span',""),
                "배터리특징": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[23]/div[2]/span',""),
                "배터리장착방식": "",
                "충전지원": "",
                "고속충전기술": "",
                "무선충전": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[23]/div[4]/span',""),
                
                #색상
                "색상": "",
                
                #규격
                "가로": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[4]/div[4]/span',"가로"),
                "세로": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[4]/div[4]/span',"세로"),
                "두께": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[4]/div[4]/span',"두께"),
                "무게": driver.find_element_by_xpath('//*[@id="product_specview"]/div[1]/form/div[5]/div[2]/span').text.replace("g","")
            }
            my_dict['사이트명'] = "세티즌"
            crawl_data = crawl_data.append(pd.DataFrame(my_dict,index=[0]))
        else:
            pass
        
    return crawl_data

def add(df_input,driver,crawl_data, a,b):
    for index in range(a,b):

        if df_input.iloc[index]['세티즌링크'] != "":
            driver.get(df_input.iloc[index]['세티즌링크'])
            print(index,  df_input.iloc[index]['세티즌링크'] )

            #req = driver.page_source
            #soup=BeautifulSoup(req, 'html.parser')
            
            my_dict = {
                #기본정보
                "모델명": df_input.iloc[index]['pl_name'],
                "모델코드": df_input.iloc[index]['pl_model_code'],
                "제조회사": df_input.iloc[index]['pl_maker'],
                "출시일": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[1]/div[4]/span',""),
                "운영체제": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[2]/div[4]/span',""),
                "판매방식": "",
                
                #화면정보
                "화면크기(센치)": "",
                "화면크기(인치)":collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[7]/div[2]/span',""),
                "패널종류": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[8]/div[4]/span',""),
                "화면해상도": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[7]/div[4]/span',"").replace(" 픽셀",""), 
                "ppi": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[8]/div[2]/span',"".replace(" ppi","")), 
                "최대주사율": "",
                "화면비": "",
                "화면면적": "",
                "화면폭": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[9]/div[2]/span',"").replace(" mm",""),
                "화면높이": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[9]/div[4]/span',"").replace(" mm",""),
                "HDR규격": "",
                
                #시스템
                "AP종류": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[11]/div[2]/span',""), 
                "코어갯수": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[12]/div[2]/span',""),
                "코어클럭": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[12]/div[4]/span',""), 
                "그래픽코어": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[13]/div[2]/span',""),
                "NPU & DSP": "",
                "Sensor Hub": "",
                "시스템램": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[13]/div[4]/span',""),
                "내장메모리": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[14]/div[2]/span',""),
                "저장장치": "",
                "외장메모리": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[14]/div[4]/span',""),
                
                #네트워크
                "5G": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[25]/div[4]/span',"5G"),
                "4G": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[25]/div[4]/span',"4G"),
                "WI-FI주파수": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[26]/div[2]/span',""),
                "블루투스": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[26]/div[4]/span',""),
                "위성항법": "",
                "유심타입": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[5]/div[4]/span',"유심타입"),
                "듀얼유심": "",
                
                #카메라
                "카메라타입": "",
                "후면카메라": "",
                "전면카메라": "",
                "동영상촬영": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[18]/div[2]/span',"동영상촬영"),
                "Flash": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[17]/div[2]/span',""),
                "사진촬영 해상도": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[17]/div[4]/span',""),
                "전면 해상도":  collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[19]/div[2]/span',""),
                # "전면 동영상 해상도": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[19]/div[4]/span',"동영상해상도"),
                "전면 동영상 해상도": "",
                "조리개 값": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[16]/div[4]/span',""),
                "카메라 특징": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[20]/div[4]/span',""),
                "손떨림보정": "",
                
                #카메라기능
                "손떨림방지": "",
                "카메라플래시": "",
                "HDR촬영지원": "",
                "오토HDR": "",
                "광학줌": "",
                "지오태그": "",
                "레이저 오토포커스": "",
                "오토 포커스": "",
                "아웃 포커스": "",
                "터치 포커스": "",
                "파노라마": "",
                "TOF센서": "",
                "야간모드 촬영": "",
                
                #사운드
                "이어폰단자": "",
                "스피커": "",
                "고음질재생": "",
                "사운드 기술": "",
                
                #보안/기능
                "지문인식": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[28]/div[4]/span',"지문"),
                "얼굴인식": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[28]/div[4]/span',"얼굴"),
                "홍채인식": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[28]/div[4]/span',"홍채"),
                "음성잠금해제": "",
                "AI/인공지능": "",
                "전자결제": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[29]/div[2]/span',""),
                "터치펜": "",
                "방수/방진": "",
                
                #배터리
                "기타": "",
                "충전단자": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[5]/div[4]/span',"충전단자"),
                "배터리용량": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[22]/div[2]/span',"").replace(" mAh",""),
                "배터리타입": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[22]/div[4]/span',""),
                "배터리특징": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[23]/div[2]/span',""),
                "배터리장착방식": "",
                "충전지원": "",
                "고속충전기술": "",
                "무선충전": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[23]/div[4]/span',""),
                
                #색상
                "색상": "",
                
                #규격
                "가로": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[4]/div[4]/span',"가로"),
                "세로": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[4]/div[4]/span',"세로"),
                "두께": collet_one(driver,'//*[@id="product_specview"]/div[1]/form/div[4]/div[4]/span',"두께"),
                "무게": driver.find_element_by_xpath('//*[@id="product_specview"]/div[1]/form/div[5]/div[2]/span').text.replace("g","")
            }
            my_dict['사이트명'] = "세티즌"
            crawl_data = crawl_data.append(pd.DataFrame(my_dict,index=[0]))
        else:
            pass
        
    return crawl_data

def URL(df_input,driver,crawl_data, a,b):
    for index in range(a,b):
        url1 = "https://review.cetizen.com/review.php?q=phone&just_one=&just_one_name=&just_one_pcat=&keyword_p="
        url2 = "&p_data=3&p_split=&recnum=10"
        driver.get(url1+df_input.iloc[index]['pl_model_code']+url2)
        print(index,url1+df_input.iloc[index]['pl_model_code']+url2)
        if hasxpath(driver,'//*[@id="product_list"]/div/div[3]/div[1]/div[1]/div/a/span') == True:
            # driver.find_element_by_xpath('//*[@id="product_list"]/div/div[3]/div[1]/div[1]/div/a/span').click()
            driver.implicitly_wait(10)
            
            my_dict = {
                #기본정보
                "pl_id": df_input.iloc[index]['pl_id'],
                "pl_maker": df_input.iloc[index]['pl_maker'],
                "pl_model_code": df_input.iloc[index]['pl_model_code'],
                "pl_name": df_input.iloc[index]['pl_name'],
                "pl_model_name": df_input.iloc[index]['pl_model_name'],
                "나무링크": "",
                "세티즌링크": driver.current_url,
                "다나와링크": "",
                "타겟": collet_one(driver,'//*[@id="product_list"]/div/div[3]/div[1]/div[1]/div[1]/a/span',""),
                
            }
            crawl_data = crawl_data.append(pd.DataFrame(my_dict,index=[0]))
        else:
            pass
        
    return crawl_data