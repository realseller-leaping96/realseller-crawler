def find_comm_stand(cetizen_row,danawa_row,namu_row):
    # 통신규격
    # 5G/4G 기재된거중에 높은 통신규격
    communication_standard = ""
    if len(cetizen_row) == 1:
        if cetizen_row.iloc[0]['sc_5g'] is not None:
            communication_standard = '5G'
        elif cetizen_row.iloc[0]['sc_4g'] is not None:
            communication_standard = '4G'
    if len(danawa_row) == 1 and communication_standard == "":
        if danawa_row.iloc[0]['sd_5g'] is not None:
            communication_standard = '5G'
        elif danawa_row.iloc[0]['sd_4g'] is not None:
            communication_standard = '4G'
    if len(namu_row) == 1 and communication_standard == "":
        if namu_row.iloc[0]['sn_5g'] is not None:
            communication_standard = '5G'
        elif namu_row.iloc[0]['sn_4g'] is not None:
            communication_standard = '4G'
    return communication_standard