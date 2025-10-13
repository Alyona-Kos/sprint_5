import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


def test_navigate_to_personal_account(driver):
    """Тест перехода в личный кабинет"""
    
    # Исправляем URL на правильный
    driver.get("https://stellarburgers.education-services.ru/")

    # Исправляем email и пароль на правильные
    email = 'alena_kostrikina_33@yandex.ru'
    password = 'kos12345'

    # Логинимся
    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_field))
    
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()
    
    # Ждем успешного входа
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    
    # Переходим в личный кабинет
    driver.find_element(*Locators.personal_account_button).click()
    
    # Ждем загрузки личного кабинета
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.profile))
    
    # Проверяем что в личном кабинете - видна история заказов
    assert driver.find_element(*Locators.order_history).is_displayed()
    print("✅ Переход в личный кабинет - УСПЕХ")