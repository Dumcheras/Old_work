import re

'''returns regular expression patterns to validate the entered data\
\возвращает паттерны регулярных выражений для проверки введенных данных'''


def get_reg_data():
    reg_name = re.compile(r'^[A-Za-zА-Яа-я]+$')
    reg_surname = re.compile(r'^[A-Za-zА-Яа-я]+$')
    reg_phone = re.compile(r'[+]\d{1,3}\(\d{1,3}\)(\d{7})$')
    reg_email = re.compile(r'[A-Za-z0-9_]+@yandex\.ru$')
    reg_patterns_list = [reg_name, reg_surname, reg_phone, reg_email]
    return reg_patterns_list



