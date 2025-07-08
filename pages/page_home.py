from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from locators.locators1 import LocatorsCollector
from locators.data import AuthData

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def click_button(self, button_id):
        self.driver.find_element(By.XPATH, f"//div[@id='accordion__heading-{button_id}']").click()

    def get_text_use_button(self, button_id):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//div[@id='accordion__panel-{button_id}']")
            )
        )
        return element.text


    def close_cooki(self):
        self.driver.find_element(By.CLASS_NAME, "App_CookieButton__3cvqF").click()
        
    def mix(self, button_id):
        self.click_button(button_id)
        return self.get_text_use_button(button_id)
    
    def click_button_zakaz_up(self):
        self.driver.find_element(*LocatorsCollector.button_zakaz_up).click()
    
    def click_button_zakaz_down(self):
        self.driver.find_element(*LocatorsCollector.button_zakaz_down).click()
    
    def click_logo_yndex(self):
        self.driver.find_element(*LocatorsCollector.button_logo_yndex).click()