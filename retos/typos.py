import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Typos(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path= './chromedriver/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/typos')


    def test_find_typo(self):
        driver = self.driver
        paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '.example > p:nth-child(3)')
        text_to_check = paragraph_to_check.text
        correct_paragraph = "Sometimes you'll see a typo, other times you won't."
        print(paragraph_to_check.text)
        print(correct_paragraph)

        if text_to_check == correct_paragraph:
            flag = True
        else:
            flag = False

        tries = 1
        

        while  flag == False:
            try:
                self.assertEqual(text_to_check, correct_paragraph)
                if text_to_check == correct_paragraph:
                    flag = True
                    tries += 1
                driver.refresh()

            except:
                print('Son diferentes')
                tries += 1
                paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '.example > p:nth-child(3)')
                text_to_check = paragraph_to_check.text
                driver.refresh()
                
        self.assertEqual(flag, True)
        if tries > 1:
            print(f"Se logro en {tries} intentos")
        else:
            print(f"Se logro en {tries} intento")

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

kwargs = {
    "output": 'typos-report'
}

if __name__ == '__main__':
    unittest.main(verbosity=2,
                  testRunner=HTMLTestRunner(
                      **kwargs))