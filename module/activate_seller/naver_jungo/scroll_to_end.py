#네이버 무한스크롤함수
import time
from datetime import datetime, timedelta

def scroll_to_end(driver):
    SCROLL_PAUSE_TIME = 2
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")        

    while True:
        # Scroll down to bottom                                                      
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)                                                
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")  
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height            
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        post_list = driver.find_elements_by_css_selector('#itemList > li.board_box')
        last_post = post_list[-1].find_element_by_css_selector('.user_area > .time').text
        if last_post.find(":")!= -1:
            current_date = datetime.today().date()
        else:
            last_post = last_post.replace(".0"," ").replace("."," ").strip().split(" ")
            last_post = list(map(int, last_post))
            current_date = datetime(2000+last_post[0], last_post[1], last_post[2]).date()
        if datetime.today().date() - current_date >= timedelta(days=14) or last_height == new_height:                                                
            break

        last_height = new_height