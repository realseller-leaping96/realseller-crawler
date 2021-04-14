def crawl_biometrics_row(temp_dict,td):
    biometrics = td[1].text
    #temp_dict["생체인식"] = biometrics
    biometrics.replace("얼굴인식", "/얼굴인식")
    biometrics.replace("지문인식", "/지문인식")
    biometrics.replace("음성인식", "/음성인식")
    biometrics.replace("홍채인식", "/홍채인식")

    biometrics.replace("Touch ID", "/Touch ID")
    biometrics.replace("Face ID", "/Face ID")

    biometrics_list = biometrics.split("/")
    for bio in biometrics_list:
        if bio.find("얼굴인식") != -1:
            temp_dict["얼굴인식"] = bio.replace("얼굴인식 -","")

        elif bio.find("지문인식") != -1:
            temp_dict["지문인식"] = bio.replace("지문인식 -","")

        elif bio.find("음성인식") != -1:
            temp_dict["음성잠금해제"] = bio.replace("음성인식 -","")

        elif bio.find("홍채인식") != -1:
            temp_dict["홍채인식"] = bio.replace("홍채인식 -","")

        elif bio.find("Touch ID")  != -1:
            temp_dict["지문인식"] = bio.replace("Touch ID -","")

        elif bio.find("Face ID")  != -1:
            temp_dict["얼굴인식"] = bio.replace("Face ID -","")

    

    return temp_dict