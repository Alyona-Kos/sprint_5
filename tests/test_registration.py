import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from data_randomizer import generate_name, generate_email, generate_password, generate_incorrect_password
from locators import Locators


class TestRegistration:
    """Набор тестов для проверки регистрации"""

    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.base_url = "https://stellarburgers.education-services.ru"

    # Позитивная проверка регистрации - НАДЕЖНАЯ ВЕРСИЯ
    def test_registration_positive(self, driver):
        """Позитивная проверка регистрации - НАДЕЖНАЯ ВЕРСИЯ"""
        driver.get(self.base_url)

        user_name = generate_name()
        user_email = generate_email()
        user_password = generate_password()

        print("1. Переходим на страницу регистрации...")
        driver.find_element(*Locators.login_button_main_page).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.register_link))
        driver.find_element(*Locators.register_link).click()
        
        # Ждем полной загрузки страницы регистрации
        WebDriverWait(driver, 10).until(EC.url_contains("/register"))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.submit_button))

        print("2. Заполняем форму регистрации...")
        print(f"   Имя: {user_name}")
        print(f"   Email: {user_email}")
        print(f"   Пароль: {user_password}")
        
        driver.find_element(*Locators.name_field).send_keys(user_name)
        driver.find_element(*Locators.email_field_register).send_keys(user_email)
        driver.find_element(*Locators.password_field_register).send_keys(user_password)
        
        # Делаем небольшую паузу перед отправкой для надежности
        import time
        time.sleep(1)
        
        driver.find_element(*Locators.submit_button).click()

        print("3. Ожидаем результат регистрации...")
        
        # Основная проверка - переход на страницу логина (как показал отладочный тест)
        WebDriverWait(driver, 20).until(EC.url_to_be("https://stellarburgers.education-services.ru/login"))
        current_url = driver.current_url
        
        print(f"   ✅ Перешли на: {current_url}")
        
        # Проверяем что мы именно на странице логина
        assert current_url == "https://stellarburgers.education-services.ru/login"
        
        # Дополнительные проверки на странице логина
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.login_button))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_field))
        
        print("✅ Успешная регистрация! Все проверки пройдены")

    # Регистрация с невалидным паролем
    def test_registration_incorrect_password_message(self, driver):
        driver.get(self.base_url)
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
        error_text = driver.find_element(*Locators.incorrect_password_message).text
        assert error_text == 'Некорректный пароль'
        print("✅ Проверка ошибки пароля!")

    # Регистрация с пустым именем
    def test_registration_empty_name_error(self, driver):
        driver.get(self.base_url)
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
        print("✅ Проверка пустого имени!")

    # Регистрация с некорректным email
    @pytest.mark.parametrize('invalid_email', ['invalid', 'test@', '@domain.com', 'test@domain', '123@ya.'])
    def test_registration_invalid_email_error(self, driver, invalid_email):
        driver.get(self.base_url)
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
        print(f"✅ Проверка email '{invalid_email}'!")

    # Регистрация с паролем менее 6 символов
    def test_registration_short_password_error(self, driver):
        driver.get(self.base_url)
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
        error_text = driver.find_element(*Locators.incorrect_password_message).text
        assert error_text == 'Некорректный пароль'
        print("✅ Проверка короткого пароля!")