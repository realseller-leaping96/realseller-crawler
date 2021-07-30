from db_config import DbConfig
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import pandas as pd
import sqlalchemy

class DbModel:
    def __init__(self,db_name):
        db_str = DbConfig().test(db_name)
        self.db = pymysql.connect(
            host=db_str['host'], \
            user=db_str['user'], \
            password=db_str['password'], \
            db=db_str['database'], \
            charset='utf8', \
            autocommit=True\
        )

        self.engine = sqlalchemy.create_engine(
            "mysql+mysqldb://"+\
            db_str['user']\
            +":"\
            +db_str['password']\
            +"@"\
            +db_str['host']\
            +"/"
            +db_str['database']\
            , encoding='utf-8'
        )
        print("DB켜짐")
    
    def end(self):
        print("DB꺼짐")
        self.db.close()

    def get_test_data(self):
        cur = self.db.cursor(pymysql.cursors.DictCursor)
        query = "select * from activate_seller"
        cur.execute(query)
        result = cur.fetchall()
        cur.close
        return result

    def get_table_dataframe(self,table_name):
        return pd.read_sql_table(table_name,self.engine) 

