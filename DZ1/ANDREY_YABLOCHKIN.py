first_question = 'Какая версия языка сейчас актуальна?'
second_question = 'Какая кодировка используется в строках?'
third_question = 'Какой оператор сравнения нужно использовать для работы с None и bool?'
fourth_question = 'Сколько значений есть у bool?'
fifth_question = 'Что будет есть случайно умножить None на число?'
sixth_question = 'Чему равно len("abc")?'
seventh_question = 'Какой цикл чаще используется?'
eighth_question = 'Можно ли назвать свою переменную False?'
ninth_question = 'Что будет результатом выражение 3 == 3.0?'
tenth_question = 'Как форматировать строку?'

questions = [first_question, second_question, third_question, fourth_question, fifth_question, sixth_question,
             seventh_question, eighth_question, ninth_question, tenth_question]

first_answer = 'python3'
second_answer = 'utf8'
third_answer = 'is'
fourth_answer = '2'
fifth_answer = 'ошибка'
sixth_answer = '3'
seventh_answer = 'for'
eighth_answer = 'нет'
ninth_answer = 'true'
tenth_answer = '.format'

answers = [first_answer, second_answer, third_answer, fourth_answer, fifth_answer, sixth_answer, seventh_answer,
           eighth_answer, ninth_answer, tenth_answer]

correct_answers = 0

for i in range(len(questions)):
    print(questions[i])
    answer = input('Ваш ответ:')
    if answer.lower() == answers[i]:
        correct_answers += 1
        print(f'Ответ "{answer}" верен')
    else:
        print('Неверный ответ')
print(f'Вы дали {correct_answers} правильных ответов из {len(questions)}')
