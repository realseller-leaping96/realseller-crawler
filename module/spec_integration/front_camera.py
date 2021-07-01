from module.spec_integration.replacer import replace_all

def find_front_camera(namu_row,danawa_row,cetizen_row):
    front_camera = ""
    if len(danawa_row) == 1 :
        if danawa_row.iloc[0]['sd_front_camera'] is not None:
            if danawa_row.iloc[0]['sd_front_camera'].find("~")==-1:
                front_camera = danawa_row.iloc[0]['sd_front_camera'].replace(",","")
    if len(namu_row) == 1 and front_camera == "":
        if namu_row.iloc[0]['sn_front_camera'] is not None:
            front_camera = namu_row.iloc[0]['sn_front_camera'].replace(" ","")

    replace_dict = {"만화소":"만"}
    return replace_all(front_camera,replace_dict)

    