import json


def get_data(file_path):
    '''функция принимает путь к файлу, конвертирует из json d python, возвращает python- адаптированные данные'''
    '''the function takes the path to the file, converts from json to python, returns python-adapted data'''

    with open(file_path, 'r', encoding='utf-8') as questions:
        json_data = questions.read()
        phyton_data = json.loads(json_data)
    return phyton_data
