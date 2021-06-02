import re

def crawl_os_row(temp_dict, td): 
    operation_system = td[1].text

    # if operation_system.find("→") != -1 and operation_system.find("iOS") != -1:
    #     version = re.search('([0-9→ .]+)',operation_system).group()
    #     operation_system = operation_system.replace(version,"")
    #     version = version.split("→")[-1]
    #     operation_system += version

    # elif operation_system.find("→") != -1 and operation_system.find("안드로이드") != -1:
    #     version = re.search('([0-9→ .()a-zA-Z]+)',operation_system).group()
    #     operation_system = operation_system.replace(version,"")
    #     version = version.split("→")[-1]
    #     operation_system += version


    
    temp_dict["운영체제"] = operation_system.replace("→","|")

    return temp_dict