from magentocommerce_test.base import BasePage,InvalidPageException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions

class ProductPage(BasePage):
    _jiangjia_message='/html/body/div[6]/div/div[2]/div[3]/div/div[1]/div[2]/a'
    _product_name_locator_field='/html/body/div[6]/div/div[2]/div[1]'
    _product_description='//*[@id="parameter-brand"]/li'
    _product_rice='/html/body/div[6]/div/div[2]/div[3]/div/div[1]/div[2]/span[1]/span[2]'

    def __init__(self,driver):
        super(ProductPage,self).__init__(driver)

    @property
    def name(self):
        return WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH,self._product_name_locator_field))).text
        # return self.driver.find_element_by_xpath(self._product_name_locator_field).text
    @property
    def description(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH,self._product_description))).text.strip()
        # return self.driver.find_element_by_xpath(self._product_description).text.strip()
    @property
    def price(self):
        return WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH,self._product_rice))).text.strip()
        # return self.driver.find_element_by_xpath(self._product_rice).text.strip()
    def _validate_page(self,driver):
        try:
            WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, self._jiangjia_message)))
            # driver.find_element_by_class_xpath(self._jiangjia_message)
        except:
            raise  InvalidPageException("Product page not loaded")


