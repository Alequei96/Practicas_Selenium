import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from time import sleep

class AddRemoveElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='./chromedriver/chromedriver')
            
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()


    def test_add_remove(self):
        driver = self.driver
        elements_added = int(input('How many elements will you add?: '))
        elements_deleted = int(input('How many elements will you delete?: '))
        total_elements = elements_added-elements_deleted
        if total_elements < 0:
            print('You are trying to delete more elements than the existent')
            return

        add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')

        sleep(3)

        for i in range (elements_added):
            add_button.click()

        for i in range (elements_deleted):
            try:
                delete_button = driver.find_element(By.XPATH, '//*[@id="elements"]/button')
                delete_button.click()
            except:
                break

        if total_elements >0:
            print(f"There are {total_elements} elements on screen")

        sleep(4)
    
    def tearDown(self):
        driver = self.driver
        driver.quit()

kwargs = {
    "output": 'add_remove-report'
}

if __name__ == '__main__':
    unittest.main(verbosity=2,
                  testRunner=HTMLTestRunner(
                      **kwargs))