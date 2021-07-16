# 무한 스크롤
import time

def scroll_to_end(driver):
    SCROLL_PAUSE_TIME = 1

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

        upload_date_list = driver.find_elements_by_css_selector('div.sc-lcpuFF.jzFJun > div.sc-cpHetk.gMPiSy > div.sc-nrwXf.hPnigT > span')
        is_2weeks = 0
        for ud in upload_date_list:
            # print(ud.text)
            if ud.text.find("2주") != -1:
                is_2weeks = 1
        if new_height == last_height or is_2weeks == 1:                                               
            break

        last_height = new_height
