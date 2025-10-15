from selenium.webdriver.common.by import By

class Locators:
    """ПОЛНЫЙ набор локаторов для всех тестов Stellar Burgers"""
    
    # ===== ГЛАВНАЯ СТРАНИЦА =====
    login_button_main_page = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    personal_account_button = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    make_an_order_button = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    
    # ===== СТРАНИЦА АВТОРИЗАЦИИ (ЛОГИН) =====
    email_field = (By.XPATH, "//input[@type='text' and @name='name']")
    password_field = (By.XPATH, "//input[@type='password']")
    login_button = (By.XPATH, "//button[contains(text(), 'Войти')]")
    
    # ===== ССЫЛКИ ДЛЯ ПЕРЕХОДА =====
    register_link = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
    forgot_password_button = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
    
    # ===== СТРАНИЦА РЕГИСТРАЦИИ =====
    name_field = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    email_field_register = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    password_field_register = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    submit_button = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    login_button_in_registration_form = (By.XPATH, "//a[contains(@href, '/login') and contains(text(), 'Войти')]")
    
    # ===== СТРАНИЦА ВОССТАНОВЛЕНИЯ ПАРОЛЯ =====
    login_password_recovery_form_button = (By.XPATH, "//a[contains(@href, '/login') and contains(text(), 'Войти')]")
    
    # ===== ЛИЧНЫЙ КАБИНЕТ =====
    profile = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    order_history = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    logout_button = (By.XPATH, "//button[contains(text(), 'Выход')]")
    
    # ===== КОНСТРУКТОР И ШАПКА =====
    constructor_button_in_header = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    logo = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    
 
    selected_section = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span")

    # ===== РАЗДЕЛЫ КОНСТРУКТОРА =====
    buns_section = (By.XPATH, "//span[text()='Булки']/parent::div")
    sauces_section = (By.XPATH, "//span[text()='Соусы']/parent::div")
    fillings_section = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    # ===== СООБЩЕНИЯ ОБ ОШИБКАХ =====
    incorrect_password_message = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")