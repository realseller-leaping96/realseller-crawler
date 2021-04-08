import re

def crawl_disp_row(temp_dict, td) :
    display = td[1].text
    #temp_dict["디스플레이"] = display
    if display.find("세부 정보 확인")!= -1:
        display_part1 = re.search('.*\[ 세부 정보 확인 \]', display).group().replace("[ 세부 정보 확인 ]","")
        
        temp_dict["화면크기(인치)"] = display_part1
        temp_dict["화면크기(인치)"] = re.search('([0-9.]+인치)', display_part1).group() 



        temp_dict["화면비"] = re.search('[0-9.]+:[0-9.]+(\+[0-9.?]+:[0-9.?]+)? 비율', display_part1).group().replace(" 비율","")
        temp_dict["화면해상도"] = re.search('([0-9]+ x [0-9]+)', display_part1).group() 
        temp_dict["ppi"] = re.sub('[\(\)]','',re.search('\([0-9.-]+ ppi\)|\([0-9]+ppi\)',"".join(display_part1)).group())

        disp_table = td[1].select(".wiki-table-wrap > table")
        disp_trs = disp_table[0].select("tr")


        for disp_tr in disp_trs:
            disp_td = disp_tr.select("td")

            if disp_td[0].text == "패널정보":
                temp_dict["패널종류"] = disp_td[1].text

            elif disp_td[0].text == "부가정보":
                plus_info = disp_td[1].text
                if plus_info.find("Hz") != -1:
                    temp_dict["최대주사율"] = re.search('([0-9]+ Hz)|([0-9]+Hz)', plus_info).group()
                
    else:
        #세부정보확인 버튼이 없는경우 따로구현할것
        pass

    return temp_dict