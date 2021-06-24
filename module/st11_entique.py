import pandas as pd
from bs4 import BeautifulSoup

def parse_11_entique(driver,df_input,crawl_data,index,option):
    url1 = 'https://search.11st.co.kr/Search.tmall?method=getCatalogPrdSearch&catalogYN=Y&kwd='
    driver.get(url1+df_input.iloc[index]['pl_name']+"#chkCtgrNo%%1002724%%중고폰%%5$$")
    driver.implicitly_wait(3)
    
    
    #페이지에 있는 링크 다 긁어오기, 일단 스크롤기능 추가안해서 5개만 가져옴 => 5개 넘어가면 검색정확도 떨어져서 고정
    req = driver.page_source
    soup=BeautifulSoup(req, 'html.parser')
    ####################################################################################
    link_list = soup.select(".c_card_info_top > .c_prd_name_row_1 > a")### 여기서 a태그를 긁지말고 더 상위엘레먼트에서 제목으로 판별하고 넘어가기
    trash_can = list()
    for num in range(len(link_list)):
        #print(link_list[num].text.replace(" ","")," |VS| ",df_input.iloc[index]['pl_name'].replace(" ",""))
        
        #1.공백제거
        if df_input.iloc[index]['pl_name'].replace(" ","") in  link_list[num].text.replace(" ","") :
            #print("good")
            pass

        #2.대문자로비교
        elif df_input.iloc[index]['pl_name'].replace(" ","").upper() in  link_list[num].text.replace(" ","").upper() :
            #print("good")
            pass

        #3.소문자로비교
        elif df_input.iloc[index]['pl_name'].replace(" ","").lower() in  link_list[num].text.replace(" ","").lower() :
            #print("good")
            pass

        #4.프로=>pro / 맥스=>max / 플러스=>plus / 와이드=wide> / 스타=star> / 엣지=edge> 
        # 액티브=active / 줌=>zoom / 호핀=>hoppin / 그랜드=>grand / 노트=>note / 폴더=>folder
        # 온=>on / 알파=>alpha / 코어=>core / 어드밴스=>advance / 윈=>win / 골든=>golden
        # 메가=>mega / 팝=>pop / 에이스=>ace / 진=>jean
        elif df_input.iloc[index]['pl_name'].replace(" ","").lower().replace("프로","pro"
        ).replace("맥스","max").replace("플러스","plus").replace("와이드","wide"
        ).replace("스타","star").replace("엣지","edge").replace("액티브","active"
        ).replace("줌","zoom").replace("호핀","hoppin").replace("그랜드","grand"
        ).replace("노트","note").replace("폴더","folder").replace("온","on"
        ).replace("알파","alpha").replace("코어","core").replace("코어","core"
        ).replace("어드밴스","advance").replace("윈","win").replace("골든","golden"
        ).replace("메가","mega").replace("팝","pop").replace("에이스","ace"
        ).replace("진","jean") in  link_list[num].text.replace(" ","").lower().replace("프로","pro"
        ).replace("맥스","max").replace("플러스","plus").replace("와이드","wide"
        ).replace("스타","star").replace("엣지","edge").replace("액티브","active"
        ).replace("줌","zoom").replace("호핀","hoppin").replace("그랜드","grand"
        ).replace("노트","note").replace("폴더","folder").replace("온","on"
        ).replace("알파","alpha").replace("코어","core").replace("코어","core"
        ).replace("어드밴스","advance").replace("윈","win").replace("골든","golden"
        ).replace("메가","mega").replace("팝","pop").replace("에이스","ace"
        ).replace("진","jean") :
            #print("good")
            pass
        
        else:
            #print("bad")
            trash_can.append(link_list[num])
    # in check으로 제목판별?
    # 실제 타겟이랑 기종이랑 다른부분에 대한 예외처리 추가
    for trash in trash_can:
        link_list.remove(trash)
    ####################################################################################
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
                "pl_name": df_input.iloc[index]['pl_name'],                    #모델한글명

                "star": star.replace("판매자 평점 별5개 중 ","").replace("개",""),                             #별점
                "market": "11번가",                                                          #구입처(ex 인터파크, 11번가)
                "write_id": review.find('strong', {'class': 'name'}).text,                   #작성자(일부가림처리)
                "upload_date": review.find('span', {'class': 'date'}).text,                   #업로드날짜
         
                "content": review.find('span', {'class': 'summ_conts'}).text,                   #리뷰내용 
                                              #리뷰대상이 되는 상품!!(실제랑 다를 수 있으므로)
                "URL":driver.current_url
            }
            
            crawl_data = crawl_data.append(pd.DataFrame(my_dict,index=[0]))
        
        
    return crawl_data