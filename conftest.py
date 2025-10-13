import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Настройки для Chrome
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Инициализация драйвера
    driver = webdriver.Chrome(options=chrome_options)
    
    # Возвращаем драйвер тесту
    yield driver
    
    # Закрываем браузер после теста
    driver.quit()