# test_constructor_sections.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from test_data import TestData


class Locators:
    # Кнопка "Войти в аккаунт" на главной
    login_button_main_page = (By.XPATH, "//button[text()='Войти в аккаунт']")
    
    # Поля формы входа
    email_field = (By.XPATH, "//input[@name='name']")
    password_field = (By.XPATH, "//input[@name='Пароль']")
    login_button = (By.XPATH, "//button[text()='Войти']")
    
    # Кнопка "Оформить заказ" (индикатор успешного входа)
    make_an_order_button = (By.XPATH, "//button[text()='Оформить заказ']")
    
    # Разделы конструктора - исправленные локаторы
    buns_section = (By.XPATH, "//span[text()='Булки']/parent::div")
    sauces_section = (By.XPATH, "//span[text()='Соусы']/parent::div")
    fillings_section = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    # Активный раздел
    selected_section = (By.XPATH, "//div[contains(@class, 'current')]/span")


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия браузера."""
    options = Options()
    # options.add_argument('--headless')  # Раскомментируйте для отладки
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def login(driver, email, password):
    """Вспомогательная функция для логина."""
    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.email_field))
    
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))


def click_section(driver, section_locator, section_name):
    """Клик по разделу с ожиданием кликабельности."""
    section_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(section_locator)
    )
    
    # Прокручиваем к элементу если нужно
    driver.execute_script("arguments[0].scrollIntoView();", section_element)
    
    # Кликаем через ActionChains для надежности
    ActionChains(driver).move_to_element(section_element).click().perform()


def wait_for_section_active(driver, section_name, timeout=10):
    """Ожидание активации раздела с явной проверкой."""
    try:
        WebDriverWait(driver, timeout).until(
            EC.text_to_be_present_in_element(Locators.selected_section, section_name)
        )
        actual_text = driver.find_element(*Locators.selected_section).text
        assert actual_text == section_name, f"Ожидался раздел '{section_name}', но активен '{actual_text}'"
    except:
        # Если не сработало, попробуем альтернативный локатор
        alternative_locator = (By.XPATH, f"//div[contains(@class, 'current')]//span[text()='{section_name}']")
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(alternative_locator)
        )


def test_navigate_buns_to_fillings(driver):
    """Переход из раздела 'Булки' в раздел 'Начинки'."""
    driver.get(TestData.BASE_URL)
    login(driver, TestData.EMAIL, TestData.PASSWORD)
    
    click_section(driver, Locators.fillings_section, "Начинки")
    wait_for_section_active(driver, "Начинки")


def test_navigate_fillings_to_sauces(driver):
    """Переход из раздела 'Начинки' в раздел 'Соусы'."""
    driver.get(TestData.BASE_URL)
    login(driver, TestData.EMAIL, TestData.PASSWORD)
    
    click_section(driver, Locators.fillings_section, "Начинки")
    wait_for_section_active(driver, "Начинки")
    
    click_section(driver, Locators.sauces_section, "Соусы")
    wait_for_section_active(driver, "Соусы")


def test_navigate_sauces_to_buns(driver):
    """Переход из раздела 'Соусы' в раздел 'Булки'."""
    driver.get(TestData.BASE_URL)
    login(driver, TestData.EMAIL, TestData.PASSWORD)
    
    click_section(driver, Locators.sauces_section, "Соусы")
    wait_for_section_active(driver, "Соусы")
    
    click_section(driver, Locators.buns_section, "Булки")
    wait_for_section_active(driver, "Булки")