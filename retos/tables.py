import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Tables(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path= './chromedriver/chromedriver')
        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/tables')


    def test_sort_tables(self):
        driver = self.driver
        headers_number = 5
        rows_number = 4
        
        #Se crea una lista vacia donde se guardaran los datos
        # Son 5 columnas que nos interesan
        table_data = [[] for i in range (headers_number)]
        table_data_dic = {}
        print(table_data)

        for i in range(headers_number):
            #Se extrae los datos de los headers
            header = driver.find_element(By.XPATH,f'/html/body/div[2]/div/div/table[1]/thead/tr/th[{i + 1}]/span')
            #Manera de lista
            table_data[i].append(header.text)
            #Manera de diccionario
            table_data_dic[header.text] = []

            for j in range(rows_number):
                #Se recorre cada fila
                row_data = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/table[1]/tbody/tr[{j + 1}]/td[{i+ 1}]')
                #Manera de lista
                table_data[i].append(row_data.text)
                #Manera de diccionario con
                table_data_dic[header.text].append(row_data.text)

        print(table_data)
        print(table_data_dic)


    @classmethod
    def tearDown(cls):
        cls.driver.quit()

kwargs = {
    "output": 'tables-report'
}

if __name__ == '__main__':
    unittest.main(verbosity=2,
                  testRunner=HTMLTestRunner(
                      **kwargs))