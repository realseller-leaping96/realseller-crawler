import pandas as pd
import pymysql
import pandas as pd
from sqlalchemy import create_engine
#########################################################
from module.add_valid import fillter, fix

a = pd.read_csv("test0413_r.csv")

a = fix(a,'text')
fillter(a,'text')


import pymysql
import pandas as pd
from sqlalchemy import create_engine

# MySQL Connector using pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

#내DB에 백업
engine = create_engine("mysql+mysqldb://root:"+"123123"+"@localhost/gidseller", encoding='utf-8')
conn = engine.connect()
a.to_sql(name='review_list', con=engine, if_exists='append', index=False)


#내DB => g5_phone_review (새로 추가된 기종만 리뷰추가하게 만들어놓음)
connection = pymysql.connect(host='localhost', user='root', password='123123', db='gidseller')
try:
    with connection.cursor() as cursor:
        sql =( "INSERT INTO g5_phone_review (pr_model_code ,pr_model_name ,pr_star ,pr_market ,pr_write_id ,pr_upload_date ,pr_title ,pt_text ,pr_url )"
              "(SELECT pl_model_code, pl_name, star, market, write_id, upload_date, title, content, URL FROM review_list WHERE pl_model_code NOT IN (SELECT DISTINCT pr_model_code FROM g5_phone_review))" )

        cursor.execute(sql)

    connection.commit()

finally:
    connection.close()





