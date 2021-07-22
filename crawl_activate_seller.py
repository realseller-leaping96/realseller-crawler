import module.chrome_driver_module as chrome_driver_module
import module.db_module as db_module
import pandas as pd
import numpy as np

from module.activate_seller.naver_jungo.main import naver_jungo
from module.activate_seller.bunjang.main import bunjang
from module.db_module import CreateTableIfNotExists
from sqlalchemy import Table, Column, Integer, String, Boolean, Date
from module.activate_seller.rearrange_as_id import rearrange_as_id
from module.activate_seller.naver_jungo.auto_login import auto_login
from module.activate_seller.naver_jungo.auto_login_for_linux import auto_login_for_liunux

db_class = db_module.Database() #db연결 생성

######### activate_seller 테이블 없다면 정의해주는 부분 ###########
table = Table(
    "activate_seller",
    db_class.metadata,
    Column("as_id", Integer, primary_key=True),
    Column("vendor_type", String(50)),
    Column("fsl_rs_id", String(50)),
    Column("shop_id", String(50)),
    Column("last_sell", Date),
    Column("sell_count", Integer),
    Column("dealing_smartphone", Integer),
    Column("is_activate", Boolean),
    mysql_auto_increment='0',
)
db_class.engine.execute(CreateTableIfNotExists(table))


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

seller_list = pd.read_sql_table('g5_real_seller_list',db_class.engine_conn) #입력데이터

#중고나라 회원인 네이버 아이디 로그인
# auto_login(driver)
auto_login_for_liunux(driver)

for i in range(len(seller_list)):
# for i in range(2): #테스트용
    print(i)

    #네이버판매처 크롤링
    crawl_data = naver_jungo(crawl_data,seller_list,i,driver)

    #번개장터판매처 크롤링
    crawl_data = bunjang(crawl_data,seller_list,i,driver)

crawl_data = crawl_data.reset_index()
indexNames = crawl_data[crawl_data['vendor_type'] == "" ].index
crawl_data.drop(indexNames,inplace=True)
crawl_data = crawl_data.drop(['index'], axis='columns')

activate_seller = pd.read_sql_table('activate_seller',db_class.engine_conn).drop(['as_id'], axis='columns') #기존테이블 로드
crawl_data = crawl_data.append(activate_seller, ignore_index=True)
crawl_data = crawl_data.drop_duplicates(['fsl_rs_id','shop_id'], keep='last')


try:    
    with db_class.cursor as cursor:
        cursor.execute("DELETE FROM activate_seller;")
        db_class.db_conn.commit()
        
finally:
     db_class.db_conn.close()

crawl_data.to_sql(name='activate_seller', con=db_class.engine, if_exists='append', index=False)
db_class.engine_conn.close()
    
rearrange_as_id()


