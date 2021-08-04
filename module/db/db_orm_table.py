
from sqlalchemy import Column, SMALLINT, BIGINT, String,Integer, engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#코드매칭 테이블
class code_matching(Base): # 식별하기 쉽게 테이블명으로 지정 
    __tablename__= 'code_matching'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    original_code = Column("original_code", String(50))
    storage = Column("storage", String(100))
    mintit_code = Column("mintit_code", String(100))
    bunjang_code = Column("bunjang_code", String(100))
    joongabi_code = Column("joongabi_code", String(100))
    price_code = Column("price_code", String(100))

    def __init__(self, original_code,storage,mintit_code,bunjang_code,joongabi_code,price_code): 
        self.original_code = original_code
        self.storage = storage 
        self.mintit_code = mintit_code 
        self.bunjang_code = bunjang_code
        self.joongabi_code = joongabi_code
        self.price_code = price_code

    def __repr__(self): 
        return "<code_matching('%d', '%s', '%s', '%s', '%s', '%s', '%s')>" \
            % (self.id,self.original_code, self.storage, self.mintit_code, \
                self.bunjang_code, self.joongabi_code,self.price_code)


###또다른 테이블
#
#
# ...






