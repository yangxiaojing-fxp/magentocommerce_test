from selenium import  webdriver




from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import  WebDriverWait

from selenium.webdriver.support import expected_conditions

import unittest

class A(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

        self.driver.maximize_window()
        url='http://www.baidu.com'
        self.driver.get(url)
    def testA(self):
        aa="By.ID"
        print(type(aa))
        bb="kw"
        cc=WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((eval(aa),bb)))
        cc.send_keys("123")
        self.assertAlmostEqual()
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()