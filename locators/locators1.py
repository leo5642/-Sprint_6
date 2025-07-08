from selenium.webdriver.common.by import By
import pytest

class LocatorsCollector:
    button_text = [
    (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ]


    button_zakaz_up = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[2]/button[1]")
    button_zakaz_down = (By.XPATH, "//*[@id='root']/div/div/div[4]/div[2]/div[5]/button")

    input_name = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/input")
    input_last_name = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/input")
    input_address = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[3]/input")
    input_number = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[5]/input")
    input_metro = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[4]/div/div/input")
    button_stancia = (By.CLASS_NAME, 'select-search__select')
    button_next = (By.XPATH, "//*[@id='root']/div/div[2]/div[3]/button")
    button_logo_scooter = (By.XPATH, "/html/body/div/div/div[1]/div[1]/a[2]")
    button_logo_yndex = (By.XPATH, "//*[@id='root']/div/div/div[1]/div[1]/a[1]")

    input_order_time_now = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[1]/div/input")
    button_order_time_now =(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]")
    button_time_arend = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div[1]/div[1]")
    button_one_day = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div[2]/div[1]")
    button_collor_black = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[3]/label[1]")
    input_commint = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[4]/input")
    button_zakazat = (By.XPATH, "//*[@id='root']/div/div[2]/div[3]/button[2]")

    button_yes = (By.XPATH, "//*[@id='root']/div/div[2]/div[5]/div[2]/button[2]")
    good_complid_order = (By.XPATH, "/html/body/div/div/div[2]/div[5]/div[1]")
    look_order_status = (By.XPATH, "/html/body/div/div/div[2]/div[5]/div[2]/button")