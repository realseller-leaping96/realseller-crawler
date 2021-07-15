import datetime
#가장최근 판매글 게시일 기록
def record_last_sell(last_sell,post_list):
    if last_sell=="" and post_list[0].find_element_by_css_selector('.user_area > .time').text.find(":")!=-1:
        last_sell = datetime.datetime.today().date()
        # print(last_sell)
    elif last_sell =="" and post_list[0].find_element_by_css_selector('.user_area > .time').text.find(":")==-1:
        last_sell = post_list[0].find_element_by_css_selector('.user_area > .time').text
        last_sell = last_sell.replace(".0"," ").replace("."," ").strip().split(" ")
        last_sell = list(map(int, last_sell))
        last_sell = datetime.datetime(2000+last_sell[0], last_sell[1], last_sell[2]).date()
        # print(last_sell)
    return last_sell