import unittest
from selenium import webdriver
from google_page import GooglePage

class GoogleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path= './chromedriver/chromedriver')

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('youtube')

        self.assertEqual('youtube', google.keyword)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity= 2)