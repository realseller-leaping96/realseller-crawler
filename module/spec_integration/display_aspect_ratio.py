import math

def find_display_ratio(cetizen_row,danawa_row,namu_row,display_resolution):
    #화면비
    display_aspect_ratio = ""
    if len(cetizen_row) == 1:
        if cetizen_row.iloc[0]['sc_display_aspect_ratio'] is not None:
            display_aspect_ratio = cetizen_row.iloc[0]['sc_display_aspect_ratio']
            
    if len(danawa_row) == 1 and display_aspect_ratio == "":
        if danawa_row.iloc[0]['sd_display_aspect_ratio'] is not None:
            display_aspect_ratio = danawa_row.iloc[0]['sd_display_aspect_ratio']

    if len(namu_row) == 1 and display_aspect_ratio == "":
        if namu_row.iloc[0]['sn_display_aspect_ratio'] is not None:
            display_aspect_ratio = namu_row.iloc[0]['sn_display_aspect_ratio']

    #비율 계산하는식/공식 반영?
    #함수화 => 정수x정수가 들어가면 비율값이 나오도록 하는
    if  display_resolution == "1792x828": 
        display_aspect_ratio = "19.5:9"
    elif  display_resolution == "2436x1125": 
        display_aspect_ratio = "19.5:9"
    elif  display_resolution == "2688x1242": 
        display_aspect_ratio = "19.5:9"
    elif  display_resolution == "1920x1080": 
        display_aspect_ratio = "16:9"
    elif display_resolution == "800x480": 
        display_aspect_ratio = "16:9"
    elif  display_resolution == "1280x720": 
        display_aspect_ratio = "16:9"
    elif  display_resolution == "2560x1440": 
        display_aspect_ratio = "16:9"
    elif  display_resolution == "1136x640":
        display_aspect_ratio = "16:9"

    if display_aspect_ratio == "":
        resolution_list = display_resolution.split("x")
        if len(resolution_list) > 1:
            width = resolution_list[0]
            height = resolution_list[1]
            gcd = math.gcd(width,height)
            a = round(height/gcd)
            b = round(width/gcd)
            if max(a,b) > 24:
                a = a/2
                b = b/2
            display_aspect_ratio = str(a)+":"+str(b)
    return display_aspect_ratio