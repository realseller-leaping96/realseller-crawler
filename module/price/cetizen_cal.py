from bs4 import BeautifulSoup
import pandas as pd

def parse_by_telecom_maker(telecom,maker,crawl_data,driver,my_dict):
    my_dict["통신사"] = telecom
    if telecom == "SKT":
        telecom = "1"
    elif telecom == "KT":
        telecom = "2"
    elif telecom == "LG":
        telecom = "3"

    if maker == "삼성전자":
        maker = "1"
    if maker == "애플":
        maker = "12"
    if maker == "LG전자":
        maker = "2"
    
    driver.get('https://fee.cetizen.com/index.php?corp='+telecom+'&maker='+maker) 

    req = driver.page_source
    soup=BeautifulSoup(req, 'html.parser')

    table = soup.select("body > div.container.custom-container > div:nth-child(22) > div > div.col-lg-4.col-md-3.border > div.pt-1.row.no-gutters")

    rows = table[0].select(".col-lg-12.col-md-12.col-sm-12.col-12")

    for r in rows:
        name_code = r.select("span")
        name1 = ""
        for nc in range(len(name_code)-1):
            name1 += name_code[nc].text
        code1 = name_code[-1].text
        price = r.select(".col-lg-3.col-md-0.col-sm-3.col-3.text-right.p13.d-md-none.d-lg-block.clr14.pr-2.no-gutters")
        price1 = price[0].text
        #print(name1, code1, price1)
        my_dict["모델명"] = name1
        my_dict["모델코드"] = code1
        my_dict["가격"] = price1
        crawl_data = crawl_data.append(pd.DataFrame(my_dict,index=[0]))
    
    return crawl_data