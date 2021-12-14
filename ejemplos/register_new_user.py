import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='./chromedriver/chromedriver'
        )
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()

        create_account_button = driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span')

        # Nos aseguramos si el boton es visible y se puede interactuar con el
        self.assertTrue(create_account_button.is_displayed()
                        and create_account_button.is_enabled())
        create_account_button.click()

        # Corroboramos si estamos en la pesta;a correcta checando el titulo
        self.assertEqual('Create New Customer Account', driver.title)

        # Ubica los campos a llenar
        first_name = driver.find_element_by_id('firstname')
        driver.implicitly_wait(1)
        middle_name = driver.find_element_by_id('middlename')
        driver.implicitly_wait(1)
        last_name = driver.find_element_by_id('lastname')
        driver.implicitly_wait(1)
        email_address = driver.find_element_by_id('email_address')
        driver.implicitly_wait(1)
        password = driver.find_element_by_id('password')
        driver.implicitly_wait(1)
        confirm_password = driver.find_element_by_id('confirmation')
        driver.implicitly_wait(1)
        submit_button = driver.find_element_by_xpath(
            '//*[@id="form-validate"]/div[2]/button/span/span')

        # Se asegura que los campos esten habilitados para poder interactuar con ellos
        self.assertTrue(first_name.is_enabled()
                        and middle_name.is_enabled()
                        and last_name.is_enabled()
                        and email_address.is_enabled()
                        and password.is_enabled()
                        and confirm_password.is_enabled()
                        and submit_button.is_enabled())

        # Escribe Test en todos los campos posibles
        first_name.send_keys('Test')
        middle_name.send_keys('Test')
        last_name.send_keys('Test')
        email_address.send_keys('Test@testingmail.com')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        submit_button.click()

    def tearDown(self):
        self.driver.quit()


kwargs = {
    "output": 'register_user-report'
}

if __name__ == '__main__':
    unittest.main(verbosity=2,
                  testRunner=HTMLTestRunner(
                      **kwargs))
