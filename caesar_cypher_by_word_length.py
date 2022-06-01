
encrypted = ''
result = ''
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
text = input('Введите текст для шифрования:   ')
words = text.split()


def letterchange(letter, key):
    res = ''
    index = alphabet.find(letter)
    res = alphabet[index + key]
    return res


def key(word):
    res = 0
    for c in word:
        if c.isalpha():
            res += 1
    return res


def word_encrypt(word):
    res = ''
    for i in word:
        if i in alphabet:
            res += letterchange(i, key(word))
        else:
            res += i
    return res


for word in words:
    encrypted += word_encrypt(word)
    encrypted += ' '

print(encrypted)
