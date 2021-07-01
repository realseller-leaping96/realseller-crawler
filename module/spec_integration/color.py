import re
from module.spec_integration.replacer import replace_all

def find_color(namu_row,danawa_row,cetizen_row):
    #color
    color = ""
    if len(namu_row) == 1:
        if namu_row.iloc[0]['sn_color'] is not None:
            color = namu_row.iloc[0]['sn_color']
            color = re.sub("\[[0-9]+\](GB)","",color).replace("&",","
                    ).replace(",","|")

    replace_dict = {"기본":""}
    return replace_all(color,replace_dict)
