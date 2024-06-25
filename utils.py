import re

'''returns regular expression patterns to validate the entered data|возвращает паттерны регулярных выражений для проверки введенных данных'''


def get_reg_data():
    reg_name = re.compile(r'^[A-Za-zА-Яа-я]+$')
    reg_surname = re.compile(r'^[A-Za-zА-Яа-я]+$')
    reg_phone = re.compile(r'[+]\d{1,3}\(\d{1,3}\)(\d{7})$')
    reg_email = re.compile(r'[A-Za-z0-9_]+@yandex\.ru$')
    reg_patterns_list = [reg_name, reg_surname, reg_phone, reg_email]
    return reg_patterns_list


'''проверяет данные при вводе пользователем|checks the data when the user enters it'''


def reg_check(user_data, reg_pattern, users_list, data_to_check=None):
    while True:
        if reg_pattern.match(user_data):  # получаем булевое значение|we get a Boolean value
            if len(users_list) > 0 and data_to_check:
                if not check_unique_data(user_data,
                                         data_to_check):  # принимает на основании аргументов булевое значение по ретерну
                    user_data = input()
                    continue
        else:
            print("Ввод некорректен\nПовторите ввод")
            user_data = input()
            continue
        print(f"{user_data} - данные приняты")
        return user_data


''' проверяет уникальность введенных данных|checks the uniqueness of the entered data'''


def check_unique_data(user_data, data_to_check):
    if user_data in data_to_check:
        print("Такие данные уже есть")
        print("введите уникальные данные!")
        return False
    else:
        return True
