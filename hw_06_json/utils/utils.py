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


def user_words_answers(words):
    '''функция задает вопрос из словаря, принммает ответы пользователя, сравнивает их с ответами из словаря,
     возвращает список ответов в булевом формате\\the function asks a question from the dictionary,
     accepts the user's answers, and compares them with the answers from the dictionary,
     returns a list of responses in Boolean format'''
    answers = {}
    for word, translate in words.items():
        answer = input(f'\n{word}, {len(translate)} букв, начинается на {translate[0].upper()}...\n').lower()
        if answer == translate:
            print(f'Верно, {word.title()} это {translate.title()}.')
            answers[word] = True
        else:
            print(f'Неверно, {word.title()} это {translate.title()}.')
            answers[word] = False
    return answers


def get_result(answers, user_level):
    '''функция принимает список с ответсами пользователя,
    выводит их в соответствии с правильностью, присваивает уровень знаний
    the function takes a list with the user's answers,
o   utputs them according to correctness, assigns the level of knowledge'''
    counter = 0
    print('\nПравильно отвеченные слова:')
    for key, value in answers.items():
        if value is True:
            print(key)
            counter += 1
    print('\nНеправильно отвеченные слова:')
    for key, value in answers.items():
        if value is False:
            print(key)
    return user_level[str(counter)]


def write_answers(file_name, answers):
    '''функция записывает результаты теста в файл
    the function writes the test results to a file'''
    answers_json = json.dumps(answers, ensure_ascii=False, indent=4)
    with open(file_name,'w',encoding='utf-8') as file:
        file.write(f"{answers_json}")
