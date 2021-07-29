import module.db_module as db_module
db_class = db_module.Database() #db연결 생성
import pandas as pd
import numpy as np
import re
import regex

## 민팃부분
mintit_index = pd.read_sql_table('mintit_index',db_class.engine_conn)
mintit_index.insert(8,"pattern",None,True)

pattern_list = []
for i, row in mintit_index.iterrows():
    
    if row['brand_name'] == '삼성전자':
        pattern_list.append(re.search("S(M|HW|HV)-[a-zA-Z][0-9]+",row['mintit_key']).group())
        
    elif row['brand_name'] == 'LG전자' :
        if re.search("L(GM|M|G)-[a-zA-Z]+[0-9]+",row['mintit_key']):
            pattern_list.append(re.search("L(GM|M|G)-[a-zA-Z]+[0-9]+",row['mintit_key']).group())
        else:
            pattern_list.append("엘지기타")
        
    elif row['brand_name'] == '애플':
        pattern_list.append("애플")
    else:
        pattern_list.append()
mintit_index["pattern"] = pattern_list


# 출고가크롤러부분
price_index = pd.read_sql_table('price_list',db_class.engine_conn)
price_index.insert(5,"pattern",None,True)
pattern_list = []
for i, row in price_index.iterrows():
    text = ""
    if row['model_code'] != None :
        text = regex.sub("(?<=[0-9]+)[a-zA-Z]+.*","",row['model_code'])
    if len(text) < 3:
        text = None
    pattern_list.append(text)
price_index["pattern"] = pattern_list

## 중가비 부분
joongabi_index = pd.read_sql_table('joongabi_index',db_class.engine_conn)
joongabi_index.insert(6,"pattern",None,True)
pattern_list = []
for i,row in joongabi_index.iterrows():
    if row['brand_name'] == "apple":
        pattern_list.append("애플")
    elif row['brand_name'] == "samsung":
        pattern_list.append(re.search("S(M|HW|HV)-[a-zA-Z][0-9]+",row['model_code']).group())
    elif row['brand_name'] == "lg":
        pattern_list.append(re.search("L(GM|M|G)-[a-zA-Z]+[0-9]+",row['model_code']).group())
joongabi_index["pattern"] = pattern_list

##번장부분
bunjang_index = pd.read_sql_table('bunjang_index',db_class.engine_conn)
bunjang_index.insert(5,"pattern",None,True)
pattern_list = []
for i,row in bunjang_index.iterrows():
    if row['bj_code'][0] == "S":
        pattern_list.append(re.search("S(M|HW|HV)-[a-zA-Z][0-9]+",row['bj_code']).group())
    elif row['bj_code'][0] == "L":
        pattern_list.append(re.search("L(GM|M|G)-[a-zA-Z]+[0-9]+",row['bj_code']).group())
    elif row['bj_code'][0:2] == "iP":
        pattern_list.append("애플")
bunjang_index["pattern"] = pattern_list