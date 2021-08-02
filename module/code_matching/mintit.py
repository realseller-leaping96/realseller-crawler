import re
from module.code_matching.utility import xstr as xstr
from module.code_matching.utility import aka_table as aka_table

def match_mintit_index(db_model,phone_list):
    mintit_index = db_model.get_table_dataframe("mintit_index")
    mintit_index.insert(8,"pattern",None,True)
    mintit_index.insert(9,"storage",None,True)
    pattern_list = []
    storage_list = []

    for i, row in mintit_index.iterrows():
        mintit_row = row.copy()
        
        #모델코드 패턴매칭부분
        
        is_aka_matched = 0
        aka_value = ""
        for i in range(len(aka_table["mintit"])):
            if (row[aka_table["mintit"][i]["column"]].lower().replace(" ",""))\
            .find(aka_table["mintit"][i]["key"].lower().replace(" ",""))!=-1:
                aka_value = aka_table["mintit"][i]["value"]
                is_aka_matched = 1
        
        if is_aka_matched == 1:
            pattern_list.append(aka_value)
        elif row['brand_name'] == '삼성전자':
            pattern_list.append(re.search("S(M|HW|HV)-[a-zA-Z][0-9]+",row['mintit_key']).group())
            
        elif row['brand_name'] == 'LG전자' :
            if re.search("L(GM|M|G)-[a-zA-Z]+[0-9]+",row['mintit_key']) is not None:
                pattern_list.append(re.search("L(GM|M|G)-[a-zA-Z]+[0-9]+",row['mintit_key']).group())
            else:
                pattern_list.append("엘지기타")
            
        elif row['brand_name'] == '애플':
            
            is_apple_find = 0
            apple_model_code = ""
            for i, row in phone_list.iterrows():
                mintit_name = re.sub(' [0-9]+G','',mintit_row['model_name'])
                
                if mintit_name.lower().replace(" ","")==row['pl_name'].lower().replace(" ",""):
                    is_apple_find = 1
                    apple_model_code = row['pl_model_code']
            if is_apple_find == 1:
                pattern_list.append(apple_model_code)
                
            else:
                
                is_apple_find = 0
                apple_model_code = ""
                mintit_key = ""
                for i, row in phone_list.iterrows():
                    mintit_key = re.search('(?<=AIP)([0-9]+( )?(PRO( MAX)?|PM|Plus|MINI|S|C)?( )?(Plus|P)?( )?|X(R|S)?( )?(MAX|M)\
                                            ?|( )?SE)',mintit_row['mintit_key']).group()
                    
                    
                    if mintit_key.lower().replace(" ","")==(xstr(row['pl_info_version']) + xstr(row['pl_info_subname_1']) +\
                                                            xstr(row['pl_info_subname_2'])).lower().replace(" ","")\
                    and row['pl_info_model'] == "iphone":
                        is_apple_find = 1
                        apple_model_code = row['pl_model_code']
                
                if is_apple_find == 1:
                    pattern_list.append(apple_model_code)
                else:
                    pattern_list.append("애플기타")
                
        else:
            pattern_list.append(None)
            
            
        #용량부분
        if re.search("(?<=-)[0-9]+(G|T)",mintit_row['mintit_key']\
            .replace(" 5G","").replace(" 4G","").replace(" 3G","")) is not None:
            storage_list.append(re.search("(?<=-)[0-9]+(G|T)",mintit_row['mintit_key']\
                .replace(" 5G","").replace(" 4G","").replace(" 3G","")).group())

        elif re.search("(?<= )[0-9]+(G|T)",mintit_row['mintit_key']\
            .replace(" 5G","").replace(" 4G","").replace(" 3G","")) is not None:
            storage_list.append(re.search("(?<= )[0-9]+(G|T)",mintit_row['mintit_key']\
                .replace(" 5G","").replace(" 4G","").replace(" 3G","")).group())
            
        elif pattern_list[-1] in list(phone_list['pl_model_code']):
            guess_single = "".join(list(phone_list[phone_list['pl_model_code'] == pattern_list[-1]]['pl_storage'])).split("|")
            if len(guess_single) == 1:
                storage_list.append(guess_single[0])
            else:
                storage_list.append(None)
        
        else:
            storage_list.append(None)
            
    mintit_index["pattern"] = pattern_list
    for i in range(len(storage_list)):
        if storage_list[i] and storage_list[i].find("G")!=-1:
            storage_list[i] = storage_list[i].replace("G","")
        elif storage_list[i] and storage_list[i].find("T")!=-1:
            storage_list[i] = int(storage_list[i].replace("T",""))*1024
    mintit_index["storage"] = storage_list

    return mintit_index