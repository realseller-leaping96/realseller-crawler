def find_ap_type(cetizen_row,danawa_row,namu_row):
    #AP 종류
    ap_type = ""
    if len(cetizen_row) == 1:
        if cetizen_row.iloc[0]['sc_ap_type'] is not None:
            ap_type = cetizen_row.iloc[0]['sc_ap_type']
            
    if len(danawa_row) == 1 and ap_type == "":
        if danawa_row.iloc[0]['sd_ap_type'] is not None:
            ap_type = danawa_row.iloc[0]['sd_ap_type']

    if len(namu_row) == 1 and ap_type == "":
        if namu_row.iloc[0]['sn_ap_type'] is not None:
            ap_type = namu_row.iloc[0]['sn_ap_type']
            
    ap_type = ap_type.replace("퀄컴","Qualcomm").replace("삼성","Samsung"
            ).replace("엑시노스","Exynos ").replace("(","").replace(")",""
            ).replace("SoC","").replace("애플","Apple").replace("스냅드래곤","Snapdragon"
            ).replace("[1]","").replace("미디어텍","MediaTek").strip()

    return ap_type