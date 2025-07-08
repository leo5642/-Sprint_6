from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.page_home import HomePage
from locators.locators1 import LocatorsCollector
import pytest
from locators.data import AuthData




driver = webdriver.Firefox()
driver.get('https://qa-scooter.praktikum-services.ru/')
# driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div[2]/button[1]").click()
home_page = HomePage(driver)
home_page.click_button_zakaz_up()









# driver.find_element(By.XPATH, "//div[@id='accordion__heading-0']").click()
# element = driver.find_element(By.XPATH, "//div[@id='accordion__panel-0']")
# print(element.text)
    
# driver.quit()



# driver = webdriver.Firefox()
# driver.get("https://qa-scooter.praktikum-services.ru/")
# coyc_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='accordion__heading-1']")))
# driver.find_element(By.CLASS_NAME, "App_CookieButton__3cvqF").click()
# coyc_button.click()


# driver.quit()    
        

    # def get_description(self):
    #     return self.driver.find_element(*self.profile_description).text
