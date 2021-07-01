def find_core_num(cetizen_row,danawa_row,namu_row):
    #코어수
    core = ""
    if len(cetizen_row) == 1:
        if cetizen_row.iloc[0]['sc_core'] is not None:
            core = cetizen_row.iloc[0]['sc_core'].replace("1개","싱글코어"
                    ).replace("2개","듀얼코어").replace("4개","쿼드코어"
                    ).replace("6개","헥사코어").replace("8개","옥타코어"
                    ).replace(" 비트","비트")
            
    if len(danawa_row) == 1 and core == "":
        if danawa_row.iloc[0]['sd_core'] is not None:
            core = danawa_row.iloc[0]['sd_core'].replace("(1)","").replace("(2)",""
                    ).replace("(4)","").replace("(8)","")

    if len(namu_row) == 1 and core == "":
        if namu_row.iloc[0]['sn_core'] is not None:
            core = namu_row.iloc[0]['sn_core']
    return core