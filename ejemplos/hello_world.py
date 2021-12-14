import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    # Se prepara el entorno de la prueba
    #Se le pone el decorador para que hagan todas las pruebas en una sola ventana
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path= './chromedriver/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

    #Se llama test para que el programa lo execute
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org')

    #Se cierra la ventana del navegador
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ =='__main__':
    unittest.main(
        verbosity= 2, 
        testRunner= HTMLTestRunner(
        output= 'reportes', 
        report_name='hello-world-report'))