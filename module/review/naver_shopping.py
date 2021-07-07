import pandas as pd
from bs4 import BeautifulSoup

def parse_naver_shopping(driver,df_input,crawl_data,index,option):
    if option == "skt":
        url1 = 'https://search.shopping.naver.com/search/category?catId=50000246&frm=NVSHMDL&iq='
    elif option == "kt":
        url1 = 'https://search.shopping.naver.com/search/category?catId=50000247&frm=NVSHMDL&iq='
    elif option == "lg":
        url1 = 'https://search.shopping.naver.com/search/category?catId=50000248&frm=NVSHMDL&iq='
    else:
        url1 = 'https://search.shopping.naver.com/search/category?catId=50000204&frm=NVSHMDL&iq='
    url2 = '&origQuery&pagingIndex=1&pagingSize=40&productSet=model&query&sort=rel&timestamp=&viewType=list'
    driver.get(url1+df_input.iloc[index][4]+url2)
    driver.implicitly_wait(3)
    
    
    #페이지에 있는 링크 다 긁어오기, 일단 스크롤기능 추가안해서 5개만 가져옴 => 5개 넘어가면 검색정확도 떨어져서 고정
    req = driver.page_source
    soup=BeautifulSoup(req, 'html.parser')
    div_list = soup.select(".basicList_info_area__17Xyo")
    
    link_list = []
    for i in range(len(div_list)):
        if div_list[i].select("div.basicList_info_area__17Xyo > div.basicList_etc_box__1Jzg6 > a") == []:
            pass
        else:
            link_list.append(div_list[i].select(".basicList_link__1MaTN")[0])
    

    for link in link_list:
        url = 'window.open("' + link.get('href') +'");'
        driver.execute_script(url)
        driver.switch_to.window(driver.window_handles[-1])
        req = driver.page_source
        soup=BeautifulSoup(req, 'html.parser')
        review_list = soup.select(".reviewItems_list_review__1sgcJ")
        if len(review_list)>0:
            review_list = review_list[0].find_all("li")
        
        for review in review_list:
            area1 = review.select(".reviewItems_etc_area__2P8i3")
            area1 = area1[0].find_all("span")
            
            star = area1[0].text.replace("평점","") 
            market = area1[3].text 
            write_id = area1[4].text 
            upload_day = area1[5].text 
            
            area2 = review.select(".reviewItems_review_text__2Bwpa")
            title = area2[0].select(".reviewItems_title__39Z8H")[0].text
            text = area2[0].select(".reviewItems_text__XIsTc")[0].text
            
            my_dict = {
                "pl_id": df_input.iloc[index]['pl_id'],              #기종아이디(자체부여한것)
                "pl_model_code": df_input.iloc[index]['pl_model_code'],      #모델코드
                "pl_name": df_input.iloc[index]['pl_name'],            #모델영문명

                "star": star,                       #별점
                "market": market,                   #구입처(ex 인터파크, 11번가)
                "write_id": write_id,               #작성자(일부가림처리)
                "upload_date": upload_day,           #업로드날짜
                "title":title,                      #리뷰제목 
                "content": text,                       #리뷰내용 
                "URL": driver.current_url
            }
            
            if my_dict is None or my_dict == None:
                pass
            else:
                a = pd.DataFrame(my_dict,index=[0])
                crawl_data = crawl_data.append(a)
                
                
        
        # 현재 탭 닫기
        driver.close()
        # 맨 처음 탭으로 변경(0번 탭)
        driver.switch_to.window(driver.window_handles[0])
    #display(crawl_data)
    return crawl_data