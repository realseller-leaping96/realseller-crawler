import pyperclip
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

#네이버자동로그인 감지우회 함수
def copy_input(driver,xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)

def auto_login(driver):
    naver_id = """"""
    naver_pw = """"""
    driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

    copy_input(driver,'//*[@id="id"]', naver_id)
    time.sleep(1)
    copy_input(driver,'//*[@id="pw"]', naver_pw)
    time.sleep(1)
    driver.find_element_by_css_selector('.login_form > input.btn_global').click()