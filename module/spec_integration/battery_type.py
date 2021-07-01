import re

def find_battery_type1(namu_row,danawa_row,cetizen_row):
    #battery_type1, 배터리타입(종류)
    battery_type1 = ""
    if len(cetizen_row) == 1 :
        if cetizen_row.iloc[0]['sc_battery_type1'] is not None:
            battery_type1 = cetizen_row.iloc[0]['sc_battery_type1']

    if len(namu_row) == 1 and battery_type1 == "":
        if namu_row.iloc[0]['sn_battery_type1'] is not None:
            battery_type1 = namu_row.iloc[0]['sn_battery_type1'].replace("내장형","").replace("착탈식","").strip()
    return battery_type1

def find_battery_type2(namu_row,danawa_row,cetizen_row):
    #battery_type2 배터리특징 (충전기술 및 와트)
    battery_type2 = ""
    if len(namu_row) == 1:
        if namu_row.iloc[0]['sn_battery_type2'] is not None:
            battery_type2 = namu_row.iloc[0]['sn_battery_type2'].replace(",","").replace(" W)","W) "
            ).replace("삼성전자의","Samsung").replace("삼성전자","Samsung"
            ).replace("퀄컴 퀵 차지","Qualcomm Quick Charge"
            ).replace("미디어텍","MediaTek").replace("(- W)","").strip()
    return battery_type2

def find_battery_type3(namu_row,danawa_row,cetizen_row):
    #battery_type3, 배터리장착방식
    battery_type3 = ""
    if len(cetizen_row) == 1 :
        if cetizen_row.iloc[0]['sc_battery_type3'] is not None:
            battery_type3 = cetizen_row.iloc[0]['sc_battery_type3'].replace("급속충전 ","")
    if len(danawa_row) == 1 and battery_type3 == "":
        if danawa_row.iloc[0]['sd_battery_type3'] is not None:
            battery_type3 = danawa_row.iloc[0]['sd_battery_type3'].replace("배터리","").replace("탈착","분리")
    return battery_type3