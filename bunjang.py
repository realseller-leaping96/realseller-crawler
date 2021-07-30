import re
from utility import xstr as xstr
from utility import aka_table as aka_table

def match_bunjang_index(db_model,phone_list):
    bunjang_index = db_model.get_table_dataframe("bunjang_index")
    bunjang_index.insert(5,"pattern",None,True)
    pattern_list = []
    for i,row in bunjang_index.iterrows():
        bunjang__row = row.copy()
        #모델코드 매칭부분
        is_aka_matched = 0
        aka_value = ""
        for i in range(len(aka_table["bunjang"])):
            if (row[aka_table["bunjang"][i]["column"]].lower().replace(" ",""))\
            .find(aka_table["bunjang"][i]["key"].lower().replace(" ",""))!=-1:
                print(aka_table["bunjang"][i]["column"],\
                aka_table["bunjang"][i]["key"],\
                aka_table["bunjang"][i]["value"])
                aka_value = aka_table["bunjang"][i]["value"]
                is_aka_matched = 1
        
        if is_aka_matched == 1:
            pattern_list.append(aka_value)
        
        elif row['bj_code'][0] == "S":
            pattern_list.append(re.search("S(M|HW|HV)-[a-zA-Z][0-9]+",row['bj_code']).group())
        elif row['bj_code'][0] == "L":
            pattern_list.append(re.search("L(GM|M|G)-[a-zA-Z]+[0-9]+",row['bj_code']).group())
        elif row['bj_code'][0:2] == "iP":
            
            is_apple_find = 0
            apple_model_code = ""
            for i, row in phone_list.iterrows():
                bunjang_name = bunjang__row['name']
                bunjang_name = bunjang_name.replace("플러스","Plus").replace("+","Plus")
                if bunjang_name.lower().replace(" ","")==row['pl_name'].lower().replace(" ",""):
                    is_apple_find = 1
                    apple_model_code = row['pl_model_code']
            if is_apple_find == 1:
                pattern_list.append(apple_model_code)
            else:
                pattern_list.append("애플기타")
                
        else:
            pattern_list.append(None)
                
        #용량 => 이미되어있음
            
    bunjang_index["pattern"] = pattern_list

    return bunjang_index