import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class DynamicControls(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path= './chromedriver/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/dynamic_controls')
        sleep(2)

    def test_dynamic_controls(self):
        driver = self.driver
        #Se puede seleccionar por el xpath o por el selector ccs
        #check_box = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/form[1]/div/input').click()
        check_box = driver.find_element(By.CSS_SELECTOR, 'html.no-js body div.row div#content.large-12.columns div.example form#checkbox-example div#checkbox input')
        check_box.click()
        

        #remove_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/form[1]/button').click()
        remove_button = driver.find_element(By.CSS_SELECTOR, 'html.no-js body div.row div#content.large-12.columns div.example form#checkbox-example button')
        remove_button.click()
        

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'html.no-js body div.row div#content.large-12.columns div.example form#checkbox-example button'))).click()
        remove_button.click()
    
        enable_disable_button = driver.find_element(By.CSS_SELECTOR, 'html.no-js body div.row div#content.large-12.columns div.example form#input-example button')
        enable_disable_button.click()

        text_field = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'html.no-js body div.row div#content.large-12.columns div.example form#input-example input')))
        text_field.send_keys("Niceeee")

        enable_disable_button.click()
        
    @classmethod
    def tearDown(cls):
        cls.driver.quit()

kwargs = {
    "output": 'dynamic_controls-report'
}

if __name__ == '__main__':
    unittest.main(verbosity=2,
                  testRunner=HTMLTestRunner(
                      **kwargs))