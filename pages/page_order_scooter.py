from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from locators.locators1 import LocatorsCollector
import allure
from pages.base_page import BasePage

class PageOrder(BasePage):
    
    @allure.step("Метот заполняет поле имя")
    def input_name(self, name):
        self.send_keys(LocatorsCollector.input_name, name)
    
    @allure.step("Метот заполняет поле Фамилия")
    def input_last_name(self, last_name):
        self.send_keys(LocatorsCollector.input_last_name, last_name)
    
    @allure.step("Метот заполняет поле Адресс")
    def input_address(self, address):
        self.send_keys(LocatorsCollector.input_address, address)

    @allure.step('Метот заполняет поле метро')
    def input_metro(self, metro):
        self.click(LocatorsCollector.input_metro)
        self.click(LocatorsCollector.button_stancia)

    @allure.step('Метот заполняет поле Телефон')
    def input_number(self, number):
        self.send_keys(LocatorsCollector.input_number, number)
    
    @allure.step('Метот нажимает далие')
    def click_button_next(self):
        self.click(LocatorsCollector.button_next)

    @allure.step('Метот объединяет все что выше')
    def mix_komy(self, name, last_name, address, metro, number):
        self.input_name(name)
        self.input_last_name(last_name)
        self.input_address(address)
        self.input_metro(metro)
        self.input_number(number)
        self.click_button_next()

    @allure.step('Метот заполняет поле Когда привезти самокат')
    def input_order_time_now(self, time):
        self.send_keys(LocatorsCollector.input_order_time_now, time)
        self.click(LocatorsCollector.button_order_time_now)
    
    @allure.step('Метот заполняет поле * Срок аренды')
    def click_time_arend_day(self):
        self.click(LocatorsCollector.button_time_arend)
        self.click(LocatorsCollector.button_one_day)
    
    @allure.step('Метот заполняет поле Цвет самоката черный')
    def click_collor(self):
        self.click(LocatorsCollector.button_collor_black)
    
    @allure.step('Метот заполняет поле Комментарий для курьера')
    def input_commint(self, commint):
        self.send_keys(LocatorsCollector.input_commint, commint)
    
    @allure.step('Метот нажимает далие')    
    def click_button_zakazat(self):
        self.click(LocatorsCollector.button_zakazat)

    @allure.step('Метот объединяет 5 методов которые выше')   
    def mix_order(self, time, commint):
        self.input_order_time_now(time)
        self.click_time_arend_day()
        self.click_collor()
        self.input_commint(commint)
        self.click_button_zakazat()

    @allure.step('-')   
    def text_button_yes(self):
        return self.get_text(LocatorsCollector.button_yes)
    
    @allure.step('метот жмет на лого скутера')   
    def click_logo_scooters(self):
        self.click(LocatorsCollector.button_logo_scooter)
    
    @allure.step('метот жмет кнопку да')   
    def click_button_yes(self):
        self.click(LocatorsCollector.button_yes)
    
    @allure.step('метот определяет какой статус у заказа')   
    def text_order_good(self):
        return self.get_text(LocatorsCollector.good_complid_order)
    
    @allure.step('метот жмет на кнопку')   
    def click_look_order_status(self):
        self.click(LocatorsCollector.look_order_status)
    
    @allure.step('метот возврвщвет текущий юрл')  
    def active_url(self):
        return self.driver.current_url