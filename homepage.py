from magentocommerce_test.base import BasePage,InvalidPageException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions

class HomePage(BasePage):
    _home_path="//*[@id='navitems-group1']/li[4]/a"
    def __init__(self,driver):
        super(HomePage,self).__init__(driver)
    #    _validate_page()没有对象调用过
    def _validate_page(self,driver):
        try:
            WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH,self._home_path)))
            # driver.find_element_by_xpath(self._home_path)
        except:
            raise InvalidPageException("Home Page not loaded")
