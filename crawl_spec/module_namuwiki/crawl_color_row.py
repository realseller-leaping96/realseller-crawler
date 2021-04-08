def crawl_color_row(temp_dict, td) :
    color = td[1].text
    temp_dict["색상"] = color

    return temp_dict