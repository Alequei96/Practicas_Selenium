import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class SearchTests(unittest.TestCase):
    # Se prepara el entorno de la prueba
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path= './chromedriver/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        #Limpia el campo de busqueda si es que tiene texto
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('salt shaker')
        search_field.submit()

        #Se selecciona el href="" para el xpath
        products = driver.find_elements_by_xpath('//*[@id="product-collection-image-389"]')
        self.assertEqual(1, len(products))



    #Se cierra la ventana del navegador
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ =='__main__':
    unittest.main(
        verbosity= 2, 
        testRunner= HTMLTestRunner(
        output= 'reportes', 
        report_name='ejemplostest'))