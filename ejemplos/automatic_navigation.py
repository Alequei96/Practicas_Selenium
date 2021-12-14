import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner


class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='./chromedriver/chromedriver'
        )
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get('http://google.com/')

    def test_browser_navigation(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('youtube')
        search_field.submit()

        driver.back()
        driver.forward()
        driver.refresh()


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()

kwargs = {
    "output": 'browser-report'
}

if __name__ == '__main__':
    unittest.main(verbosity=2,
                  testRunner=HTMLTestRunner(
                      **kwargs))
