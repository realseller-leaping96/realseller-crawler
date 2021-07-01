#딕셔너리 대로 문자열 치환하는함수
def replace_all(txt,dic):
    for d in dic.items():
        txt = txt.replace(d[0],d[1])
    return txt