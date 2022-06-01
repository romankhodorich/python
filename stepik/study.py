num = int(input())
arr = []
summ = 0
count = 0
multiplexor = 1
while num != 0:
    last_digit = num % 10
    arr.append(last_digit)
    summ += last_digit
    count += 1
    multiplexor *= last_digit
    num = num // 10

# print(summ)
# print(count)
# print(multiplexor)
#print(summ / count)
print(arr[-2])
#print(arr[0] + arr[-1])
