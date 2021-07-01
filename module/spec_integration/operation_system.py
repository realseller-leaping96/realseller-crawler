import re

def find_os(cetizen_row,danawa_row,namu_row):
    #운영체제
    # 안드로이드, iOS 중 최신버전만 남기기 (UI, 삼성,LG,옵티머스등 자체추가OS는 생략)
    os = ""
    if len(cetizen_row) == 1:
        if cetizen_row.iloc[0]['sc_os'] is not None:
            os = re.sub(('삼성.*|옵티머스.*'),"",cetizen_row.iloc[0]['sc_os'])
            os_split = os.split("|")
            os_split = re.search('[0-9.]+',os_split[-1]).group()
            if os.find("iOS") != -1:
                os = 'iOS ' +  os_split
            elif os.find("안드로이드") != -1:
                os = 'Android ' +  os_split
    if len(danawa_row) == 1 and os == "":
        if danawa_row.iloc[0]['sd_os'] is not None:
            os = danawa_row.iloc[0]['sd_os']
            os_split = os.split("|")
            os_split = re.search('[0-9.]+',os_split[-1]).group()
            if os.find("iOS") != -1:
                os = 'iOS ' +  os_split
            elif os.find("안드로이드") != -1:
                os = 'Android ' +  os_split
    if len(namu_row) == 1 and os == "":
        if namu_row.iloc[0]['sn_os'] is not None:
            os = re.sub(('삼성.*|옵티머스.*|Samsung.*|LG.*'),"",namu_row.iloc[0]['sn_os'])
            os_split = os.split("|")
            os_split = re.search('[0-9.]+',os_split[-1]).group()
            if os.find("iOS") != -1:
                os = 'iOS ' +  os_split
            elif os.find("안드로이드") != -1:
                os = 'Android ' +  os_split
    return os