from module.spec_integration.replacer import replace_all

def find_back_camera(namu_row,danawa_row,cetizen_row,front_camera):
    #back_camera
    back_camera = ""
    if len(danawa_row) == 1 :
        if danawa_row.iloc[0]['sd_back_camera'] is not None:
            if danawa_row.iloc[0]['sd_back_camera'].find("~")==-1:
                back_camera = danawa_row.iloc[0]['sd_back_camera'].replace(",","")
    if len(namu_row) == 1 and front_camera == "":
        if namu_row.iloc[0]['sn_back_camera'] is not None:
            back_camera = namu_row.iloc[0]['sn_back_camera'].replace(" ","")

    replace_dict = {"만화소":"만"}
    return replace_all(back_camera,replace_dict)