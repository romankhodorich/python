import random

answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова",
           "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]

print()
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос!')
print()
name = input('Как тебя зовут, роднуля? ')
print(f'Ну привет, {name}!')
print()
a = input(f'Какой у тебя вопрос? Какие сомнения, {name}? ')
print()
while a != '':
    print(random.choice(answers))
    print()
    a = input(f'Есть еще вопросы? если нет, просто нажми enter')
print('Возвращайся если возникнут вопросы!')