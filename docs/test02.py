import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email


class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    # excel = DATA_PATH + '/baidu.xlsx'

    locator_signin = (By.XPATH, '/html/body/div[1]/div/div[4]/a[1]')
    locator_username = (By.XPATH, '//*[@id="aw-login-user-name"]')
    locator_password = (By.XPATH, '//*[@id="aw-login-user-password"]')
    locator_enter = (By.XPATH, '//*[@id="login_submit"]')

    def sub_setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()

    def test_sign(self):
        # datas = ExcelReader(self.excel).data
        # for d in datas:
        #     with self.subTest(data=d):
        self.sub_setUp()
        self.driver.find_element(*self.locator_signin).click()
        self.driver.find_element(*self.locator_username).send_keys('admin')
        self.driver.find_element(*self.locator_password).send_keys('admin123!@#')
        self.driver.find_element(*self.locator_enter).click()
        time.sleep(2)
        logger.info(self.driver.title)
        self.sub_tearDown()

if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='we chat问答平台', description='第一版')
        runner.run(TestBaiDu('test_sign'),0, False)
    e = Email(title='百度搜索测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='1921142171@qq.com',
              server='smtp.163.com',
              sender='wang_yao95@163.com',
              password= 'NNWAMIKTQZOVNIAJ',
              path=report
              )
    e.send()