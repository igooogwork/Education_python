import random
import string
import pyperclip

def generate_complex_password(length=24):
    # Создаем строку с символами, которые будут использоваться для генерации пароля
    characters = string.ascii_letters + string.digits  # Буквы и цифры
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Генерируем пароль и выводим его
password = generate_complex_password()
pyperclip.copy(password)