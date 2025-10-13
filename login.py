import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver

# Вход по кнопке «Войти в аккаунт» 
def test_login_via_button_on_main_page(driver):
    driver.get("https://stellarburgers.education-services.ru")

    email = 'alena_kostrikina_33@yandex.ru'
    password = 'kos12345'

    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.register_link))
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators. login_button).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    assert driver.find_element(*Locators.make_an_order_button).is_displayed()

# Вход через кнопку «Личный кабинет»
def test_login_via_personal_account(driver):
    driver.get("https://stellarburgers.education-services.ru")

    email = 'alena_kostrikina_33@yandex.ru'
    password = 'kos12345'

    driver.find_element(*Locators.personal_account_button).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.register_link))
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    assert driver.find_element(*Locators.make_an_order_button).is_displayed()

# Вход через кнопку в форме регистрации
def test_login_via_registration_form_button(driver):
    driver.get("https://stellarburgers.education-services.ru")

    email = 'alena_kostrikina_33@yandex.ru'
    password = 'kos12345'

    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.register_link))
    driver.find_element(*Locators.register_link).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.submit_button))
    driver.find_element(*Locators.login_button_in_registration_form).click()
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    assert driver.find_element(*Locators.make_an_order_button).is_displayed()

# Вход через кнопку в форме восстановления пароля
def test_login_via_password_recovery_button(driver):
    driver.get("https://stellarburgers.education-services.ru")

    email = 'alena_kostrikina_33@yandex.ru'
    password = 'kos12345'

    driver.find_element(*Locators.personal_account_button).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.register_link))
    driver.find_element(*Locators.forgot_password_button).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.login_password_recovery_form_button))
    driver.find_element(*Locators.login_password_recovery_form_button).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.login_button))
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    assert driver.find_element(*Locators.make_an_order_button).is_displayed()

