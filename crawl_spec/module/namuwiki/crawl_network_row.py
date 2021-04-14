def crawl_network_row(temp_dict, td):   
    network = td[1].text
    #temp_dict["네트워크"] = network
    if network.find("5G") != -1:
        temp_dict["5G"] = "5G"
    if network.find("4G") != -1:
        temp_dict["4G"] = "4G"

    return temp_dict