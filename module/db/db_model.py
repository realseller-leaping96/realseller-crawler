####SQL부분
from pprint import pprint

from sqlalchemy.orm.session import Session
from module.db.db_config import DbConfig
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import pandas as pd

##### ORM 부분
import sqlalchemy
from sqlalchemy.schema import CreateTable
from sqlalchemy.ext.compiler import compiles
import re
from module.db.db_orm_table import code_matching
from module.db.db_orm_table import Base
from sqlalchemy.orm import sessionmaker


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

        Base.metadata.create_all(self.engine)

        print("DB켜짐")
        
    
    def end(self):
        print("DB꺼짐")
        self.engine.dispose()
        self.db.close()

    def get_test_data(self):
        cur = self.db.cursor(pymysql.cursors.DictCursor)
        query = "select * from activate_seller"
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result

    def get_table_dataframe(self,table_name):
        return pd.read_sql_table(table_name,self.engine) 

    def update_code_matching(self,result):
        ex_code_matching = pd.read_sql_table("code_matching",self.engine)

        cur = self.db.cursor(pymysql.cursors.DictCursor)
        query = "DELETE FROM code_matching"
        cur.execute(query)
        cur.close()

        temp_result = ex_code_matching.append(result).\
            reset_index().drop(['id','index'],axis=1).\
            reset_index().drop(['index'],axis=1).\
            drop_duplicates(['original_code','storage','mintit_code',\
                'bunjang_code','joongabi_code'],keep="last").\
            reset_index().drop(['index'],axis=1)

        temp_result.to_sql(name='code_matching', con=self.engine, if_exists='append', index=False)

        cur = self.db.cursor(pymysql.cursors.DictCursor)
        query = """
            SELECT 
                cm.id, 
                cm.original_code, 
                cm.`storage`,
                max(cm.mintit_code), 
                max(cm.bunjang_code),
                max(cm.joongabi_code), 
                max(cm.price_code) 
                FROM code_matching cm

            GROUP BY cm.original_code, cm.`storage`
        """
        
        cur.execute(query)
        result = cur.fetchall()
        final_result = pd.DataFrame(result).drop('id',axis=1)
        final_result.columns = ['original_code', 'storage', 'mintit_code','bunjang_code','joongabi_code','price_code']
        cur.close()

        cur = self.db.cursor(pymysql.cursors.DictCursor)
        query = "DELETE FROM code_matching"
        cur.execute(query)
        cur.close()
        
        final_result.to_sql(name='code_matching', con=self.engine, if_exists='append', index=False)

        cur = self.db.cursor(pymysql.cursors.DictCursor)
        query = """
            UPDATE code_matching cm 
            SET cm.bunjang_code = REPLACE(cm.bunjang_code, '_r', '');
        """
        cur.execute(query)
        cur.close()
        return

    # def init_autoincrement(self,table_name,pk_name):
    #     cur = self.db.cursor(pymysql.cursors.DictCursor)
    #     query_1 = "ALTER TABLE " + table_name +" AUTO_INCREMENT=1;"
    #     cur.execute(query_1)
    #     cur.close()

    #     cur = self.db.cursor(pymysql.cursors.DictCursor)
    #     query_2 = "SET @COUNT = 0;"
    #     cur.execute(query_2)
    #     cur.close()

    #     cur = self.db.cursor(pymysql.cursors.DictCursor)
    #     query_3 = "UPDATE " +table_name + " SET " + pk_name + "  = @COUNT:=@COUNT+1;"
    #     cur.execute(query_3)
    #     cur.close()

    def orm_test(self): # code_matching테이블에서 원본코드컬럼만 모두 출력하기
        Session = sessionmaker(bind=self.engine)
        session = Session()
        for row in session.query(code_matching):
            print(row.original_code)
        session.close()

    def init_autoincrement(self,table_name,pk_name):
        Session = sessionmaker(bind=self.engine,autocommit=True, autoflush=True)
        session = Session()
        
        session.execute("ALTER TABLE " + table_name +" AUTO_INCREMENT=1;")

        session.execute("SET @COUNT = 0;")

        session.execute("UPDATE " +table_name + " SET " + pk_name + "  = @COUNT:=@COUNT+1;")

        session.close()
        

    



    

class CreateTableIfNotExists(CreateTable):
    pass

@compiles(CreateTableIfNotExists)
def compile_create_table_if_not_exists(element, ddlcompiler, **kw):
    default_create_ddl = ddlcompiler.visit_create_table(element, **kw)
    default_create_ddl = default_create_ddl.lstrip()
    create_if_not_exists = re.sub(
        r"^CREATE TABLE ", "CREATE TABLE IF NOT EXISTS ", default_create_ddl, flags=re.IGNORECASE
    )
    return create_if_not_exists


