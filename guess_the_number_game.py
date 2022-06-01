from curses.ascii import isdigit
import random

answer = random.randint(1, 100)
print('Ну привет, дружочек! Поиграем?')
count = 0
a = int(input('Угадай число от 1 до 100: '))


def is_invalid(a):
    if a not in range(1, 101):
        return True


while is_invalid(a):
    a = int(input('Ну это не от 1 до 100! Введи нормально! '))
while int(a) != answer:
    if int(a) < answer:
        a = int(input(f'Не угадал, ответ больше чем {a}, попробуй ещё раз: '))
        count += 1
        continue
    elif a > answer:
        a = int(input(f'Не угадал, ответ меньше чем {a}, попробуй ещё: '))
        count += 1
        continue
    else:
        break
print(f'Точно! Загадано число {answer}!!! Йееееееее!!!!!')
if count >= 6:
    print(f'Тебе понадобилось {count} попыток, могло быть и лучше!)))')
else:
    print(f'Тебе понадобилось {count} попыток, красавелло!')
