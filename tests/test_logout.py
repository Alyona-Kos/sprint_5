import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

# Добавляем путь к корневой директории для импорта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.urls import Urls
from config.locators import Locators


def test_logout(driver):
    """Тест выхода из аккаунта"""
    
    # 1. Открываем главную страницу (используем константу из Urls)
    driver.get(Urls.BASE_URL)

    # 2. Данные для входа
    email = 'alena_kostrikina_33@yandex.ru'
    password = 'kos12345'

    # 3. Логинимся
    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_field))
    
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()
    
    # 4. Ждем успешного входа
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    
    # 5. Переходим в личный кабинет
    driver.find_element(*Locators.personal_account_button).click()
    
    # 6. Ждем загрузки личного кабинета
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.profile))
    
    # 7. Выполняем выход
    driver.find_element(*Locators.logout_button).click()
    
    # 8. Проверяем что вышли - видна кнопка входа
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.login_button))
    assert driver.find_element(*Locators.login_button).is_displayed()