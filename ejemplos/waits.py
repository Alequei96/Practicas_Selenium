import unittest

from selenium import webdriver
#Para interactuar con los elementos de la página através de los selectores
from selenium.webdriver.common.by import By
#Nos permite utilizar las expected_conditions junto con las esperas implicitas
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyunitreport import HTMLTestRunner

class ExplicitWaitTests(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(
            executable_path='./chromedriver/chromedriver'
        )
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_account_link(self):
        WebDriverWait(self.driver,10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')

        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()


    def test_create_new_costumer(self):
        self.driver.find_element_by_link_text('ACCOUNT').click()

        my_account = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        create_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_button.click()

        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))

    @classmethod
    def tearDown(cls):
        cls.driver.implicitly_wait(3)
        cls.driver.quit()

kwargs = {
    "output": 'waits-report'
}

if __name__ == '__main__':
    unittest.main(verbosity=2,
                  testRunner=HTMLTestRunner(
                      **kwargs))
