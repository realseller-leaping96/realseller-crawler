def find_bluetooth(namu_row,danawa_row,cetizen_row):
    #bluetooth
    bluetooth = ""
    
    if len(cetizen_row) == 1 :
        if cetizen_row.iloc[0]['sc_bluetooth'] is not None:
            bluetooth = cetizen_row.iloc[0]['sc_bluetooth']
    if len(danawa_row) == 1 and bluetooth == "":
        if danawa_row.iloc[0]['sd_bluetooth'] is not None:
            bluetooth = danawa_row.iloc[0]['sd_bluetooth'].replace("v","").replace(".0","")
    if len(namu_row) == 1 and bluetooth == "":
        if namu_row.iloc[0]['sn_bluetooth'] is not None:
            bluetooth = namu_row.iloc[0]['sn_bluetooth']
    return bluetooth