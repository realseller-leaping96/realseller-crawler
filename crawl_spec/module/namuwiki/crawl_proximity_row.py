import re

def crawl_proximity_row(temp_dict, td):
    proximity = td[1].text
    #temp_dict["근접통신"] = proximity
    
    if proximity.find("블루투스") != -1:
        temp_dict["블루투스"] = re.sub('(블루투스|,)',"",re.search('(블루투스 [0-9.]+)', proximity).group())
    
    return temp_dict