import re

def find_charging_terminal(namu_row,danawa_row,cetizen_row):
    #charging_terminal
    charging_terminal = ""
    if len(namu_row) == 1:
        if namu_row.iloc[0]['sn_charging_terminal'] is not None:
            charging_terminal = namu_row.iloc[0]['sn_charging_terminal']
            charging_terminal = re.sub("( x [0-9])","",charging_terminal.split(",")[0]).strip()
            
    if len(danawa_row) == 1 and charging_terminal == "":
        if danawa_row.iloc[0]['sd_charging_terminal'] is not None:
            charging_terminal = danawa_row.iloc[0]['sd_charging_terminal']
            if charging_terminal.find("8핀"):
                charging_terminal = "USB 2.0 Apple Lightning 8-pin"
            elif charging_terminal.find("5핀"):
                charging_terminal = "USB 2.0 micro Type-B"
            elif charging_terminal.find("타입C"):
                charging_terminal = "USB 3.1 Type-C"
    return charging_terminal