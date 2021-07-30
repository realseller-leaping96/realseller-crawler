from db_model import DbModel
import pandas as pd
import numpy as np
import re
import regex
from pprint import pprint
from mintit import match_mintit_index
from joongabi import match_joongabi_index
from bunjang import match_bunjang_index

db_model = DbModel("main")

phone_list = db_model.get_table_dataframe("g5_phone_list")

mintit_index = match_mintit_index(db_model,phone_list)

# pprint(mintit_index.head(5))

joongabi_index = match_joongabi_index(db_model,phone_list)

# pprint(joongabi_index.head(5))

bunjang_index = match_bunjang_index(db_model,phone_list)

# pprint(bunjang_index.head(5))

db_model.end()

join_keys = ['pattern','storage'] #모델명으로 데이터 조인
b_merge = bunjang_index.drop('id',axis=1).astype({'storage': 'float'})
j_merge = joongabi_index.drop('id',axis=1).fillna(0).astype({'storage': 'float'})
m_merge = mintit_index.fillna(0).astype({'storage': 'float'})
df_OUTER_JOIN = pd.merge(b_merge, j_merge, left_on=join_keys, right_on=join_keys, how='outer')
df_OUTER_JOIN = pd.merge(df_OUTER_JOIN,m_merge, left_on=join_keys, right_on=join_keys, how='outer')
# display(df_OUTER_JOIN)
result = df_OUTER_JOIN.drop(['name','brand_id_x','brand_name_x','model_id_x','model_name_x','id','generation','retail_price',
                            'brand_id_y','brand_name_y','model_id_y','model_name_y'],axis=1)
result = result[['pattern', 'storage', 'key','model_code','mintit_key']]
result = result.fillna(0)
result = result.astype({'storage': 'int'})
result = result.rename(columns={'key':'번장키','model_code':'중가비키','mintit_key':'민팃키'})
result = result.replace(0,np.NAN).drop_duplicates()
# display(result)
result_for_join = result.rename(columns={'pattern':'pl_model_code'})
result_for_join = pd.merge(result_for_join,phone_list, left_on='pl_model_code', right_on='pl_model_code', how='inner')
# display(result_for_join[['pl_id','pl_model_name','pl_model_code','storage' ,'번장키', '중가비키','민팃키']].replace(0,np.NaN))
result_for_join = result_for_join[['pl_model_code','storage' ,'번장키', '중가비키','민팃키']].replace(0,np.NaN)
result_for_join.columns = ['original_code', 'price_code', 'mintit_code','bunjang_code','joongabi_code']