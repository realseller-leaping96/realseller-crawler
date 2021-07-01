def find_camera_aperture(namu_row,danawa_row,cetizen_row):
    #camera_aperture
    camera_aperture = ""
    if len(cetizen_row) == 1:
        if cetizen_row.iloc[0]['sc_camera_aperture'] is not None:
            camera_aperture = cetizen_row.iloc[0]['sc_camera_aperture'].replace("/","")
            
    if len(danawa_row) == 1 and camera_aperture == "":
        if danawa_row.iloc[0]['sd_camera_aperture'] is not None:
            camera_aperture = danawa_row.iloc[0]['sd_camera_aperture']
    camera_aperture = camera_aperture.replace(" ","")
    return camera_aperture