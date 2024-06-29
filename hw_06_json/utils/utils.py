import json


def get_data(file_path):
    '''функция принимает путь к файлу, конвертирует из json d python, возвращает python- адаптированные данные
    the function takes the path to the file, converts from json to python, returns python-adapted data'''

    with open(file_path, 'r', encoding='utf-8') as questions:
        json_data = questions.read()
        phyton_data = json.loads(json_data)
    return phyton_data


def get_user_level(user_select, questions_list):
    '''функция позволяет выбрать уровень сложности через input.
    по умолчанию или при некоректном вводе устанавливается легкий уровень
    the function allows you to select the difficulty level via input.
    by default, or if the input is incorrect, the light level is set'''
    if user_select == 'средний':
        words = questions_list[1]
    elif user_select == 'сложный':
        words = questions_list[2]
    else:
        words = questions_list[0]
    return words
