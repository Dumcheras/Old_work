from hw_06_json.utils.utils import get_data

questions, levels = get_data(r'questions/questions.json')
questions_list = questions['questions']
user_level = levels['levels']
# print(questions_list)  # список словарей
# print(user_level)  # словарь
