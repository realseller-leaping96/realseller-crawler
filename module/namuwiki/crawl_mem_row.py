import re

def crawl_mem_row(temp_dict, td):
    memory = td[1].text
    #temp_dict["메모리"] = memory
    
    memorry_arr = td[1].text.split(',')
    
    if len(memorry_arr) >= 1:
        temp_dict["시스템램"] = memorry_arr[0]
        
    if len(memorry_arr) >= 2:
        in_mem = ""
        if memorry_arr[1].find("GB") != -1:
            in_mem = re.search('(.*GB)',memorry_arr[1]).group()
        elif memorry_arr[1].find("MB") != -1:
            in_mem = re.search('(.*MB)',memorry_arr[1]).group()
        mem_dev = memorry_arr[1].replace(in_mem,"")
        temp_dict["내장메모리"] = in_mem.replace(" GB","")
        temp_dict["저장장치"] = mem_dev.replace(" 규격 내장 메모리","")
        
    if len(memorry_arr) >= 3:
        temp_dict["외장메모리"] = memorry_arr[2]

    # 여기도 고도화 필요
    

    return temp_dict