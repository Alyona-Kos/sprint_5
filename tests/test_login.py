import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.urls import Urls
from config.credentials import Credentials
from config.locators import Locators


def test_login_via_button_on_main_page(driver):
    """Вход по кнопке «Войти в аккаунт» на главной странице."""
    driver.get(Urls.BASE_URL)
    
    driver.find_element(*Locators.login_button_main_page).click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_field))
    driver.find_element(*Locators.email_field).send_keys(Credentials.EXISTING_USER_EMAIL)
    driver.find_element(*Locators.password_field).send_keys(Credentials.EXISTING_USER_PASSWORD)
    driver.find_element(*Locators.login_button).click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    assert driver.find_element(*Locators.make_an_order_button).is_displayed()


def test_login_via_personal_account(driver):
    """Вход через кнопку «Личный кабинет»."""
    driver.get(Urls.BASE_URL)
    
    driver.find_element(*Locators.personal_account_button).click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_field))
    driver.find_element(*Locators.email_field).send_keys(Credentials.EXISTING_USER_EMAIL)
    driver.find_element(*Locators.password_field).send_keys(Credentials.EXISTING_USER_PASSWORD)
    driver.find_element(*Locators.login_button).click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    assert driver.find_element(*Locators.make_an_order_button).is_displayed()


def test_login_via_registration_form_button(driver):
    """Вход через кнопку в форме регистрации."""
    driver.get(Urls.BASE_URL)
    
    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.register_link))
    driver.find_element(*Locators.register_link).click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.submit_button))
    driver.find_element(*Locators.login_button_in_registration_form).click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_field))
    driver.find_element(*Locators.email_field).send_keys(Credentials.EXISTING_USER_EMAIL)
    driver.find_element(*Locators.password_field).send_keys(Credentials.EXISTING_USER_PASSWORD)
    driver.find_element(*Locators.login_button).click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    assert driver.find_element(*Locators.make_an_order_button).is_displayed()


def test_login_via_password_recovery_button(driver):
    """Вход через кнопку в форме восстановления пароля."""
    driver.get(Urls.BASE_URL)
    
    driver.find_element(*Locators.personal_account_button).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.forgot_password_button))
    driver.find_element(*Locators.forgot_password_button).click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.login_password_recovery_form_button))
    driver.find_element(*Locators.login_password_recovery_form_button).click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_field))
    driver.find_element(*Locators.email_field).send_keys(Credentials.EXISTING_USER_EMAIL)
    driver.find_element(*Locators.password_field).send_keys(Credentials.EXISTING_USER_PASSWORD)
    driver.find_element(*Locators.login_button).click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    assert driver.find_element(*Locators.make_an_order_button).is_displayed()