from hw_06_json.utils.utils import get_data, get_user_level, user_words_answers, get_result, write_answers

questions, levels = get_data(r'questions/questions.json')
questions_list = questions['questions']
user_level = levels['levels']
# print(questions_list)  # список словарей
# print(user_level)  # словарь
user_name = input('Введите имя студента:\n')
user_choice = input('Введите уровень сложности:\nлегкий|средний|сложный\n')
user_words = get_user_level(user_choice, questions_list)
user_result = user_words_answers(user_words)
# print(user_result)
user_stage = get_result(user_result, user_level)
print(f'\nВаш ранг {user_stage}')
write_answers(fr"students/{user_name}_answers.json", user_result)
