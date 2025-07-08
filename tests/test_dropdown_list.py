from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from pages.page_home import HomePage
from locators.locators1 import LocatorsCollector

class Testbookscollector1:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')

        home_page = HomePage(cls.driver)
        home_page.close_cooki()
    @pytest.mark.parametrize("locator, text_use_button", LocatorsCollector.button_text)
    def test_page(self, locator, text_use_button):
        home_page = HomePage(self.driver)
        actual_text = home_page.mix(locator)
        assert actual_text == text_use_button
        home_page.click_logo_scooters()
        

    @classmethod
    def teardown_class(cls):
        if cls.driver:
            cls.driver.quit()
