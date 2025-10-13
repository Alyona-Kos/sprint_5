import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


# Переход из раздела "Булки" в раздел "Начинки"
def test_navigate_buns_to_fillings(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    # Используем те же учетные данные что и в других тестах
    email = 'alena_kostrikina_33@yandex.ru'
    password = 'kos12345'

    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_field))
    
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()
    
    # Ждем успешного входа
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    
    # Переходим в раздел "Начинки"
    driver.find_element(*Locators.fillings_section).click()
    
    # Проверяем что активен раздел "Начинки"
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.selected_section, "Начинки"))
    assert driver.find_element(*Locators.selected_section).text == "Начинки"
    
    print("✅ Успешный переход из Булок в Начинки")


# Переход из раздела "Начинки" в раздел "Соусы"
def test_navigate_fillings_to_sauces(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    email = 'alena_kostrikina_33@yandex.ru'
    password = 'kos12345'

    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_field))
    
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()
    
    # Ждем успешного входа
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    
    # Переходим в раздел "Начинки"
    driver.find_element(*Locators.fillings_section).click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.selected_section, "Начинки"))
    
    # Переходим в раздел "Соусы"
    driver.find_element(*Locators.sauces_section).click()
    
    # Проверяем что активен раздел "Соусы"
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.selected_section, "Соусы"))
    assert driver.find_element(*Locators.selected_section).text == "Соусы"
    
    print("✅ Успешный переход из Начинок в Соусы")


# Переход из раздела "Соусы" в раздел "Булки"
def test_navigate_sauces_to_buns(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    email = 'alena_kostrikina_33@yandex.ru'
    password = 'kos12345'

    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_field))
    
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()
    
    # Ждем успешного входа
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    
    # Переходим в раздел "Соусы"
    driver.find_element(*Locators.sauces_section).click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.selected_section, "Соусы"))
    
    # Переходим в раздел "Булки"
    driver.find_element(*Locators.buns_section).click()
    
    # Проверяем что активен раздел "Булки"
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(Locators.selected_section, "Булки"))
    assert driver.find_element(*Locators.selected_section).text == "Булки"
    
    print("✅ Успешный переход из Соусов в Булки")