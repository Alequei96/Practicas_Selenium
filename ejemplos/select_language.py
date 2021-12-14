import unittest
from selenium import webdriver
# Necesario para poder trabajar con dropdowns y listas de menus
from selenium.webdriver.support.ui import Select
from pyunitreport import HTMLTestRunner


class LanguageOptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='./chromedriver/chromedriver'
        )
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_select_language(self):
        expos_options = ['English', 'French', 'German']
        active_options = []

        select_language = Select(
            self.driver.find_element_by_id('select-language'))

        self.assertEqual(3, len(select_language.options))

        for option in select_language.options:
            active_options.append(option.text)

        # Se comparan las listas a ver si son iguales
        self.assertListEqual(expos_options, active_options)

        # Se checa si el primer lenguaje por default es el ingles en el menu
        self.assertEqual('English', select_language.first_selected_option.text)

        select_language.select_by_visible_text('German')

        self.assertTrue('store=german' in self.driver.current_url)

        select_language = Select(
            self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()

kwargs = {
    "output": 'language-report'
}

if __name__ == '__main__':
    unittest.main(verbosity=2,
                  testRunner=HTMLTestRunner(
                      **kwargs))
