from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from locators.locators1 import LocatorsCollector
from locators.data import AuthData
import allure
from pages.base_page import BasePage

class HomePage(BasePage):

    @allure.step('Метот нажинает на стрелочку')
    def click_button(self, button_id):
        locator = (By.XPATH, f"//div[@id='accordion__heading-{button_id}']")
        self.click(locator)

    @allure.step('Метот возвращает текст активной стрелочки')
    def get_text_use_button(self, button_id):
        locator = (By.XPATH, f"//div[@id='accordion__panel-{button_id}']")
        return self.get_text(locator)

    @allure.step('Метот закрывает куки')
    def close_cooki(self):
        self.click(LocatorsCollector.button_close_cooki)
    
    @allure.step('Обедененный метот нажатия и вовращения активного текста ')
    def mix(self, button_id):
        self.click_button(button_id)
        return self.get_text_use_button(button_id)

    @allure.step('Метот нажимает на ввернию кнопку заказать')
    def click_button_zakaz_up(self):
        self.click(LocatorsCollector.button_zakaz_up)
    
    @allure.step('Метот нажимает на нижнию кнопку заказать')
    def click_button_zakaz_down(self):
        self.click(LocatorsCollector.button_zakaz_down)
    
    @allure.step('Метот нажимает на Лого яндекса')
    def click_logo_yndex(self):
        self.click(LocatorsCollector.button_logo_yndex)