from selenium.webdriver.common.by import By

class Locators:
    """Локаторы для элементов веб-страницы"""
    
    # Главная страница
    login_button_main_page = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    
    # Страница авторизации/регистрации
    register_link = (By.LINK_TEXT, "Зарегистрироваться")
    name_field = (By.XPATH, "//fieldset[1]//input")
    email_field = (By.XPATH, "//fieldset[2]//input")
    password_field = (By.XPATH, "//fieldset[3]//input")
    submit_button = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    
    # Сообщения об ошибках
    incorrect_password_message = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")
    
    # Страница логина
    login_button = (By.XPATH, "//button[contains(text(), 'Войти')]")