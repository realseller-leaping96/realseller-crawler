#화면인치
def find_disp_inch(cetizen_row,danawa_row,namu_row):
    display_in = ""
    if len(cetizen_row) == 1:
        if cetizen_row.iloc[0]['sc_display_in'] is not None:
            display_in = cetizen_row.iloc[0]['sc_display_in']

    if len(danawa_row) == 1 and display_in == "":
        if danawa_row.iloc[0]['sd_display_in'] is not None:
            display_in = danawa_row.iloc[0]['sd_display_in']

    if len(namu_row) == 1 and display_in == "":
        if namu_row.iloc[0]['sn_display_in'] is not None:
            display_in = namu_row.iloc[0]['sn_display_in']
    return display_in