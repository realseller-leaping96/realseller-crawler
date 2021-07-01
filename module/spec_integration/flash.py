def find_flash(namu_row,danawa_row,cetizen_row) :
    #flash
    flash = ""
    if len(cetizen_row) == 1:
        if cetizen_row.iloc[0]['sc_flash'] is not None:
            flash = cetizen_row.iloc[0]['sc_flash']
    if len(namu_row) == 1 and flash == "":
        if namu_row.iloc[0]['sn_flash'] is not None:
            flash = namu_row.iloc[0]['sn_flash'].replace("듀얼-","Dual "
                    ).replace("듀얼","Dual").replace("쿼드-","Quad "
                    ).replace("광학 2배줌 지원",""
                    ).replace("광학 2배줌 지원","").replace("광학 1.85배줌 지원",""
                    ).replace("LASER AF 및","").replace("플래시","")
    return flash