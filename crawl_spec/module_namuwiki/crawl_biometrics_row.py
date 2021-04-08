def crawl_biometrics_row(temp_dict,td):
    biometrics = td[1].text
    temp_dict["생체인식"] = biometrics

    return temp_dict