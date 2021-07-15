import re

def valid_dealing(dealing_count,string):
    samsung1 = """갤럭시( )?(그랜드|노트|a|s|진|w|j|줌|골든|알파
    |윈|r|z플립|와이드|폴더|코어|온7|팝|메가|라운드|에이스|폴드|m|네오|u|지오)([0-9]+)?"""
    samsung2 = """galaxy( )?(grand|wide|note|ace|alpha|a|s|
    jean|w|j|zoom|golden|win|r|z|folder|core|on7|pop|mega|round|ace|fold|m|neo|u|gio)( )?([0-9]+|flip)?2""" 
    lg = """(lg)?( )?(프라다|prada|옵티머스|g|x|(스마트)?폴더|folder|q|
    볼트|윙|아카|벨벳|aka|velvet|클래스|class|stylo|스타일로|stylus|
    스타일러스|f|v|엑스|wine|와인)( )?([0-9]+)?(screen|스크린|skin|
    스킨|flex|플렉스|thinq|plus|power|파워|스마트|smart|pro)?"""
    apple = """(아이폰|iphone)"""

    #판매중인 물품이 스마트폰인지 판별(추측)
    if re.search(samsung1,string.lower()): 
        dealing_count += 1
    elif re.search(samsung2,string.lower()): 
        dealing_count += 1
    elif re.search(apple,string.lower()): 
        dealing_count += 1
    elif re.search(lg,string.lower()): 
        dealing_count += 1
    
    return dealing_count