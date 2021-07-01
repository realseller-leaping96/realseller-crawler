def find_usim_type(namu_row,danawa_row,cetizen_row):
    #usim_type
    usim_type = ""
    if len(cetizen_row) == 1 :
        if cetizen_row.iloc[0]['sc_usim_type'] is not None:
            usim_type = cetizen_row.iloc[0]['sc_usim_type']
    if len(danawa_row) == 1 and usim_type == "":
        if danawa_row.iloc[0]['sd_usim_type'] is not None:
            usim_type = danawa_row.iloc[0]['sd_usim_type']
    return usim_type