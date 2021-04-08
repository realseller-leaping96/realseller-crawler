def crawl_os_row(temp_dict, td): 
    operation_system = td[1].text
    temp_dict["운영체제"] = operation_system

    return temp_dict