from user_dates import data_user_id, data_surname, data_name, data_address, data_phone
from app import data_write, read_data, formating_dates, delete_row, deleting_dates, deleting_file, progr_exit
def main():
    while True:
        # Присваиваем переменной значение в виде названия файла, на которвый она будет ссылаться
        file_name = 'phone_directory.csv' 
        new_file_name = 'new_phone_directory.csv'
        # В данном блоке происходит выбор действий, которые должен выполняить
        #  пользователь
        print('ТЕЛЕФОННЫЙ СПРАВОЧНИК v.1.0')
        print('=' * 30)
        print(
            'ВЫБЕРИТЕ ИЗ МЕНЮ ДЕЙСТВИЕ, КОТОРОЕ ВЫ ХОТЕЛИ БЫ СОВЕРШИТЬ?'
        )
        print('=' * 30)
        print('[1] - Заполнить данные?\
            \n[2] - Вывести данные для просмотора на консоль?\
            \n[3] - Редактировать данные?\
            \n[4] - Удалить файл?'
        )
        print('-' * 30)
        answer_menu = int(input())
        if answer_menu == 1:      
            #  Данные функции вызываются бесконечное множество раз, позволяя заполнять данные
            # с новой строки
            u_id = data_user_id() 
            surname = data_surname()
            name = data_name()
            address = data_address()
            phone = data_phone()         
            data_write(u_id, surname, name, address, phone, file_name)
        elif answer_menu == 2:
            read_data(file_name)
        elif answer_menu == 3:
            print(
                'Хотите редактировать данные?\
                    \nДа / Нет'
            )
            answer2_menu = input()
            if answer2_menu.lower() == 'да' or answer2_menu.lower() == 'д':
                print(
                    'Выберите что вы хотите сделать?\
                    \n[1] - Отредактировать данные\
                    \n[2] - Удалить строку\
                    \n[3] - Удалить данные'
                )
                answer3_menu = int(input())
                if answer3_menu == 1:
                    print('Введите строку, которую нужно изменить?')
                    date = int(input())
                    formating_dates(date, file_name, new_file_name)
                elif answer3_menu == 2:
                    print('Введите номер строки, которую нужно удалить?')
                    date = int(input())
                    delete_row(date, file_name, new_file_name)
                elif answer3_menu == 3:
                    print('Введите номер строки?')
                    date = int(input())
                    deleting_dates(date, file_name, new_file_name)  
            elif answer2_menu.lower() == 'нет' or answer2_menu.lower() == 'н':
                continue
        elif answer_menu == 4:
            print(
                'Данные, содержащиеся в файле\
                \nбудут удалены безвозвратно.\
                \nХотите продолжить?\
                \nДа / Нет'
            )
            answer4_menu = input()
            if answer4_menu.lower() == 'да' or answer4_menu.lower() == 'д':
                deleting_file(file_name)
            elif answer4_menu.lower() == 'нет' or answer4_menu.lower() == 'н':
                continue
        # Выход из программы
        progr_exit()
