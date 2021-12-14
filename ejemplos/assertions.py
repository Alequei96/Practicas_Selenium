import unittest
from selenium import webdriver
#Sirve como excepcion para los assertions cuando queremos
#validar la presencia de un elemento
from selenium.common.exceptions import NoSuchElementException
#Ayuda a llamar a las excepciones que queremos validar
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

class AssertionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path= './chromedriver/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_filed(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    #Se cierra la ventana del navegador
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    #Para saber si esta presente el elemento
    #How: tipo de selector
    #What: El valor que tiene
    def is_element_present(self,how,what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__ =='__main__':
    unittest.main(
        verbosity= 2, 
        testRunner= HTMLTestRunner(
        output= 'reportes', 
        report_name='assertiontest'))