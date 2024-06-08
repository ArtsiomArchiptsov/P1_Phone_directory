# Создается цикл функций, которые заполняют таблицу данными о пользователе
def data_user_id():
    print("Введите номер порядковый номер строки?")
    u_id = int(input())
    return u_id
def data_surname():
     print("Введите Вашу фамилию?")
     surname = input().title()
     return surname
def data_name():
     print("Введите Ваше  имя?")
     name = input().title()
     return name
def data_address():
     print("Введите Ваш адрес?")
     address = input().title()
     return address
def data_phone():
     print("Введите номер Вашего телефона?")
     phone = int(input())
     return phone