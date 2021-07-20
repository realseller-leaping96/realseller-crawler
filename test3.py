import module.chrome_driver_module as chrome_driver_module
driver = chrome_driver_module.ChromeDriver().driver


#ID.py파일이 필요합니다.
from selenium import webdriver


#네이버 아이디 비밀번호 입력해놓은 파일
#ID.py입니다.
NAVER={
    'id': 'leaping19',
    'passwd':'dkwn!2019'
}

myID=NAVER["id"]
myPASSWD=NAVER["passwd"]
driver = chrome_driver_module.ChromeDriver().driver
driver.implicitly_wait(3) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
# Login
driver.get('https://nid.naver.com/nidlogin.login') # 네이버 로그인 URL로 이동하기
driver.execute_script("document.getElementsByName('id')[0].value=\'"+ myID +"\'") #id입력
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+ myPASSWD +"\'")#pw입력
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click() # 로그인 버튼클릭하기