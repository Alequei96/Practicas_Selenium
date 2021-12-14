import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HomePageTests(unittest.TestCase):
    # Se prepara el entorno de la prueba
    #Se le pone el decorador para que hagan todas las pruebas en una sola ventana
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path= './chromedriver/chromedriver')
        driver = cls.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    #Se llama test para que el programa lo execute
    def test_search_text_field(self):
        #Siempre que se indique un valor atributo se debe poner comillas
        search_field = self.driver.find_element_by_id("search")

    def test_search_text_field_by_name(self):
        #Siempre que se indique un valor atributo se debe poner comillas
        search_field = self.driver.find_element_by_name("q")

    def test_search_text_field_by_class_name(self):
        #Siempre que se indique un valor atributo se debe poner comillas
        search_field = self.driver.find_element_by_class_name("input-text")

    def test_search_button_enabled(self):
        #Siempre que se indique un valor atributo se debe poner comillas
        button = self.driver.find_element_by_class_name("button")

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners))

    #Cuando se buscan imagenes se puede buscar por el XPATH
    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')
      
    #Se busca un elemento <div class="header-minicart" <span class="icon"></span></div>
    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector('div.header-minicart span.icon')

    #Se cierra la ventana del navegador
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ =='__main__':
    unittest.main(
        verbosity= 2, 
        testRunner= HTMLTestRunner(
        output= 'reportes', 
        report_name='ejemplostest'))