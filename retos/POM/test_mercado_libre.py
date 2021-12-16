import unittest
from selenium import webdriver
from mercado_libre_page import MercadoLibre
from time import sleep

class MercadolibreTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path= './chromedriver/chromedriver')
        cls.driver.maximize_window()

    def test_mercado_libre(self):
        mercl = MercadoLibre(self.driver)
        mercl.open()
        self.assertTrue(mercl.is_loaded)
        mercl.selected_country('Colombia')
        mercl.rid_pop_alert()
        mercl.search("playstation 4")
        mercl.choice_filter('Bogotá D.C.')
        mercl.choice_filter('Nuevo')
        mercl.choice_oder_by('Mayor precio')
        
        print(mercl.get_top_5_elements_result())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

