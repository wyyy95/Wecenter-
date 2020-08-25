from wecenter_test.common.browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from utils.log import logger
from selenium.webdriver.support import expected_conditions as EC

class Page(Browser):
    def __init__(self, page=None, browser_type='chrome'):
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__(browser_type=browser_type)

    def get_driver(self):
        return self.driver

    def find_element(self, *loc):
        """
        查找单一元素
        :param loc:
        :return:
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            # log.logger.info('The page of %s had already find the element %s'%(self,loc))
            # return self.driver.find_element(*loc)
        except Exception as e:
            logger.exception('finding element timeout!, details', exc_info=True)
            raise e
        else:
            logger.info('The page of %s had already find the element %s' % (self, loc))
            return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        """
        查找一组元素
        :param loc:
        :return:
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            # log.logger.info('The page of %s had already find the element %s' % (self, loc))
            # return self.driver.find_elements(*loc)
        except Exception as e:
            logger.exception('finding element timeout!, details', exc_info=True)
            raise e
        else:
            logger.info('The page of %s had already find the element %s' % (self, loc))
            return self.driver.find_elements(*loc)

