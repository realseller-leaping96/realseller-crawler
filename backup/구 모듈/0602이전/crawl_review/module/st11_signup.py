import pandas as pd
from bs4 import BeautifulSoup

def parse_11_signup(driver,df_input,crawl_data,index,option):
    url1 = 'https://search.11st.co.kr/Search.tmall?method=getCatalogPrdSearch&catalogYN=Y&kwd='
    driver.get(url1+df_input.iloc[index]['pl_name']+"#chkCtgrNo%%1059026%%휴대폰완납가입%%10$$$$")
    driver.implicitly_wait(3)
    
    
    #페이지에 있는 링크 다 긁어오기, 일단 스크롤기능 추가안해서 5개만 가져옴 => 5개 넘어가면 검색정확도 떨어져서 고정
    req = driver.page_source
    soup=BeautifulSoup(req, 'html.parser')
    link_list = soup.select(".c_card_info_top > .c_prd_name_row_1 > a")
    link_list = link_list[0:3]
    for link in link_list:
        driver.get(link.get('href'))
        driver.find_element_by_xpath('//*[@id="reviewLi"]/a')
        req = driver.page_source
        soup=BeautifulSoup(req, 'html.parser')
        review_list = soup.select("#reviewObj")
        review_list = review_list[0].select("div.cfix")
        
        for review in review_list:
            
            if not review.find('span', {'class': 'selr_star'}):
                star = ""
            else:
                star = review.find('span', {'class': 'selr_star'}).text
                
            my_dict = {
                "pl_id": df_input.iloc[index]['pl_id'],                      #스펙테이블 아이디
                "pl_model_code": df_input.iloc[index]['pl_model_code'],              #모델코드
                "pl_name": df_input.iloc[index]['pl_name'],                    #모델한글

                "star": star,                                                                #별점
                "market": "11번가",                                                          #구입처(ex 인터파크, 11번가)
                "write_id": review.find('strong', {'class': 'name'}).text,                   #작성자(일부가림처리)
                "upload_day": review.find('span', {'class': 'date'}).text,                   #업로드날짜
                "title":"",                                                                  #리뷰제목 => 11번가는 없음
                "text": review.find('span', {'class': 'summ_conts'}).text,                   #리뷰내용 
                "Target":link.text,                                         #리뷰대상이 되는 상품!!(실제랑 다를 수 있으므로)
                "URL":driver.current_url
            }
            
            crawl_data = crawl_data.append(pd.DataFrame(my_dict,index=[0]))
        
        
    return crawl_data
    