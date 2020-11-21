from selenium import webdriver
import unittest

import  cgi


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get('https://www.baidu.com/')


        cls.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_5__"]/div').click()

        cls.driver.switch_to("TANGRAM__PSP_11__form")

        form=cgi.FieldStorage()

        # 获取数据
        site_name=form.getvalue('userName')
        site_url=form.getvalue('password')

        print(site_name, site_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()