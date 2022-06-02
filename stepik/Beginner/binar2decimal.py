s = int(input('Введите основание (систему счисления) - целое число:  '))
i = input("Введите двоичное число из единиц и нулей:  ")
dec = 0
l = len(i) - 1
while l > 0:
    for digit in i:
        if digit == 'A':
            digit = 10
        elif digit == 'B':
            digit = 11
        elif digit == 'C':
            digit = 12
        elif digit == 'D':
            digit = 13
        elif digit == 'E':
            digit = 14
        elif digit == 'F':
            digit = 15
        else:
            digit = int(digit)
        dec += digit * (s ** l)
        l -= 1
print(
    f'Число {i} в {s}-ичной системе счисления равняется числу {dec} в десятичной!')
