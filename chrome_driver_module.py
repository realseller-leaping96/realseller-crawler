from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class ChromeDriver:

    def __init__(self):
        self.path = '/home/an/바탕화면/chromedriver' #크롬드라이버 경로가 따로 있을경우 지정해줘야함
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')

        if self.path != '':
            self.driver  = webdriver.Chrome(executable_path=self.path,chrome_options=self.options)
        else:
            self.driver  = webdriver.Chrome()
        self.driver.implicitly_wait(3)
