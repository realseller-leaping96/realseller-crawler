import pandas as pd
import pymysql
import pandas as pd
from sqlalchemy import create_engine


# df_complete_review = pd.read_csv("output_add.csv")
df_price = pd.read_csv("price.csv")

# MySQL Connector using pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

#detail_list에 백업
engine = create_engine("mysql+mysqldb://root:"+"123123"+"@localhost/gidseller", encoding='utf-8')
conn = engine.connect()

df_price.to_sql(name='price', con=engine, if_exists='append', index=False)


