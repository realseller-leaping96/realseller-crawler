from module.db.db_model import DbModel
from module.code_matching.mintit import match_mintit_index
from module.code_matching.joongabi import match_joongabi_index
from module.code_matching.bunjang import match_bunjang_index
from module.code_matching.price_list import match_price_list
from module.code_matching.merge import merge_index

from sqlalchemy import Table, Column, Integer, String, Boolean, Date
from module.db.db_model import CreateTableIfNotExists

db_model = DbModel("main") #code_matching 테이블 없을경우 정의해줌

phone_list = db_model.get_table_dataframe("g5_phone_list")

mintit_index = match_mintit_index(db_model,phone_list)

joongabi_index = match_joongabi_index(db_model,phone_list)

bunjang_index = match_bunjang_index(db_model,phone_list)

price_list = match_price_list(db_model,phone_list)

result= merge_index(bunjang_index,joongabi_index,mintit_index,price_list,phone_list)

db_model.update_code_matching(result)

db_model.init_autoincrement("code_matching","id")

db_model.end()



