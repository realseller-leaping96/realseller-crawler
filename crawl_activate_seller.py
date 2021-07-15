import module.chrome_driver_module as chrome_driver_module
import module.db_module as db_module
import pandas as pd
import numpy as np

from module.activate_seller.naver_jungo.main import naver_jungo
from module.activate_seller.bunjang.main import bunjang

db_class = db_module.Database() #db연결 생성
driver = chrome_driver_module.ChromeDriver().driver

   #############################################
  #        워닛 판매자 활동여부 크롤링         #
 #  입력: ? / 출력: activate_seller 테이블    #
#############################################

# 결과데이터 형식 정의
my_dict = {
    "vendor_type" : "", 
    "fsl_rs_id" : "",               #리얼셀러 아이디
    "shop_id":"",                   #네이버/번장 판매자 아이디
    "last_sell": "",                #가장최근 판매글 게시일
    "sell_count": "",               #2주간 판매중인 물품 갯수
    "dealing_smartphone": "",       #2주간 스마트폰 품목 취급여부
    "is_activate": ""               #종합적으로 판단한 최종 활동여부
}
crawl_data = pd.DataFrame(my_dict,index=[0])

seller_list = pd.read_excel('셀러리스트.xlsx').fillna(np.NAN) #입력데이터

# for i in range(len(seller_list)):
for i in range(2): #테스트용
    
    #네이버판매처 크롤링
    crawl_data = naver_jungo(crawl_data,seller_list,i,driver)

    #번개장터판매처 크롤링
    crawl_data = bunjang(crawl_data,seller_list,i,driver)
    
print(crawl_data)
        
    
    



