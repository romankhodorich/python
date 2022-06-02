dir = input('Задайте направление шифрования "+" или "-":   ')
lang = input('Задайте языка алфавита "ru" или "en":   ')
encrypted = ''
en_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
ru_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
key = int(input('Введите ключ шифрования:   '))
passphrase = input('Введите текст для шифрования:   ')
words = passphrase.split()
if lang == 'ru':
    alphabet = ru_alphabet
elif lang == 'en':
    alphabet = en_alphabet


def letterchange(letter, key):
    res = ''
    index = alphabet.find(letter)
    if dir == '+':
        res += alphabet[index + key]
    if dir == '-':
        res += alphabet[(index + len(alphabet) // 4) - key]
    return res


def key_by_wordlength():
    res = 0
    for word in words:
        for c in word:
            if c.isalpha():
                res += 1
    return res


print(encrypted)
