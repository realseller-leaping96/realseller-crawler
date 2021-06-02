import re

def crawl_disp_row(temp_dict, td) :
    display = td[1].text
    if display.find("세부 정보 확인")!= -1:
        display_part1 = re.search('.*\[ 세부 정보 확인 \]', display).group().replace("[ 세부 정보 확인 ]","")
        
        temp_dict["화면크기(인치)"] = re.search('([0-9.]+인치)', display_part1).group().replace("인치","")

        if display_part1.find("비율")!=-1:
            temp_dict["화면비"] = re.search('[0-9.]+:[0-9.]+(\+[0-9.?]+:[0-9.?]+)?( )?비율', display_part1).group().replace(" 비율","")
        
        temp_dict["화면해상도"] = re.findall('([0-9]+ (x|X) [0-9]+)', display_part1)[-1][0]
        temp_dict["ppi"] = re.sub('[\(\)]','',re.search('\([0-9.-]+ ppi\)|\([0-9]+ppi\)',"".join(display_part1)).group()).replace(" ","").replace("ppi","")

        disp_table = td[1].select(".wiki-table-wrap > table")
        disp_trs = disp_table[0].select("tr")

        for disp_tr in disp_trs:
            disp_td = disp_tr.select("td")

            if disp_td[0].text == "패널정보":
                temp_dict["패널종류"] = disp_td[1].text

            elif disp_td[0].text == "부가정보":
                plus_info = disp_td[1].text
                if plus_info.find("Hz") != -1:
                    temp_dict["최대주사율"] = re.search('([0-9]+ Hz)|([0-9]+Hz)', plus_info).group().replace(" ","")
                
    else:
        #세부정보확인 버튼이 없는경우 따로구현할것
        
        if display.find("ppi") != -1 and display.find("&") != -1:
            
            ppi_panel = re.search('\([a-zA-Z -]+방식 &.*ppi\)', display).group()
            
            ppi = re.search('[0-9. ]+ppi',ppi_panel).group()
            panel = re.search('\(.* &',ppi_panel).group()
            
            temp_dict["패널종류"] = panel.replace("(","").replace("&","").replace("방식","")
            temp_dict["ppi"] = ppi.replace(" ","").replace("ppi","")
            
        if display.find("인치") != -1:
            temp_dict["화면크기(인치)"] = re.search('([0-9.]+인치)', display).group().replace("인치","")
        
        if display.find("x") != -1:
            temp_dict["화면해상도"] = re.findall('([0-9]+ (x|X) [0-9]+)', display)[-1][0]
        
        if display.find("Hz") != -1:
            temp_dict["최대주사율"] = re.search('([0-9]+ Hz)|([0-9]+Hz)', display).group().replace(" ","")

        if display.find("비율") != -1:
            temp_dict["화면비"] = re.search('[0-9.]+:[0-9.]+(\+[0-9.?]+:[0-9.?]+)?( )?비율', display).group().replace(" 비율","")
        

        pass

    return temp_dict