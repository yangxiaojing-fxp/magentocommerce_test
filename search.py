from magentocommerce_test.base import BasePage,InvalidPageException
from magentocommerce_test.product import  ProductPage

from time import sleep

from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions

class SearchRegion(BasePage):

    search_input_locator="//*[@id='key']"
    search_button_locator='//*[@id="search"]/div/div[2]/button'

    def __init__(self,driver):
        super(SearchRegion,self).__init__(driver)
    def searchFor(self,term):


        self.search_input=WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH,self.search_input_locator)))


        self.search_input.clear()
        self.search_input.send_keys(term)


        self.search_button=WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH,self.search_button_locator)))

        self.search_button.click()
        return SearchResults(self.driver)
class SearchResults(BasePage):

    _full_goods='//*[@id="categorys-2014"]/div[1]/a'
    _products_list_locator='//*[@id="J_goodsList"]/ul/li'
    _products_name_text_locator='//*[@id="J_goodsList"]/ul/li[1]/div/div[3]/a/em'
    _products_name_src='//*[@id="J_goodsList"]/ul/li[1]/div/div[3]/a'
    _page_title_locator='/html/head/title'

    _products={}

    def __init__(self,driver):
       super(SearchResults,self).__init__(driver)

       results=WebDriverWait(driver,10).until(expected_conditions.visibility_of_all_elements_located((By.XPATH,self._products_list_locator)))

       self.products_count=len(results)
       print(len(results),"调试数量",self.products_count)
       _name=''
       for product in results:
           _name=WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH,self._products_name_text_locator))).text
           # name=product.find_element_by_xpath(self._products_name_text_locator).text
           self._products[_name]=WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH,self._products_name_src)))
           # self._products[name]=product.find_element_by_xpath(self._products_name_src)
       print(_name, "调试名字")


    def _validate_page(self,driver):
        try:

            WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, self._full_goods)))
        except:
            raise InvalidPageException("Search results not loaded")

    @property
    def product_count(self):
        return self.products_count
    def get_products(self):
        return self._products
    def open_product_page(self,product_name_input):
        self._products[product_name_input].click()


        windows=self.driver.window_handles

        self.driver.switch_to.window(windows[1])
        return  ProductPage(self.driver)


