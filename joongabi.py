import re
from utility import xstr as xstr
from utility import aka_table as aka_table

def match_joongabi_index(db_model,phone_list):
    joongabi_index = db_model.get_table_dataframe("joongabi_index")
    joongabi_index.insert(6,"pattern",None,True)
    joongabi_index.insert(7,"storage",None,True)
    pattern_list = []
    storage_list = []
    for i,row in joongabi_index.iterrows():
        joongabi_row = row.copy()
        
        #모델코드 매칭부분
        if row['brand_name'] == "apple":
            
            is_apple_find = 0
            apple_model_code = ""
            for i, row in phone_list.iterrows():
                joongabi_name = re.sub(' [0-9]+G(B)?(_리퍼)?','',joongabi_row['model_name'])
                joongabi_name = joongabi_name.replace("플러스","Plus").replace("+","Plus")
                if joongabi_name.lower().replace(" ","")==row['pl_name'].lower().replace(" ",""):
                    is_apple_find = 1
                    apple_model_code = row['pl_model_code']
                    
            if is_apple_find == 1:
                pattern_list.append(apple_model_code)
                
            else:
                is_apple_find = 0
                apple_model_code = ""
                joongabi_key = ""
                for i, row in phone_list.iterrows():
                    joongabi_key = re.search('(?<=AIP)([0-9]+(PM|Plus|M|S|C)?( )?(Plus|P)?( )?|X(R|S)?( )?(MAX|M)?|( )?SE([0-9]+)?)',\
                                            joongabi_row['model_code']).group()
                    
                    if joongabi_key.find("PM")!=-1:
                        joongabi_key = joongabi_key.replace("PM","PRO MAX")
                    elif joongabi_key.find("MAX")!=-1:
                        pass
                    elif joongabi_key.find("Plus")!=-1:
                        pass
                    elif joongabi_key.find("P")!=-1:
                        joongabi_key = joongabi_key.replace("P","Plus")
                    elif joongabi_key.find("M")!=-1:
                        joongabi_key = joongabi_key.replace("M","MINI")
                    
                    
                    if joongabi_key.lower().replace(" ","")==(xstr(row['pl_info_version']) + xstr(row['pl_info_subname_1']) +\
                                                            xstr(row['pl_info_subname_2'])).lower().replace(" ",""):
                        is_apple_find = 1
                        apple_model_code = row['pl_model_code']
                
                if is_apple_find == 1:
                    pattern_list.append(apple_model_code)
                else:
                    pattern_list.append("애플기타")
            
        elif row['brand_name'] == "samsung":
            pattern_list.append(re.search("S(M|HW|HV)-[a-zA-Z][0-9]+",row['model_code']).group())
        elif row['brand_name'] == "lg":
            pattern_list.append(re.search("L(GM|M|G)-[a-zA-Z]+[0-9]+",row['model_code']).group())
        else:
            pattern_list.append(None)
            
        #용량부분
        if re.search("(?<=-)[0-9]+(G|T)",joongabi_row['model_code']) is not None:
            storage_list.append(re.search("(?<=-)[0-9]+(G|T)",joongabi_row['model_code']).group())
            
        elif re.search("(?<=_)[0-9]+(G|T)",joongabi_row['model_code']) is not None:
            storage_list.append(re.search("(?<=_)[0-9]+(G|T)",joongabi_row['model_code']).group())
            
        elif re.search("(?<= )[0-9]+(G|T)(B)?",joongabi_row['model_name']) is not None:
            storage_list.append(re.search("(?<= )[0-9]+(G|T)(B)?",joongabi_row['model_name']).group())
        
        #단일용량 기종 거르는 부분
        elif pattern_list[-1] in list(phone_list['pl_model_code']):
            guess_single = "".join(list(phone_list[phone_list['pl_model_code'] == pattern_list[-1]]['pl_storage'])).split("|")
            if len(guess_single) == 1:
                storage_list.append(guess_single[0])
            else:
                storage_list.append(None)
        else:
            storage_list.append(None)
        
    joongabi_index["pattern"] = pattern_list
    for i in range(len(storage_list)):
        if storage_list[i] and storage_list[i].find("G")!=-1:
            storage_list[i] = storage_list[i].replace("GB","").replace("G","")
        elif storage_list[i] and storage_list[i].find("T")!=-1:
            storage_list[i] = int(storage_list[i].replace("TB","").replace("T",""))*1024
    joongabi_index["storage"] = storage_list

    return joongabi_index