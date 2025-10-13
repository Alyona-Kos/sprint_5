import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


def test_navigate_to_constructor_via_constructor_button(driver):
    """Переход по клику на «Конструктор» из личного кабинета"""
    
    # 1. Логинимся и переходим в личный кабинет
    driver.get("https://stellarburgers.education-services.ru/")
    
    email = 'alena_kostrikina_33@yandex.ru'
    password = 'kos12345'

    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_field))
    
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()
    
    # 2. Ждем успешного входа
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    
    # 3. Переходим в личный кабинет
    driver.find_element(*Locators.personal_account_button).click()
    
    # 4. Ждем загрузки личного кабинета
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.profile))
    
    # 5. Кликаем на "Конструктор" в шапке
    driver.find_element(*Locators.constructor_button_in_header).click()
    
    # 6. Проверяем что перешли в конструктор - видна кнопка "Оформить заказ"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    assert driver.find_element(*Locators.make_an_order_button).is_displayed()
    
    print("✅ Успешный переход в конструктор через кнопку 'Конструктор'")


def test_navigate_to_constructor_via_logo(driver):
    """Переход по клику на логотип Stellar Burgers из личного кабинета"""
    
    # 1. Логинимся и переходим в личный кабинет
    driver.get("https://stellarburgers.education-services.ru/")
    
    email = 'alena_kostrikina_33@yandex.ru'
    password = 'kos12345'

    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_field))
    
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()
    
    # 2. Ждем успешного входа
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    
    # 3. Переходим в личный кабинет
    driver.find_element(*Locators.personal_account_button).click()
    
    # 4. Ждем загрузки личного кабинета
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.profile))
    
    # 5. Кликаем на логотип в шапке
    driver.find_element(*Locators.logo).click()
    
    # 6. Проверяем что перешли в конструктор - видна кнопка "Оформить заказ"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    assert driver.find_element(*Locators.make_an_order_button).is_displayed()
    
    print("✅ Успешный переход в конструктор через логотип")