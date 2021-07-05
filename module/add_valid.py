import re

#리뷰내용중에서 앞뒤 공백 전체제거하는 함수
def fix(df, col):
    for i in df.index:
        cont = str(df.iloc[i][col])
        cont = cont.strip()
        cont = cont.replace("","") 
        cont = re.sub('([\\n\r\n]+[ ]+)',"",cont)
        df.iloc[i][col] = cont +"[0123456789]"
    return df


#리뷰내용중에서 제품내용 포함되어있는지 valid 열 추가하는 함수
def fillter(df,col):
    df['pr_valid'] = 'N'
    regex = re.compile(
        r'용량|색|사이즈|인치|화면|무게|센치|배터리|카메라|메모리|성능|출시|속도'
        + r'|[0-9]+기가|보급형|방수|무선충전|지문인식|스크린|디스플레이|스펙|내장'
        + r'|외장|컬러|버튼|단자|현상|듀얼|화소|내구성|발열|업데이트|C타입'
        )
    for i in df.index:
        cont = str(df.loc[i, col])
        if regex.search(cont): 
            df.loc[i,'pr_valid'] = 'Y'
        else:
            pass
        df.loc[i, col] = cont
    return df
