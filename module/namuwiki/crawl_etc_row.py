def crawl_etc_row(temp_dict, td):
    etc = td[1].text
    temp_dict["기타"] = etc

    return temp_dict