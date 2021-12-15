import csv, unittest
from selenium import webdriver
from ddt import ddt, data, unpack
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By

def get_data(file_name):
    rows = []
    data_file = open(file_name, 'r')
    reader = csv.reader(data_file)
    next(reader, None)

    for row in reader:
        rows.append(row)
    return rows


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
    @data(*get_data('./files/testdata.csv'))
    @unpack #Se van a desempaquetar las tuplas de arriba 

    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        #Ya que son varios objetos dentro de la clase product-name se pone dentro de corchetes
        products = driver.find_elements(By.XPATH, '//h2[@class="product-name"]/a')

        expected_count = int(expected_count)

        if expected_count >0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element(By.CLASS_NAME , 'note-msg')
            self.assertEqual('Your search returns no results', message)

        print(f'Found {len(products)} products')


    @classmethod
    def tearDown(cls):
        cls.driver.close()

kwargs = {
    "output": 'ddt_csv-report'
}

if __name__ == '__main__':
    unittest.main(verbosity=2,
                  testRunner=HTMLTestRunner(
                      **kwargs))