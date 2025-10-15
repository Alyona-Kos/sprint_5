import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data_randomizer import generate_name, generate_email, generate_password, generate_incorrect_password
from config.urls import Urls
from config.locators import Locators


def test_registration_positive(driver):
    """Позитивная проверка регистрации."""
    driver.get(Urls.BASE_URL)

    user_name = generate_name()
    user_email = generate_email()
    user_password = generate_password()

    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.register_link))
    driver.find_element(*Locators.register_link).click()

    WebDriverWait(driver, 10).until(EC.url_contains("/register"))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.submit_button))

    driver.find_element(*Locators.name_field).send_keys(user_name)
    driver.find_element(*Locators.email_field_register).send_keys(user_email)
    driver.find_element(*Locators.password_field_register).send_keys(user_password)

    driver.find_element(*Locators.submit_button).click()

    WebDriverWait(driver, 20).until(EC.url_to_be(Urls.LOGIN_URL))
    current_url = driver.current_url

    assert current_url == Urls.LOGIN_URL


def test_registration_incorrect_password_message(driver):
    """Регистрация с невалидным паролем."""
    driver.get(Urls.BASE_URL)
    user_name = generate_name()
    user_email = generate_email()
    user_password = generate_incorrect_password()

    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.register_link))
    driver.find_element(*Locators.register_link).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.submit_button))

    driver.find_element(*Locators.name_field).send_keys(user_name)
    driver.find_element(*Locators.email_field_register).send_keys(user_email)
    driver.find_element(*Locators.password_field_register).send_keys(user_password)
    driver.find_element(*Locators.submit_button).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.incorrect_password_message))
    assert driver.find_element(*Locators.incorrect_password_message).is_displayed()


def test_registration_empty_name_error(driver):
    """Регистрация с пустым именем."""
    driver.get(Urls.BASE_URL)
    user_email = generate_email()
    user_password = generate_password()

    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.register_link))
    driver.find_element(*Locators.register_link).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.submit_button))

    driver.find_element(*Locators.email_field_register).send_keys(user_email)
    driver.find_element(*Locators.password_field_register).send_keys(user_password)
    driver.find_element(*Locators.submit_button).click()

    assert "register" in driver.current_url


@pytest.mark.parametrize('invalid_email', ['invalid', 'test@', '@domain.com', 'test@domain', '123@ya.'])
def test_registration_invalid_email_error(driver, invalid_email):
    """Регистрация с некорректным email."""
    driver.get(Urls.BASE_URL)
    user_name = generate_name()
    user_password = generate_password()

    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.register_link))
    driver.find_element(*Locators.register_link).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.submit_button))

    driver.find_element(*Locators.name_field).send_keys(user_name)
    driver.find_element(*Locators.email_field_register).send_keys(invalid_email)
    driver.find_element(*Locators.password_field_register).send_keys(user_password)
    driver.find_element(*Locators.submit_button).click()

    assert "register" in driver.current_url


def test_registration_short_password_error(driver):
    """Регистрация с паролем менее 6 символов."""
    driver.get(Urls.BASE_URL)
    user_name = generate_name()
    user_email = generate_email()
    short_password = "12345"

    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.register_link))
    driver.find_element(*Locators.register_link).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.submit_button))

    driver.find_element(*Locators.name_field).send_keys(user_name)
    driver.find_element(*Locators.email_field_register).send_keys(user_email)
    driver.find_element(*Locators.password_field_register).send_keys(short_password)
    driver.find_element(*Locators.submit_button).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.incorrect_password_message))
    assert driver.find_element(*Locators.incorrect_password_message).is_displayed()