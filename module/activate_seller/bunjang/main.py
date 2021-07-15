import pandas as pd
from module.activate_seller.bunjang.scroll_to_end import scroll_to_end as bunjang_scroll
from module.activate_seller.naver_jungo.dealing_smartphone import valid_dealing
from datetime import datetime, timedelta

def has_selector(driver,selector):
    try:
        driver.find_element_by_css_selector(selector)
        return True
    except:
        return False

def bunjang(crawl_data,seller_list,i,driver):
    if pd.notnull(seller_list.iloc[i]['fsl_rs_bunjang_mun']):
        bunjang_mun_list = str(seller_list.iloc[i]['fsl_rs_bunjang_mun']).split("|")
        url_bunjang_1 = """
        https://m.bunjang.co.kr/shop/
        """ 
        url_bunjang_2= """
        /products
        """
        for bunjang_mun in bunjang_mun_list:
            import re
            url = url_bunjang_1+str(bunjang_mun)+url_bunjang_2
            url = re.sub(r"\s+", "", url, flags=re.UNICODE)
            driver.get(url)
            
            if has_selector(driver,'a > div.sc-lcpuFF.jzFJun > div.sc-cpHetk.gMPiSy > \
                                                                div.sc-nrwXf.hPnigT > span'):
                #번장네이버 모두 없는페이지,아이디일경우 판별하는 로직 다시체크!!!

                bunjang_scroll(driver)
                #print("asdasdasd")

                post_list = driver.find_elements_by_css_selector('a > div.sc-lcpuFF.jzFJun > div.sc-bqjOQT.eTztLy')
                sell_count = len(post_list)    #2주간 판매중인 물품수
                dealing_count = 0 #2주간 판매중인 물품중 스마트폰으로 추정되는 갯수
                for post in post_list:
                    dealing_count = valid_dealing(dealing_count,post.text)

                last_sell = ""    #가장최근 판매글 게시일
                last_sell = driver.find_element_by_css_selector('a > div.sc-lcpuFF.jzFJun > div.sc-cpHetk.gMPiSy > \
                                                                div.sc-nrwXf.hPnigT > span').text


                #가장최근 판매글 게시일 기록
                # => 초?,분,시간,일,주,달 등으로 기록하여 타임델타 사용해서 변환하는 정규표현식 로직 구현할것
                if last_sell.find("초")!=-1 or last_sell.find("분")!=-1 or last_sell.find("시간")!=-1:
                    last_sell = datetime.today().date()
                elif last_sell.find("일")!=-1:
                    last_sell = int(last_sell.replace("일","").replace("전","").replace(" ",""))
                    last_sell = datetime.today().date() - timedelta(days=last_sell)
                elif last_sell.find("주")!=-1:
                    last_sell = int(last_sell.replace("주","").replace("전","").replace(" ",""))*7
                    last_sell = datetime.today().date() - timedelta(days=last_sell)
                elif last_sell.find("달")!=-1:
                    last_sell = int(last_sell.replace("달","").replace("전","").replace(" ",""))*30
                    last_sell = datetime.today().date() - timedelta(days=last_sell)
                else: #일단 여기까지 분기될필요 없을것같아 생략
                    pass


                #2주간 판매중인 물품수 계산 => 완료
                #판매중인 물품이 스마트폰인지 판별(추측) => 완료


                #활동여부 종합판단
                is_activate = True
                if datetime.today().date()-last_sell>=timedelta(days=14) or sell_count/dealing_count<0.5:
                    is_activate = False

                my_dict = {
                    "vendor_type" : "번개장터", 
                    "fsl_rs_id" : seller_list.iloc[i]['fsl_rs_id'],                           #리얼셀러 아이디
                    "shop_id":bunjang_mun,                                                     #네이버/번장 판매자 아이디
                    "last_sell": last_sell,                                                   #가장최근 판매글 게시일
                    "sell_count": sell_count,                                                 #2주간 판매중인 물품 갯수
                    "dealing_smartphone": dealing_count,                                      #2주간 스마트폰 품목 취급여부
                    "is_activate": is_activate                                                #종합적으로 판단한 최종 활동여부
                }
                crawl_data = crawl_data.append(pd.DataFrame(my_dict, index=[0]))
            else:
                my_dict = {
                    "vendor_type" : "번개장터", 
                    "fsl_rs_id" : seller_list.iloc[i]['fsl_rs_id'],                           #리얼셀러 아이디
                    "shop_id":bunjang_mun,                                                     #네이버/번장 판매자 아이디
                    "last_sell": None,                                                   #가장최근 판매글 게시일
                    "sell_count": None,                                                 #2주간 판매중인 물품 갯수
                    "dealing_smartphone": None,                                      #2주간 스마트폰 품목 취급여부
                    "is_activate": False                                                #종합적으로 판단한 최종 활동여부
                }
                crawl_data = crawl_data.append(pd.DataFrame(my_dict, index=[0]))
    
    return crawl_data


