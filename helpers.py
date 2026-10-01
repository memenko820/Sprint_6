from datetime import date, timedelta
import random

# функция-генератор будущей даты на days дней
def get_future_date(days):
    future_date = date.today() + timedelta(days=days)
    return future_date.strftime('%d.%m.%Y')

# генератор рандомного номера телефона
def random_phone():
    phone = str(random.randint(1000000, 9999999))
    return f'7985{phone}'

# генератор рандомного имени, фамилии, адреса
def random_name():
    russian_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    name_length = random.randint(5, 10)
    name = ''.join(random.choices(russian_letters, k=name_length))
    return name