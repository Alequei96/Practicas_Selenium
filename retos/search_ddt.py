import unittest
from selenium import webdriver
from ddt import ddt, data, unpack
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@ddt
class SearchDDT(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path= './chromedriver/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    #Decorador en donde se guardan las tuplas de datos esperados
    @data(('dress', 5), ('music', 5))
    @unpack #Se van a desempaquetar las tuplas de arriba 

    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        #Ya que son varios objetos dentro de la clase product-name se pone dentro de corchetes
        products = driver.find_elements(By.XPATH, '//h2[@class="product-name"]/a')
        print(f'Found {len(products)} products')

        for product in products:
            print(product.text)

        self.assertEqual(expected_count, len(products))

    @classmethod
    def tearDown(cls):
        cls.driver.close()

kwargs = {
    "output": 'ddt-report'
}

if __name__ == '__main__':
    unittest.main(verbosity=2,
                  testRunner=HTMLTestRunner(
                      **kwargs))