from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from pages.page_home import HomePage
from locators.locators1 import LocatorsCollector
from locators.url import UrlCollector
from pages.page_order_scooter import PageOrder
import allure

@pytest.mark.usefixtures("browser")
class Testbookscollector1:
    @allure.title('Использование парометреции в тесте')
    @pytest.mark.parametrize("locator, expected_text", LocatorsCollector.button_text)
    def test_accordion_items(self, browser, setup_classes, locator, expected_text):
        home_page, home_order = setup_classes
        actual_text = home_page.mix(locator)
        assert actual_text == expected_text
