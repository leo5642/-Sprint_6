from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from pages.page_home import HomePage
from locators.locators1 import LocatorsCollector
from pages.page_order_scooter import PageOrder
from locators.url import UrlCollector
from locators.data import AuthData


class Testbookscollector2:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(UrlCollector.url_home)


    def test_page_order_scooter(self):
        home_page = HomePage(self.driver)
        home_order = PageOrder(self.driver)
        home_page.click_button_zakaz_up()
        home_order.mix_komy(AuthData.name, AuthData.last_name, AuthData.address, AuthData.metro, AuthData.number)
        home_order.mix_order(AuthData.time, AuthData.commint)

        home_order.click_button_yes()
        element = home_order.text_order_good()
        assert 'Заказ оформлен' in element
        home_order.click_look_order_status()

        home_order.click_logo_scooters()
        assert self.driver.current_url == UrlCollector.url_home

        home_page.click_logo_yndex()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in self.driver.current_url.lower()
        self.driver.quit()


    def test_page_order_scooter_down(self):
        self.driver = webdriver.Firefox()
        self.driver.get(UrlCollector.url_home)

        home_page = HomePage(self.driver)
        home_order = PageOrder(self.driver)
        home_page.close_cooki()
        home_page.click_button_zakaz_down()
        home_order.mix_komy(AuthData.name1, AuthData.last_name1, AuthData.address1, AuthData.metro1, AuthData.number1)
        home_order.mix_order(AuthData.time1, AuthData.commint1)

        home_order.click_button_yes()
        element = home_order.text_order_good()
        assert 'Заказ оформлен' in element
        home_order.click_look_order_status()

        home_order.click_logo_scooters()
        assert self.driver.current_url == UrlCollector.url_home

        home_page.click_logo_yndex()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in self.driver.current_url.lower()

        self.driver.quit()



    @classmethod
    def teardown_class(cls):
        if cls.driver:
            cls.driver.quit()
