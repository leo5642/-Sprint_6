import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()