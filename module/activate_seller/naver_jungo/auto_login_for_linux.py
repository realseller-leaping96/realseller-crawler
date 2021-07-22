def auto_login_for_liunux(driver):
    NAVER={
        'id': '', #네이버 아이디 입력
        'passwd':'' #네이버 비밀번호 입력
    }
    myID=NAVER["id"]
    myPASSWD=NAVER["passwd"]
    # Login
    driver.get('https://nid.naver.com/nidlogin.login') # 네이버 로그인 URL로 이동하기
    driver.execute_script("document.getElementsByName('id')[0].value=\'"+ myID +"\'") #id입력
    driver.execute_script("document.getElementsByName('pw')[0].value=\'"+ myPASSWD +"\'")#pw입력
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click() # 로그인 버튼클릭하기