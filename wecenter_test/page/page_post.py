from selenium.webdriver.common.by import By
from test.common.page import Page
from utils.log import logger


class Post(Page):

    faqi = (By.XPATH, '//*[@id="header_publish"]')
    wenzhang = (By.LINK_TEXT, '文章')
    locator_password = (By.XPATH, '//*[@id="aw-login-user-password"]')
    locator_enter = (By.XPATH, '//*[@id="login_submit"]')
    error_message = (By.XPATH, '//*[@id="login_form"]/ul/li[3]')

    def go_to_login(self):
        """进入到登录界面"""
        self.find_element(*self.locator_signin).click()

    def login(self,username,password):
        """输入用户名和密码"""
        self.find_element(*self.locator_username).send_keys(username)
        self.find_element(*self.locator_password).send_keys(password)

    def click_element(self):
        """点击登录按钮"""
        self.find_element(*self.locator_enter).click()

    def alert_sign(self):
        """获取异常信息"""
        info = self.find_element(*self.error_message).text
        logger.info('login failed : %s' % info)
        return info
