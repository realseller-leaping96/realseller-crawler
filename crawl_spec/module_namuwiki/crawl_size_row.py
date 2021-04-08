import re

def crawl_size_row(temp_dict, td):
    if td[0].text == "규격" and td[1].text != "한국" and td[1].text != "UMTS"and td[1].text != "크기" and td[1].text != "싱글" and td[1].text != "기본" and "가로" not in temp_dict:
        size = td[1].text
        #temp_dict["규격"] = size
        xyz = re.search('[0-9.x ]+mm', size).group()
        if xyz.find("x") != -1:
            xyz = xyz.split("x")
            
        if len(xyz) > 2:
            temp_dict["가로"] = xyz[0]
            temp_dict["세로"] = xyz[1]
            temp_dict["두께"] = xyz[2]
        
        if size.find("g") != -1:
            temp_dict["무게"] = re.search('[0-9. ]+g', size).group()
        elif td[2].text.find("g"):
            temp_dict["무게"] = re.search('[0-9. ]+g', td[2].text).group()
        
    elif td[0].text == "규격" and td[1].text == "크기" and "가로" not in temp_dict:
        size = td[2].text
        xyz = re.search('[0-9.x ]+mm', size).group()
        if xyz.find("x") != -1:
            xyz = xyz.split("x")
            
        if len(xyz) > 2:
            temp_dict["가로"] = xyz[0]
            temp_dict["세로"] = xyz[1]
            temp_dict["두께"] = xyz[2]
    
    elif td[0].text == "규격" and td[1].text == "무게" and "무게" not in temp_dict:
        weight = td[2].text
        weight = re.search('[0-9. ]+g', weight).group()
        temp_dict["무게"] = weight
        
    elif td[0].text == "규격" and td[1].text == "싱글" and "무게" not in temp_dict:
        size = td[2].text
        xyz = re.search('[0-9.x ]+mm', size).group()
        if xyz.find("x") != -1:
            xyz = xyz.split("x")
            
        if len(xyz) > 2:
            temp_dict["가로"] = xyz[0]
            temp_dict["세로"] = xyz[1]
            temp_dict["두께"] = xyz[2]
        
        weight = td[3].text
        weight = re.search('[0-9. ]+g', weight).group()
        temp_dict["무게"] = weight
        
        
        
        
    elif td[0].text == "규격" and td[1].text == "기본" and "가로" not in temp_dict:
        size = td[2].text
        #temp_dict["규격"] = size
        xyz = re.search('[0-9.x ]+mm', size).group()
        if xyz.find("x") != -1:
            xyz = xyz.split("x")
            
        if len(xyz) > 2:
            temp_dict["가로"] = xyz[0]
            temp_dict["세로"] = xyz[1]
            temp_dict["두께"] = xyz[2]
            
        if size.find("g") != -1:
            temp_dict["무게"] = re.search('[0-9. ]+g', size).group()
        elif td[3].text.find("g") != -1:
            temp_dict["무게"] = re.search('[0-9. ]+g', td[3].text).group()
            
    elif td[0].text == "규격" and (td[1].text == "UMST" or td[1].text == "한국" ) and "가로" not in temp_dict:
        size = td[2].text
        #temp_dict["규격"] = size
        xyz = re.search('[0-9.x ]+mm', size).group()
        if xyz.find("x") != -1:
            xyz = xyz.split("x")
            
        if len(xyz) > 2:
            temp_dict["가로"] = xyz[0]
            temp_dict["세로"] = xyz[1]
            temp_dict["두께"] = xyz[2]
            
        if size.find("g") != -1:
            temp_dict["무게"] = re.search('[0-9. ]+g', size).group()
        elif td[3].text.find("g") != -1:
            temp_dict["무게"] = re.search('[0-9. ]+g', td[3].text).group()
            
    return temp_dict
                    
            