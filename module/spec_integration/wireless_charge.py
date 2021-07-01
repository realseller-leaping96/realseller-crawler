def find_wireless_charge(namu_row,danawa_row,cetizen_row):
    #wireless_charge
    wireless_charge = ""
    if len(danawa_row) == 1 :
        if danawa_row.iloc[0]['sd_wireless_charge'] is not None:
            wireless_charge = danawa_row.iloc[0]['sd_wireless_charge'].replace(":","")
    if len(cetizen_row) == 1 and wireless_charge == "":
        if cetizen_row.iloc[0]['sc_wireless_charge'] is not None:
            wireless_charge = "무선충전"
    return wireless_charge