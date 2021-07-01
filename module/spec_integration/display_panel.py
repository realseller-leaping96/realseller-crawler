def find_display_panel(cetizen_row,danawa_row,namu_row):
    #패널종류
    #S- / P- / D- 수식어 앞에다 붙이는 방식으로 통일
    display_type = ""
    if len(cetizen_row) == 1:
        if cetizen_row.iloc[0]['sc_display_type'] is not None:
            display_type = cetizen_row.iloc[0]['sc_display_type']
            
    if len(danawa_row) == 1 and display_type == "":
        if danawa_row.iloc[0]['sd_display_type'] is not None:
            display_type = danawa_row.iloc[0]['sd_display_type']

    if len(namu_row) == 1 and display_type == "":
        if namu_row.iloc[0]['sn_display_type'] is not None:
            display_type = namu_row.iloc[0]['sn_display_type']
    display_type = display_type.replace("super ","S-").replace("Super ","S-").replace(
        "Dynamic ","D-").replace("pOLED","P-OLED").replace("Plastic 소재의 ","P-").strip()
    return display_type