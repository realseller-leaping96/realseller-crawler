from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
engine = create_engine('mysql+mysqldb://root:123123@localhost/gidseller')
print(engine.execute("desc price_list").fetchone()) # test 테이블의 schema를 출력

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine) # Engine에 종속적인 Session을 정의하고
session = Session() # Session 객체를 만든다

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

import datetime
from sqlalchemy import Column, Integer, String, DateTime
class User(Base):
    __tablename__ = 'orm_test_table'
    a = Column(Integer)
    b = Column(Integer)
    c = Column(String(50))
    time = Column(DateTime, default=datetime.datetime.utcnow, primary_key=True)
    def __init__(self, a, b,c):
        self.a = a
        self.b = b
        self.c = c

# Base.metadata.create_all(engine) # Base에 연결된 모든 테이블을 DB에 생성한다.
Base.metadata.tables['orm_test_table'].create(bind = engine) # Base에 연결된 TEST_TB 테이블을 DB에 생성한다.
# Base.metadata.drop_all(engine) # Base에 연결된 모든 테이블을 DB에서 제거한다.
# Base.metadata.tables['TEST_TB'].drop(bind = engine) # Base에 연결된 TEST_TB 테이블을 DB에서 제거한다.


user = User(1,2,"오예~~~오알엠")
session.add(user)
session.commit()


# CustomTable.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
class CustomTable(Base):
    __tablename__ = 'CUSTOM_TB'
    a = Column(Integer, primary_key=True, autoincrement=True)
    b = Column(Integer)
    time = Column(DateTime, default=datetime.utcnow, primary_key=True)
    def __init__(self, b):
        self.b = b