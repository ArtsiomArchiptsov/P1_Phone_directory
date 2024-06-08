# Данная функция позволяет завершить бесконечную итерацию цикла while
def progr_exit():
     print(
          'Жалаете продолжить?\
            \nДа / Нет'
     )
     answer_prog = input()
     if answer_prog.lower() =='да' or answer_prog.lower() =='д':
          pass
     elif answer_prog.lower() =='нет' or answer_prog.lower() =='н':
          exit()

# С помощью данной функции заполняется список, который сохраняется в дальнейшем в файл
# при этом список сохраняется в списке, для того, чтобы можно было извлекать данные из 
# файла и работать с ними.  
# Сохраняем данные в файл, используя библиотеку csv, при том запись происходит с новой строки.
def data_write( u_id, surname, name, address, phone, file_name):
    import csv
    user_data = [
         [ u_id, surname, name, address, phone]
     ]
    for user in user_data:
         with open(file_name,'a', newline='', encoding='utf-8') as csvfile_object:
            writer = csv.writer(csvfile_object, delimiter='|')
            writer.writerow(
                 user
                 )
# Данная функция выводит данные на консоль, считывая их из файла
def read_data(file_name): 
     import csv    
     with open(file_name, 'r', encoding='utf-8') as csvfile_object:
        reader=csv.reader(csvfile_object) 
        for line in reader:
             print(*line, end = '\n') 
# С помощью данной функции производим измения в любой строке файла.
# Изменения проходят по индексу с последующим присваиванием значения.
# Проводится перебор строк вначале выводится та строка, которую нужно 
# изменить, затем по индексу вводится то значение, которое нужно изменить.
# В конце с помощью библиотеки os происходит перезапись данных. Вначале
# данные сохраняются в временный файл new_file_name, затем перезаписываются
# в существующий файл file_name
def formating_dates(date, file_name, new_file_name):
    import csv, os  
    new_rows = []
    with open(file_name, 'r', newline='', encoding='utf-8') as csvfile_object:
         reader = csv.reader(csvfile_object, delimiter='|')
         for row in reader:
             if str(date) in row:
                 print(row, end=' ')
                 print('Введите номер, по которому нужно произвести измения?\
                      \n(1) - Фамилия\
                      \n(2) - Имя\
                      \n(3) - Адрес\
                      \n(4) - Телефон')
                 print('Введите номер?')
                 index = int(input())
                 print('Введите новое значение?')
                 value = input().title()
                 if index < len(row):
                     row[index] = value
                 print(row, end=' ')
             new_rows.append(row)
    with open(new_file_name, 'w', newline='', encoding='utf-8') as csvfile_object:
          writer = csv.writer(csvfile_object, delimiter='|')
          writer.writerows(new_rows) 
    os.remove(file_name)
    os.rename(new_file_name, file_name) 
# Данная функция удаляет строку по ее id. Происходит фильтрация по имеющимся строкам. Создан новый
# пустой список, который перезаписывается на место выбранной строки, тем самым создавая пустую строку
# С помощью библиотеки os файл перезаписывается.
def delete_row(date, file_name, new_file_name):
    import csv, os    
    new_rows = []
    with open(file_name, 'r', encoding='utf-8') as csvfile_object:
         reader = csv.reader(csvfile_object, delimiter='|')
         for row in reader:
             if str(date) not in row:
                 new_rows.append(row)
    with open(new_file_name, 'w', newline='', encoding='utf-8') as csvfile_object:
         writer = csv.writer(csvfile_object, delimiter='|')
         writer.writerows(new_rows)
    os.remove(file_name)
    os.rename(new_file_name, file_name)
# Данная функция удаляет данные по их индексу в списке
def deleting_dates(date, file_name, new_file_name):
    import csv, os  
    new_rows = []
    with open(file_name, 'r', newline='', encoding='utf-8') as csvfile_object:
         reader = csv.reader(csvfile_object, delimiter='|')
         for row in reader:
             if str(date) in row:
                 print(row, end=' ')
                 print('Введите номер, по которому нужно произвести измения?\
                      \n(1) - Фамилия\
                      \n(2) - Имя\
                      \n(3) - Адрес\
                      \n(4) - Телефон')
                 print('Введите номер?')
                 index = int(input())
                 if index < len(row):
                     del row[index] 
                 print(row, end=' ')
             new_rows.append(row)
    with open(new_file_name, 'w', newline='', encoding='utf-8') as csvfile_object:
          writer = csv.writer(csvfile_object, delimiter='|')
          writer.writerows(new_rows) 
    os.remove(file_name)
    os.rename(new_file_name, file_name) 

# Полное удаление файла без возможности восстановления
def deleting_file(file_name):
    import os
    if os.path.exists(file_name):
       os.remove(file_name)
       print(f"Файл {file_name} успешно удален")
    else:
       print(f"Файл {file_name} не существует")