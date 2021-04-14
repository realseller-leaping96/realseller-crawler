def crawl_satlite_row(temp_dict, td):
    satelite = td[1].text
    temp_dict["위성항법"] = satelite

    return temp_dict