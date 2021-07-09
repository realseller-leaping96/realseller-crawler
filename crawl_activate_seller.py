import module.chrome_driver_module as chrome_driver_module
import module.db_module as db_module
import pandas as pd
import numpy as np

db_class = db_module.Database() #db연결 생성
driver = chrome_driver_module.ChromeDriver().driver

seller_list = pd.read_excel('셀러리스트.xlsx').fillna(np.NAN)


for i in range(len(seller_list)):
    # url_naver_1 = """
    # https://m.cafe.naver.com/ArticleSearchList.nhn?search.query=
    # """
    # naver_nick = 
    # url_naver_2= """
    # &search.menuid=0&search.searchBy=3&search.sortBy=date&search.clubid=10050146
    # &search.option=0&search.defaultValue=1
    # """
    if pd.notnull(seller_list.iloc[i]['fsl_rs_naver_nickname']):
        print(seller_list.iloc[i]['fsl_rs_naver_nickname'])