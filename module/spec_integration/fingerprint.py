def find_fingerprint(namu_row,danawa_row,cetizen_row):
    #fingerprint
    fingerprint = ""
    if len(namu_row) == 1:
        if namu_row.iloc[0]['sn_fingerprint'] is not None:
            fingerprint = namu_row.iloc[0]['sn_fingerprint']
            
    if len(danawa_row) == 1 and fingerprint == "":
        if danawa_row.iloc[0]['sd_fingerprint'] is not None:
            fingerprint = danawa_row.iloc[0]['sd_fingerprint']

    if len(cetizen_row) == 1 and fingerprint == "":
        if cetizen_row.iloc[0]['sc_fingerprint'] is not None:
            fingerprint = cetizen_row.iloc[0]['sc_fingerprint']
    return fingerprint