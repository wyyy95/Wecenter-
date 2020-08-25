from selenium import webdriver
from utils.file_reader import ExcelReader
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import unittest, time, ddt
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH
from wecenter_test.page.page_login import Login
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from wecenter_test.common.browser import Browser
from utils.log import logger

URL = Config().get('URL')
excelPath = DATA_PATH + '/denglu.xlsx'
reader = ExcelReader(excelPath, title_line=True)


@ddt.ddt
class TestPost(unittest.TestCase,Login,Browser):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(URL)
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    @ddt.data(* reader.data)
    def test_signin(self, data):
        username, password, except_res = tuple(data)
        self.go_to_login()
        self.login(username, password)
        self.click_element()
        try:
            self.assertEqual(self.alert_sign(),except_res)
            logger.info(self.alert_sign())
            self.save_screen_shot()
        except:
            logger.info('success')



if __name__ == '__main__':
    # unittest.main()
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='We center问答平台', description='登录功能')
        runner.run(TestPost('test_signin'))  # 需要0，False参数
    e = Email(title='We Center登录测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='18252068105@163.com',
              server='smtp.qq.com',
              sender='1336181723@qq.com',
              password='pinxywnwmdzsihac',
              path=report
              )
    e.send()

# import os, time, unittest, ddt, logging
# from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH
# from utils.log import logger
# from utils.file_reader import ExcelReader
# from utils.HTMLTestRunner import HTMLTestRunner
# from utils.mail import Email
# from wecenter_test.page.page_login import Login
#
#
# @ddt.ddt
# class TestWeCenter(unittest.TestCase):
#     URL = Config().get('URL')
#     excelPath = DATA_PATH + '/denglu.xlsx'
#     reader = ExcelReader(excelPath, title_line=True)
#
#     def setUp(self):
#         self.driver = Login().get(url=self.URL)
#         self.driver.go_to_login()
#
#     def tearDown(self):
#         self.driver.close()
#
#     @ddt.data(*reader.data)
#     def test_post(self, data):
#         username, password, except_res = tuple(data)
#         self.driver.login(username=username, passwd=password)
#         self.driver.click_element()
#         self.driver.alert_sign()
#         try:
#             sign = self.driver.alert_sign()
#             self.assertEqual(sign,except_res)
#             self.driver.save_screen_shot()
#             logger.info(sign)
#         except:
#             logger.info('登陆成功！')
#
#
#
# if __name__ == '__main__':
#     unittest.main()
#     # report = REPORT_PATH + '/report.html'
#     # with open(report, 'wb') as f:
#     #     runner = HTMLTestRunner(f, verbosity=2, title='We Center社区问答_测试报告', description='html报告')
#     #     runner.run(TestWeCenter('test_post'))
#     # e = Email(title='We Center登录测试报告',
#     #           message='这是今天的测试报告，请查收！',
#     #           receiver='18252068105@163.com',
#     #           server='smtp.qq.com',
#     #           sender='1336181723@qq.com',
#     #           password='pinxywnwmdzsihac',
#     #           path=report
#     #           )
#     # e.send()
