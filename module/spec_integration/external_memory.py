from module.spec_integration.replacer import replace_all

def find_external_memory(namu_row,danawa_row,cetizen_row):
    #external_memory
    external_memory = ""
    
    if len(namu_row) == 1 :
        if namu_row.iloc[0]['sn_external_memory'] is not None:
            external_memory = namu_row.iloc[0]['sn_external_memory']
    if len(danawa_row) == 1 and external_memory == "":
        if danawa_row.iloc[0]['sd_external_memory'] is not None:
            external_memory = danawa_row.iloc[0]['sd_external_memory'].replace("미지원",""
                                ).replace("Micro","micro").replace("micro"," micro "
                                ).replace(":","").replace("최대","최대 ").replace("GB"," GB"
                                ).replace("TB"," TB").replace("MB"," MB")
        if external_memory.find("최대")!=-1:
            external_memory += " 지원"
    if len(cetizen_row) == 1 and external_memory == "":
        if cetizen_row.iloc[0]['sc_external_memory'] is not None:
            external_memory = cetizen_row.iloc[0]['sc_external_memory'].replace("Micro","micro"
                            ).replace("micro"," micro ")
    external_memory = external_memory.strip()

    replace_dict = {"(규격상":"규격상","공식 지원)":""," TB":"TB"}
    return replace_all(external_memory,replace_dict)