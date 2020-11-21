import  unittest
from magentocommerce_test.homepage import  HomePage
from magentocommerce_test.basetestcase import BaseTestCase
from magentocommerce_test.search import SearchResults

from xmlrunner import  xmlrunner
class SearchProductTest(BaseTestCase):
    def SearchForProduct(self):
        homepage=HomePage(self.driver)
        search_results=homepage.search.searchFor("美赞臣")
        print(search_results.product_count,"    对比   ")
        self.assertEqual(30,search_results.product_count)
        product=search_results.open_product_page('美赞臣(MeadJohnson)蓝臻婴儿配方奶粉 2段(6-12月龄) 900克(罐装) 荷兰原装进口 20倍乳铁蛋白')
        self.assertIn("美赞臣(MeadJohnson)蓝臻婴儿配方奶粉 2段(6-12月龄) 900克(罐装) 荷兰原装进口 20倍乳铁蛋白",product.name)
        print("价格=",product.price,"      名字=",product.name)
        self.assertEqual("428.00",product.price)


if __name__=="__main__":
    # unittest.main(verbosity=2)
    searchTest=unittest.TestLoader().loadTestsFromTestCase(SearchProductTest)
    suite=unittest.TestSuite([searchTest])

    xmlrunner.XMLTestRunner(verbosity=2,output="test_reports").run(suite)
