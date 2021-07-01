def find_battery(namu_row,danawa_row,cetizen_row):
    #battery
    battery = ""
    if len(cetizen_row) == 1 :
        if cetizen_row.iloc[0]['sc_battery'] is not None:
            battery = cetizen_row.iloc[0]['sc_battery']
    if len(danawa_row) == 1 and battery == "":
        if danawa_row.iloc[0]['sd_battery'] is not None:
            if danawa_row.iloc[0]['sd_battery'].find("~") == -1:
                battery = danawa_row.iloc[0]['sd_battery']
                
    if len(namu_row) == 1 and battery == "":
        if namu_row.iloc[0]['sn_battery'] is not None:
            battery = namu_row.iloc[0]['sn_battery']
    return battery