import random
import string

def generate_name():
    """Генерирует случайное имя"""
    names = ['Иван', 'Мария', 'Петр', 'Анна', 'Сергей', 'Ольга', 'Алексей', 'Елена']
    return random.choice(names)

def generate_email():
    """Генерирует случайный email в правильном формате"""
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domains = ['ya.ru', 'gmail.com', 'mail.ru', 'yandex.ru']
    domain = random.choice(domains)
    return f"{username}@{domain}"

def generate_password():
    """Генерирует валидный пароль (6+ символов)"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=8))

def generate_incorrect_password():
    """Генерирует невалидный пароль (< 6 символов)"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=5))  # 5 символов