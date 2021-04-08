import re

def crawl_battery_row(temp_dict,td):
    battery = td[1].text
    #temp_dict["배터리"] = battery

    if battery.find("[ 충전 기술 정보") != -1:
        bat_part1 = re.search('.*\[ 충전 기술 정보', battery).group().replace("[ 충전 기술 정보","")
        storage = re.search('[0-9 .,]+mAh', bat_part1).group()
        temp_dict["배터리용량"] = storage
        temp_dict["배터리타입"] = bat_part1.replace(storage,"")
    else:
        pass
        
    if td[1].select(".wiki-table-wrap > table"):

            in_table = td[1].select(".wiki-table-wrap > table")
            in_trs = in_table[0].select("tr")

            for tr in in_trs:
                td = tr.select("td")
                if td[0].text == "유선고속충전":
                    temp_dict["배터리특징"] = td[1].text

    return temp_dict