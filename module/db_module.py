from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import re
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.schema import CreateTable
from sqlalchemy import MetaData


class Database:
    def __init__(self):
        self.db_conn = pymysql.connect(host='localhost', user='root', password='123123', db='gidseller')
        self.cursor = self.db_conn.cursor()

        self.engine = create_engine("mysql+mysqldb://root:"+"123123"+"@localhost/gidseller", encoding='utf-8')
        self.engine_conn = self.engine.connect()
        
        self.metadata = MetaData()
        

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