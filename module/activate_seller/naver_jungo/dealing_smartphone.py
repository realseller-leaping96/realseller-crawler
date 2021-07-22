import re

def valid_dealing(dealing_count,string):
    samsung1_tier1 = ["그랜드","노트","a","s","진","w","j","줌","골든","알파","윈","r",
    "z플립","와이드","폴더","코어","온7","팝","메가","라운드","에이스","폴드","m","네오","u",
    "지오"]

    samsung2_tier1 = ["grand","wide","note","ace","alpha","a","s","jean","w","j",
    "zoom","golden","win","r","z","folder","core","on7","pop","mega","round","ace","fold",
    "m","neo","u","gio"]

    lg_tier1 = ["프라다","prada","옵티머스","g","x","(스마트)?폴더","folder","q",
    "볼트","윙","아카","벨벳","aka","velvet","클래스","class","stylo","스타일로",
    "stylus","스타일러스","f","v","엑스","wine","와인"]

    lg_tier2 = ["screen","스크린","skin","스킨","flex","플렉스","thinq","플러스",
    "plus","power","파워","스마트","smart","pro","프로"]

    apple_tier1 = ["아이폰","iphone"]

    samsung1_pattern = "갤럭시( )?("+"|".join(samsung1_tier1)+")([0-9]+)?"
    samsung2_pattern = "galaxy( )?("+"|".join(samsung2_tier1)+")( )?([0-9]+|flip)?"
    lg_pattern = "(lg)?( )?("+"|".join(lg_tier1)+")( )?([0-9]+)?" + "("+"|".join(lg_tier2)+")?"
    apple_pattern = "("+"|".join(apple_tier1)+")"


    #판매중인 물품이 스마트폰인지 판별(추측)
    if re.search(samsung1_pattern,string.lower()): 
        dealing_count += 1
    elif re.search(samsung2_pattern,string.lower()): 
        dealing_count += 1
    elif re.search(apple_pattern,string.lower()): 
        dealing_count += 1
    elif re.search(lg_pattern,string.lower()): 
        dealing_count += 1
    
    return dealing_count