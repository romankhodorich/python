import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

n = int(input('Введите количество генерируемых паролей: '))
length = int(input('введите длину одного пароля: '))
if input('Включать ли цифры в пароль? да/нет:   ') == 'да':
    chars += digits
if input('Включать ли прописные буквы в пароль? да/нет:   ') == 'да':
    chars += uppercase_letters
if input('Включать ли строчные буквы в пароль? да/нет:   ') == 'да':
    chars += lowercase_letters
if input('Включать ли символы пунктуации в пароль? да/нет:   ') == 'да':
    chars += punctuation
if input('Включать ли в пароль неоднозначные символы (il1Lo0O)? да/нет:   ') == 'нет':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password


for _ in range(n):
    print(generate_password(length, chars))
