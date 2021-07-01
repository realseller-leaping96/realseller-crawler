def find_release_date(namu_row,danawa_row,cetizen_row):
    #release_date
    release_date = ""
    if len(cetizen_row) == 1:
        if cetizen_row.iloc[0]['sc_release_date'] is not None:
            release_date = cetizen_row.iloc[0]['sc_release_date']
    return release_date