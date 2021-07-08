from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

class Database:
    def __init__(self):
        self.db_conn = pymysql.connect(host='localhost', user='root', password='123123', db='gidseller')
        self.cursor = self.db_conn.cursor()

        self.engine = create_engine("mysql+mysqldb://root:"+"123123"+"@localhost/gidseller", encoding='utf-8')
        self.engine_conn = self.engine.connect()