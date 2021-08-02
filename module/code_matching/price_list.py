import regex
from module.code_matching.utility import aka_table as aka_table

def match_price_list(db_model,phone_list):
    price_list = db_model.get_table_dataframe("price_list")
    price_list.insert(5,"pattern",None,True)
    pattern_list = []
    storage_list = []
    for i,row in price_list.iterrows():
        price__row = row.copy()
        #모델코드 매칭부분

        is_aka_matched = 0
        aka_value = ""
        for i in range(len(aka_table["price_list"])):
            if row[aka_table["price_list"][i]["column"]] is not None:
                if (row[aka_table["price_list"][i]["column"]].lower().replace(" ",""))\
                    .find(aka_table["price_list"][i]["key"].lower().replace(" ",""))!=-1:
                    aka_value = aka_table["price_list"][i]["value"]
                    is_aka_matched = 1
        
        if is_aka_matched == 1:
            pattern_list.append(aka_value)
     
        elif row['model_code'] is not None :
            pattern_list.append(regex.sub("(?<=[0-9]+)[a-zA-Z]+","",row['model_code']))

        else:
            pattern_list.append(None)
                
        #용량
        if pattern_list[-1] == "SM-B510":
            storage_list.append("0.25")
        elif pattern_list[-1] in list(phone_list['pl_model_code']):
            guess_single = "".join(list(phone_list[phone_list['pl_model_code'] == pattern_list[-1]]['pl_storage'])).split("|")
            if len(guess_single) == 1:
                storage_list.append(guess_single[0])
            elif price__row['storage'] is not None:
                storage_list.append(price__row['storage'].replace("GB","").replace("TB","").\
                replace("G","").replace("T",""))
            else:
                storage_list.append(None)
        elif price__row['storage'] is not None:
            storage_list.append(price__row['storage'].replace("GB","").replace("TB","").\
                replace("G","").replace("T",""))
        else:
            storage_list.append(None)

            
    price_list["pattern"] = pattern_list
    price_list["storage"] = storage_list

    return price_list