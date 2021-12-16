from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Se hace el objeto MercadoLibre el cual se inicializa

class MercadoLibre(object):
    def __init__(self, driver):
        self._driver = driver
        self._url = 'https://mercadolibre.com'
        self.search_country = 'CO'
        self.search_bar = 'cb1-edit'

    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.ID, self.search_country)) 
            or 
            EC.presence_of_element_located((By.CLASS_NAME, '#CO'))
            )
        return True

    @property
    def keyword(self):
        input_field = self._driver.find_element(By.ID, self.search_bar)
        return input_field.get_attribute('value')

    def open(self):
        self._driver.get(self._url)

    def rid_pop_alert(self):
        button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.ID, 'newCookieDisclaimerButton')))
        button.click()

    def type_search(self,keyword):
        input_field = self._driver.find_element(By.ID, self.search_bar)
        input_field.send_keys(keyword)

    def click_submit(self):
        input_field = self._driver.find_element(By.ID, self.search_bar)
        input_field.submit()

    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()

    def order_data(self,elements):
        data ={}
        for element in elements:
            data[element.text.lower()] = element
        return data
    
    def get_countries(self):
        countries = self._driver.find_elements(By.CSS_SELECTOR, '.ml-site-link')
        return self.order_data(countries)

    def selected_country(self,country):
        country_item = self.get_countries()[country.lower()] 
        country_item.click()

    def get_filters(self):
        filters = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_any_elements_located((By.CLASS_NAME, 'ui-search-filter-name')))
        return self.order_data(filters)

    def choice_filter(self,keyword):
        filter_item =self.get_filters()[keyword.lower()].click()

    def get_orders(self):
        list_buttom = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.andes-dropdown__trigger'))
        )
        list_buttom.click()
        orders = self._driver.find_elements(By.CLASS_NAME, 'andes-list__item-primary')
        return self.order_data(orders)

    def choice_oder_by(self,keyword):
        self.get_orders()[keyword.lower()].click()

    def get_top_5_elements_result(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ui-search-layout__item')))
        products = {}
        for i in range(5):
            article_name = self._driver.find_element(By.XPATH,f'/html/body/main/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2').text
            price = self._driver.find_element(By.XPATH,f'/html/body/main/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/span[1]/span[2]/span[2]').text

            products[article_name]=price

        return products