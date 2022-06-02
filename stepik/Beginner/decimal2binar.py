s = int(input('Введите основание (систему счисления) - целое число:  '))
i = int(input("Введите десятичное число:  "))
bin = ''
while i > 0:
    if i % s <= 9:
        bin += str(i % s)
    elif i % s == 10:
        bin += 'A'
    elif i % s == 11:
        bin += 'B'
    elif i % s == 12:
        bin += 'C'
    elif i % s == 13:
        bin += 'D'
    elif i % s == 14:
        bin += 'E'
    elif i % s == 15:
        bin += 'F'
    i = i // s
if s == 2:
    bin += 'b0'
elif s == 8:
    bin += 'o0'
elif s == 16:
    bin += 'x0'
print(bin[::-1])
