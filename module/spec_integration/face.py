def find_face(namu_row,danawa_row,cetizen_row):
    #face
    face = ""
    if len(namu_row) == 1:
        if namu_row.iloc[0]['sn_face'] is not None:
            face = namu_row.iloc[0]['sn_face']
            
    if len(danawa_row) == 1 and face == "":
        if danawa_row.iloc[0]['sd_face'] is not None:
            face = danawa_row.iloc[0]['sd_face']

    if len(cetizen_row) == 1 and face == "":
        if cetizen_row.iloc[0]['sc_face'] is not None:
            face = cetizen_row.iloc[0]['sc_face']
    return face