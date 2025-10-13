import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import Locators


class TestLogin:
    """Тесты для проверки входа в систему"""
    
    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.base_url = "https://stellarburgers.education-services.ru"
        self.email = 'alena_kostrikina_33@yandex.ru'
        self.password = 'kos12345'
    
    def _perform_login(self, driver):
        """Универсальный метод для выполнения входа"""
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_field))
            driver.find_element(*Locators.email_field).send_keys(self.email)
            driver.find_element(*Locators.password_field).send_keys(self.password)
            driver.find_element(*Locators.login_button).click()
            
            # Проверяем успешный вход
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))
            assert driver.find_element(*Locators.make_an_order_button).is_displayed()
            return True
        except TimeoutException:
            print("❌ Таймаут при выполнении входа")
            return False

    # Вход по кнопке «Войти в аккаунт» 
    def test_login_via_button_on_main_page(self, driver):
        driver.get(self.base_url)

        driver.find_element(*Locators.login_button_main_page).click()
        
        success = self._perform_login(driver)
        assert success, "Вход через кнопку на главной не удался"
        print("✅ Вход через кнопку на главной - УСПЕХ")

    # Вход через кнопку «Личный кабинет»
    def test_login_via_personal_account(self, driver):
        driver.get(self.base_url)

        driver.find_element(*Locators.personal_account_button).click()
        
        success = self._perform_login(driver)
        assert success, "Вход через Личный кабинет не удался"
        print("✅ Вход через Личный кабинет - УСПЕХ")

    # Вход через кнопку в форме регистрации
    def test_login_via_registration_form_button(self, driver):
        driver.get(self.base_url)

        # Переходим на страницу регистрации
        driver.find_element(*Locators.login_button_main_page).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.register_link))
        driver.find_element(*Locators.register_link).click()
        
        # Кликаем "Войти" на странице регистрации
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.submit_button))
        driver.find_element(*Locators.login_button_in_registration_form).click()
        
        success = self._perform_login(driver)
        assert success, "Вход через форму регистрации не удался"
        print("✅ Вход через форму регистрации - УСПЕХ")

    # Вход через кнопку в форме восстановления пароля
    def test_login_via_password_recovery_button(self, driver):
        driver.get(self.base_url)

        # Переходим на страницу восстановления пароля
        driver.find_element(*Locators.personal_account_button).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.forgot_password_button))
        driver.find_element(*Locators.forgot_password_button).click()
        
        # Кликаем "Войти" на странице восстановления
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.login_password_recovery_form_button))
        driver.find_element(*Locators.login_password_recovery_form_button).click()
        
        success = self._perform_login(driver)
        assert success, "Вход через форму восстановления пароля не удался"
        print("✅ Вход через форму восстановления пароля - УСПЕХ")
