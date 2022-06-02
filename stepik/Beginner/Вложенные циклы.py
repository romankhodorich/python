n = int(input())
for i in range(n):
    for j in range(i + 1):
        if n > i + j:
            print('*', end='')
    print()
