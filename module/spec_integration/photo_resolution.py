import re

def find_photo_resolution(namu_row,danawa_row,cetizen_row):
    #photo_resolution
    photo_resolution = ""
    if len(cetizen_row) == 1:
        if cetizen_row.iloc[0]['sc_photo_resolution'] is not None:
            photo_resolution = cetizen_row.iloc[0]['sc_photo_resolution']
    return re.sub(' \([0-9. ]+메가픽셀\)',"",photo_resolution)