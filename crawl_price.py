import pandas as pd
from selenium import webdriver
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from module.price.cetizen_cal import parse_by_telecom_maker #세티즌 가격크롤러
import pandas as pd
#########################################
# 세티즌 가격계산기 크롤링 #
#########################################
my_dict = {
    "통신사" : "",
    "모델명": "",
    "모델코드": "",
    "가격": ""
}
crawl_data = pd.DataFrame(my_dict,index=[0])

driver  = webdriver.Chrome()
driver.implicitly_wait(3)

telecoms = ["SKT","KT","LG"]
makers = ["삼성전자", "애플", "LG전자"]

for telecom in telecoms:
    for maker in makers:
        crawl_data = parse_by_telecom_maker(telecom,maker,crawl_data,driver,my_dict)

#########################################
# 통신사별 가격 라벨링하여 테이블에 저장 #
#########################################
df_input = crawl_data
my_dict = {
    "model_name": "",              #모델이름
    "model_code": "",              #모델코드
    "price": "",                       #가격
}

to_db = pd.DataFrame(my_dict,index=[0])


for i in range(len(crawl_data)):
    
    price = ""
    
    #skt
    if df_input.iloc[i]['통신사'] == "SKT":
        price = "SKT:"+df_input.iloc[i]['가격']
    
    #kt
    if df_input.iloc[i]['통신사'] == "KT" and price == "":
        price = "KT:"+df_input.iloc[i]['가격'] 
    elif df_input.iloc[i]['통신사'] == "KT" and price != "":
        price = price +"|KT:"+df_input.iloc[i]['가격'] 
    
    #lg
    if df_input.iloc[i]['통신사'] == "LG" and price == "":
        price = "LG:"+df_input.iloc[i]['가격'] 
    elif df_input.iloc[i]['통신사'] == "LG" and price != "":
        price = price +"|LG:"+df_input.iloc[i]['가격']   
            
    print(i)
    my_dict = {
        "model_name": df_input.iloc[i]['모델명'],              #모델이름
        "model_code": df_input.iloc[i]['모델코드'].replace("/",""),              #모델코드
        "price": price.replace(",","").replace("원",""),                       #가격
    }
    to_db = to_db.append(pd.DataFrame(my_dict, index=[0]))

#내DB => price_list
connection = pymysql.connect(host='localhost', user='root', password='123123', db='gidseller')
try:
    with connection.cursor() as cursor:
        sql =( "CREATE TABLE if not exists `price_list` (`price_id` INT(11) NOT NULL AUTO_INCREMENT,"+
              "`model_name` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',"+
              "`model_code` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',"+
              "`price` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',"+
              "PRIMARY KEY (`price_id`) USING BTREE"+
              ")COLLATE='utf8mb4_general_ci'"+
              "ENGINE=InnoDB;" 
             )
        cursor.execute(sql)

    connection.commit()

finally:
    connection.close()
    

#내DB에 백업
engine = create_engine("mysql+mysqldb://root:"+"123123"+"@localhost/gidseller", encoding='utf-8')
conn = engine.connect()
to_db.to_sql(name='price_list', con=engine, if_exists='append', index=False)