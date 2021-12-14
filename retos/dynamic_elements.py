import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from time import sleep

class DynamicElements(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path= './chromedriver/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/disappearing_elements')

    def test_name_elements(self):
        driver = self.driver

        options =[]
        menu= 5
        tries = 1

        while len(options)< 5:

            options.clear()
            #Se itera sobre los objetos dinamicos 
            for i in range (menu):
                try:
                    #Se recorre cada uno de los objetos que puedan existir acorde al numero de vuelta del ciclo
                    option_name = driver.find_element(By.XPATH, f'//*[@id="content"]/div/ul/li[{i + 1}]/a')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"Option numbert {i +1} is NOT FOUND")
                    tries += 1
                    driver.refresh()

        print(f"Finished in {tries} tries")
    
    @classmethod
    def tearDown(cls):
        cls.driver.quit()

kwargs = {
    "output": 'dynamic_elements-report'
}

if __name__ == '__main__':
    unittest.main(verbosity=2,
                  testRunner=HTMLTestRunner(
                      **kwargs))