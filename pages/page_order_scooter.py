from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from locators.locators1 import LocatorsCollector

class PageOrder:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def input_name(self, name):
        self.driver.find_element(*LocatorsCollector.input_name).send_keys(name)
    
    def input_last_name(self, last_name):
        self.driver.find_element(*LocatorsCollector.input_last_name).send_keys(last_name)
    
    def input_address(self, address):
        self.driver.find_element(*LocatorsCollector.input_address).send_keys(address)

    def input_metro(self, metro):
        self.driver.find_element(*LocatorsCollector.input_metro).click()
        self.driver.find_element(*LocatorsCollector.button_stancia).click()

    def input_number(self, number):
        self.driver.find_element(*LocatorsCollector.input_number).send_keys(number)
    
    def click_button_next(self):
        self.driver.find_element(*LocatorsCollector.button_next).click()

    def mix_komy(self, name, last_name, address, metro, number):
        self.input_name(name)
        self.input_last_name(last_name)
        self.input_address(address)
        self.input_metro(metro)
        self.input_number(number)
        self.click_button_next()


    def input_order_time_now(self, time):
        self.driver.find_element(*LocatorsCollector.input_order_time_now).send_keys(time)
        self.driver.find_element(*LocatorsCollector.button_order_time_now).click()

    def click_time_arend_day(self):
        self.driver.find_element(*LocatorsCollector.button_time_arend).click()
        self.driver.find_element(*LocatorsCollector.button_one_day).click()

    def click_collor(self):
        self.driver.find_element(*LocatorsCollector.button_collor_black).click()
    
    def input_commint(self, commint):
        self.driver.find_element(*LocatorsCollector.input_commint).send_keys(commint)
    
    def click_button_zakazat(self):
        self.driver.find_element(*LocatorsCollector.button_zakazat).click()

    def mix_order(self, time, commint):
        self.input_order_time_now(time)
        self.click_time_arend_day()
        self.click_collor()
        self.input_commint(commint)
        self.click_button_zakazat()

    def text_button_yes(self):
        return self.driver.find_element(*LocatorsCollector.button_yes).text
    
    def click_logo_scooters(self):
        self.driver.find_element(*LocatorsCollector.button_logo_scooter).click()
    
    def click_button_yes(self):
        self.driver.find_element(*LocatorsCollector.button_yes).click()
    
    def text_order_good(self):
        return self.driver.find_element(*LocatorsCollector.good_complid_order).text
    
    def click_look_order_status(self):
        self.driver.find_element(*LocatorsCollector.look_order_status).click()
