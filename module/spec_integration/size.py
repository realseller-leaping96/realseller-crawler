def find_thickness(danawa_row,cetizen_row,namu_row):
    #thickness
    thickness = ""
    if len(danawa_row) == 1 :
        if danawa_row.iloc[0]['sd_thickness'] is not None:
            if danawa_row.iloc[0]['sd_thickness'].find("~") == -1:
                thickness = danawa_row.iloc[0]['sd_thickness']
    if len(cetizen_row) == 1 and thickness == "":
        if cetizen_row.iloc[0]['sc_thickness'] is not None:
            thickness = cetizen_row.iloc[0]['sc_thickness']
    if len(namu_row) == 1 and thickness == "":
        if namu_row.iloc[0]['sn_thickness'] is not None:
            thickness = namu_row.iloc[0]['sn_thickness']
    return thickness

def find_width(namu_row,danawa_row,cetizen_row):
    #width
    width = ""
    if len(danawa_row) == 1 :
        if danawa_row.iloc[0]['sd_width'] is not None:
            if danawa_row.iloc[0]['sd_width'].find("~") == -1:
                width = danawa_row.iloc[0]['sd_width']
    if len(cetizen_row) == 1 and width == "":
        if cetizen_row.iloc[0]['sc_width'] is not None:
            width = cetizen_row.iloc[0]['sc_width']
    if len(namu_row) == 1 and width == "":
        if namu_row.iloc[0]['sn_width'] is not None:
            width = namu_row.iloc[0]['sn_width']
    return width

def find_height(namu_row,danawa_row,cetizen_row):
    #height
    height = ""
    if len(danawa_row) == 1 :
        if danawa_row.iloc[0]['sd_height'] is not None:
            if danawa_row.iloc[0]['sd_height'].find("~") == -1:
                height = danawa_row.iloc[0]['sd_height']
    if len(cetizen_row) == 1 and height == "":
        if cetizen_row.iloc[0]['sc_height'] is not None:
            height = cetizen_row.iloc[0]['sc_height']
    if len(namu_row) == 1 and height == "":
        if namu_row.iloc[0]['sn_height'] is not None:
            height = namu_row.iloc[0]['sn_height']
    return height

def find_weight(namu_row,danawa_row,cetizen_row):
    #weight
    weight = ""
    if len(danawa_row) == 1 :
        if danawa_row.iloc[0]['sd_weight'] is not None:
            if danawa_row.iloc[0]['sd_weight'].find("~") == -1:
                weight = danawa_row.iloc[0]['sd_weight']
    if len(cetizen_row) == 1 and weight == "":
        if cetizen_row.iloc[0]['sc_weight'] is not None:
            weight = cetizen_row.iloc[0]['sc_weight']
    if len(namu_row) == 1 and weight == "":
        if namu_row.iloc[0]['sn_weight'] is not None:
            weight = namu_row.iloc[0]['sn_weight']
    weight = weight.replace("\r","")
    return weight