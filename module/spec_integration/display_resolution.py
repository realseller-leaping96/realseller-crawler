def find_display_resol(cetizen_row,danawa_row,namu_row):
    display_resolution = ""
    if len(cetizen_row) == 1:
        if cetizen_row.iloc[0]['sc_display_resolution'] is not None:
            display_resolution = cetizen_row.iloc[0]['sc_display_resolution']
            # resolution_list = display_resolution.split("x")
            # width = resolution_list[0]
            # height = resolution_list[1]
            # display_resolution = height+"x"+width
            
    if len(danawa_row) == 1 and display_resolution == "":
        if danawa_row.iloc[0]['sd_display_resolution'] is not None:
            display_resolution = danawa_row.iloc[0]['sd_display_resolution'].replace(" ","")

    if len(namu_row) == 1 and display_resolution == "":
        if namu_row.iloc[0]['sn_display_resolution'] is not None:
            display_resolution = namu_row.iloc[0]['sn_display_resolution'].replace(" ","")

    # "x"를 기준으로 split해서 둘중에 큰값/작은값 비교해서 재구성 
    resolution_list = display_resolution.split("x")
    if len(resolution_list) > 1:
        width = resolution_list[0]
        height = resolution_list[1]
        display_resolution = height+"x"+width
        
    return display_resolution