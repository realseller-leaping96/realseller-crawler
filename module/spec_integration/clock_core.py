import re
def find_core_clock(namu_row,cetizen_row,danawa_row):
    #코어클럭
    core_clock = ""
    
    if len(namu_row) == 1 and core_clock == "":
        if namu_row.iloc[0]['sn_core_clock'] is not None:
            if re.search('[0-9.]+ GHz',namu_row.iloc[0]['sn_core_clock']) is not None:
                core_clock_iter = re.finditer('[0-9.]+ GHz',namu_row.iloc[0]['sn_core_clock'])
                for matchObj in core_clock_iter:
                    if core_clock == "":
                        core_clock = matchObj.group()
                    else:
                        core_clock += "+" + matchObj.group()   
    if len(cetizen_row) == 1:
        if cetizen_row.iloc[0]['sc_core_clock'] is not None:
            core_clock = str(int(cetizen_row.iloc[0]['sc_core_clock'].replace("MHz",""))/1000)+("GHz")
            
    if len(danawa_row) == 1 and core_clock == "":
        if danawa_row.iloc[0]['sd_core_clock'] is not None:
            core_clock = danawa_row.iloc[0]['sd_core_clock']
    core_clock = core_clock.replace(" " ,"")
    return core_clock