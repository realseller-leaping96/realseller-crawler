import pandas as pd
from datetime import datetime, timedelta
from module.spec.cetizen.main import hasxpath
from module.activate_seller.naver_jungo.scroll_to_end import scroll_to_end
from module.activate_seller.naver_jungo.auto_login import auto_login
from module.activate_seller.naver_jungo.dealing_smartphone import valid_dealing
from module.activate_seller.naver_jungo.last_sell import record_last_sell

#네이버판매처 크롤링
def naver_jungo(crawl_data,seller_list,i,driver):
    
    if pd.notnull(seller_list.iloc[i]['fsl_rs_naver_nickname']):
        naver_nick_list = seller_list.iloc[i]['fsl_rs_naver_nickname'].split("|")
        url_naver_1 = """
        https://m.cafe.naver.com/ArticleSearchList.nhn?search.query=
        """ 
        url_naver_2= """
        &search.menuid=0&search.searchBy=3&search.sortBy=date&search.clubid=10050146&search.option=0&search.defaultValue=1 
        """
        #중고나라 회원인 네이버 아이디 로그인
        auto_login(driver)
        for naver_nick in naver_nick_list:
            driver.get(url_naver_1+naver_nick+url_naver_2)
            if hasxpath(driver,'//*[@id="articleList"]/ul/li[1]/div[1]/a[1]'):
                sell_count = 0    #현재 판매중인 물품수
                dealing_count = 0 #현재 판매중인 물품중 스마트폰으로 추정되는 갯수
                last_sell = ""    #가장최근 판매글 게시일
                
                driver.find_element_by_xpath('//*[@id="articleList"]/ul/li[1]/div[1]/a[1]').click()
                scroll_to_end(driver)
                post_list = driver.find_elements_by_css_selector('#itemList > li.board_box')
                
                #가장최근 판매글 게시일 기록
                last_sell = record_last_sell(last_sell,post_list)
                
                
                for post in post_list:
                    try:
                        icon_txt = post.find_element_by_css_selector('.icon_txt')
                        #2주간 판매중인 물품수 계산
                        if icon_txt.text.find("판매")!= -1:
                            #print(icon_txt.text)
                            sell_count += 1
                            
                            #판매중인 물품이 스마트폰인지 판별(추측)
                            dealing_count = valid_dealing(dealing_count,post.find_element_by_css_selector('strong.tit').text)

                    
                    except:
                        try:
                            strong_tit = post.find_element_by_css_selector('strong.tit')
                            #2주간 판매중인 물품수 계산
                            if strong_tit.text.find("[공식앱]")!=-1:
                                #print(strong_tit.text)
                                sell_count += 1
                                
                                #판매중인 물품이 스마트폰인지 판별(추측)
                                dealing_count = valid_dealing(dealing_count,strong_tit.text)
                                
                        except:
                            pass
                
                #활동여부 종합판단
                is_activate = True
                if datetime.today().date()-last_sell>=timedelta(days=14) or sell_count/dealing_count<0.5:
                    is_activate = False
                    
                
                my_dict = {
                    "vendor_type" : "중고나라", 
                    "fsl_rs_id" : seller_list.iloc[i]['fsl_rs_id'],                           #리얼셀러 아이디
                    "shop_id":naver_nick,                                                     #네이버/번장 판매자 아이디
                    "last_sell": last_sell,                                                   #가장최근 판매글 게시일
                    "sell_count": sell_count,                                                 #2주간 판매중인 물품 갯수
                    "dealing_smartphone": dealing_count,                                      #2주간 스마트폰 품목 취급여부
                    "is_activate": is_activate                                                #종합적으로 판단한 최종 활동여부
                }
                crawl_data = crawl_data.append(pd.DataFrame(my_dict, index=[0]))
            else:#닉네임으로 검색했는데 해당아이디 검색안될경우 없음처리!! => False값 밀어넣기
                my_dict = {
                    "vendor_type" : "중고나라", 
                    "fsl_rs_id" : seller_list.iloc[i]['fsl_rs_id'],                           #리얼셀러 아이디
                    "shop_id":naver_nick,                                                     #네이버/번장 판매자 아이디
                    "last_sell": None,                                                   #가장최근 판매글 게시일
                    "sell_count": None,                                                 #2주간 판매중인 물품 갯수
                    "dealing_smartphone": None,                                      #2주간 스마트폰 품목 취급여부
                    "is_activate": False                                                #종합적으로 판단한 최종 활동여부
                }
                crawl_data = crawl_data.append(pd.DataFrame(my_dict, index=[0]))
                pass
    
    return crawl_data