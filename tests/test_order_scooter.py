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
import allure

@pytest.mark.usefixtures("browser")
class Testbookscollector2:
    @allure.step('Тестирование формы регистрации заказа скутера через ввернию кнопку заказа ')
    def test_page_order_scooter_up(self, browser, setup_classes):
        home_page, home_order = setup_classes

        home_page.click_button_zakaz_up()
        home_order.mix_komy(AuthData.name, AuthData.last_name, AuthData.address, AuthData.metro, AuthData.number)
        home_order.mix_order(AuthData.time, AuthData.commint)

        home_order.click_button_yes()
        element = home_order.text_order_good()
        assert 'Заказ оформлен' in element


    @allure.step('Тестирование формы регистрации заказа скутера через нижнию кнопку заказа ')
    def test_page_order_scooter_down(self, browser, setup_classes):
        browser.get(UrlCollector.url_home)
        home_page, home_order = setup_classes

        home_page.click_button_zakaz_up()
        home_order.mix_komy(AuthData.name1, AuthData.last_name1, AuthData.address1, AuthData.metro1, AuthData.number1)
        home_order.mix_order(AuthData.time1, AuthData.commint1)

        home_order.click_button_yes()
        element = home_order.text_order_good()
        assert 'Заказ оформлен' in element

    @allure.step('Тестирование перехода по логотипу скутера')
    def test_logo_scooter(self, browser, setup_classes):
        browser.get(UrlCollector.url_home)
        home_page, home_order = setup_classes
        home_order.click_logo_scooters()
        assert home_order.active_url() == UrlCollector.url_home

    @allure.step('Тестирование перехода по яндекса')
    def test_logo_yndex(self, browser, setup_classes):
        browser.get(UrlCollector.url_home)
        home_page, home_order = setup_classes
        home_page.click_logo_yndex()
        browser.switch_to.window(browser.window_handles[-1])
        WebDriverWait(browser, 10).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in home_order.active_url()