def find_front_video_resol(namu_row,danawa_row,cetizen_row):
    #front_video_resolution
    front_video_resolution = ""
    if len(cetizen_row) == 1:
        if cetizen_row.iloc[0]['sc_front_video_resolution'] is not None:
            front_video_resolution = cetizen_row.iloc[0]['sc_front_video_resolution'].replace(")",") "
                ).replace("(Full HD)","").replace("(UHD)","").replace("(HD)",""
                ).replace("(WVGA)","").replace("(NTSC)","").replace("(VGA)","").replace("(QVGA)",""
                ).replace("(WQVGA)","")
        front_video_resolution = front_video_resolution.strip()
        if front_video_resolution == "FPS":
            front_video_resolution = ""
    #UHD, FHD 다 지우고 다시 해상도기준으로 추가시키도록 로직작성
    return front_video_resolution