import pytest
import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Добавляем путь к корневой директории для импорта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.urls import Urls
from config.credentials import Credentials
from config.locators import Locators


def test_navigate_buns_to_fillings(driver):
    """Переход из раздела 'Булки' в раздел 'Начинки'."""
    # Открываем главную страницу
    driver.get(Urls.BASE_URL)
    
    # Логинимся
    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_field))
    driver.find_element(*Locators.email_field).send_keys(Credentials.EXISTING_USER_EMAIL)
    driver.find_element(*Locators.password_field).send_keys(Credentials.EXISTING_USER_PASSWORD)
    driver.find_element(*Locators.login_button).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    
    # Переходим в раздел "Начинки"
    driver.find_element(*Locators.fillings_section).click()
    
    # Проверяем что активен раздел "Начинки"
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(Locators.selected_section, "Начинки")
    )
    actual_text = driver.find_element(*Locators.selected_section).text
    assert actual_text == "Начинки", f"Ожидался раздел 'Начинки', но активен '{actual_text}'"


def test_navigate_fillings_to_sauces(driver):
    """Переход из раздела 'Начинки' в раздел 'Соусы'."""
    # Открываем главную страницу
    driver.get(Urls.BASE_URL)
    
    # Логинимся
    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_field))
    driver.find_element(*Locators.email_field).send_keys(Credentials.EXISTING_USER_EMAIL)
    driver.find_element(*Locators.password_field).send_keys(Credentials.EXISTING_USER_PASSWORD)
    driver.find_element(*Locators.login_button).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    
    # Переходим в раздел "Начинки"
    driver.find_element(*Locators.fillings_section).click()
    
    # Проверяем что активен раздел "Начинки"
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(Locators.selected_section, "Начинки")
    )
    actual_text = driver.find_element(*Locators.selected_section).text
    assert actual_text == "Начинки", f"Ожидался раздел 'Начинки', но активен '{actual_text}'"
    
    # Переходим в раздел "Соусы"
    driver.find_element(*Locators.sauces_section).click()
    
    # Проверяем что активен раздел "Соусы"
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(Locators.selected_section, "Соусы")
    )
    actual_text = driver.find_element(*Locators.selected_section).text
    assert actual_text == "Соусы", f"Ожидался раздел 'Соусы', но активен '{actual_text}'"


def test_navigate_sauces_to_buns(driver):
    """Переход из раздела 'Соусы' в раздел 'Булки'."""
    # Открываем главную страницу
    driver.get(Urls.BASE_URL)
    
    # Логинимся
    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_field))
    driver.find_element(*Locators.email_field).send_keys(Credentials.EXISTING_USER_EMAIL)
    driver.find_element(*Locators.password_field).send_keys(Credentials.EXISTING_USER_PASSWORD)
    driver.find_element(*Locators.login_button).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    
    # Переходим в раздел "Соусы"
    driver.find_element(*Locators.sauces_section).click()
    
    # Проверяем что активен раздел "Соусы"
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(Locators.selected_section, "Соусы")
    )
    actual_text = driver.find_element(*Locators.selected_section).text
    assert actual_text == "Соусы", f"Ожидался раздел 'Соусы', но активен '{actual_text}'"
    
    # Переходим в раздел "Булки"
    driver.find_element(*Locators.buns_section).click()
    
    # Проверяем что активен раздел "Булки"
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(Locators.selected_section, "Булки")
    )
    actual_text = driver.find_element(*Locators.selected_section).text
    assert actual_text == "Булки", f"Ожидался раздел 'Булки', но активен '{actual_text}'"