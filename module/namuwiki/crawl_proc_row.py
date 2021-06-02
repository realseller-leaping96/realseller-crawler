import re

def crawl_proc_row(temp_dict, td): 
    processor = td[1].text
    #temp_dict["프로세서"] = processor
    next_is_core_clock = -1
    if processor.find("구성 내용 확인") != -1:
        temp_dict["AP종류"] = re.search('.*\[ 구성 내용 확인 \]', processor).group().replace("[ 구성 내용 확인 ]","")
    
        proc_table = td[1].select(".wiki-table-wrap > table")
        proc_trs = proc_table[0].select("tr")

        for proc_tr in proc_trs:
            proc_td = proc_tr.select("td")

            if proc_td[0].text == "CPU":
                if proc_td[1].text.find("Hz") != -1:
                    temp_dict["코어클럭"] = proc_td[1].text
                    next_is_core_clock = -1
                else:
                    next_is_core_clock = 1

            elif next_is_core_clock == 1:
                temp_dict["코어클럭"] = proc_td[0].text
                next_is_core_clock = -1

            elif proc_td[0].text == "GPU":
                temp_dict["그래픽코어"] = proc_td[1].text

            elif proc_td[0].text == "NPU & DSP":
                temp_dict["NPU & DSP"] = proc_td[1].text

            elif proc_td[0].text == "Sensor Hub":
                temp_dict["Sensor Hub"] = proc_td[1].text

            elif proc_td[0].text == "통신 모뎀":
                temp_dict["통신모뎀"] = proc_td[1].text
    else:
        #[구성내용 확인] 버튼이 없는경우 따로구현할것 
        if processor.find("SoC") != -1 or processor.find("Platform") != -1: 
            temp_dict["AP종류"] = re.search('.*(SoC|Platform)', processor).group()

        if processor.find("CPU") != -1:
            temp_dict["코어클럭"] = re.search('([a-zA-Z0-9 -]+[0-9. ]+(G|M)Hz)([ +a-zA-Z0-9 -]+[0-9. ]+(G|M)Hz)? CPU', processor).group()
            # temp_dict["코어클럭"] = re.search('[0-9.]+ GHz', processor).group()

        if processor.find("GPU") != -1:
            if temp_dict["AP종류"] != -1 and temp_dict["코어클럭"] != -1:
                temp_dict["그래픽코어"] = processor.replace(temp_dict["AP종류"],"").replace(temp_dict["코어클럭"],"")


    return temp_dict