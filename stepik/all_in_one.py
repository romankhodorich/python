n = int(input())
count_3 = 0
last_num_repeat = 0
even_nums = 0
more_than_5_sum = 0
more_than_7_mult = 1
fives_and_zeroes = 0
last = n % 10

while n > 0:
    last_num = n % 10
    if last_num == 3:
        count_3 += 1
    if last == last_num:
        last_num_repeat += 1
    if last_num % 2 == 0:
        even_nums += 1
    if last_num > 5:
        more_than_5_sum += last_num
    if last_num > 7:
        more_than_7_mult *= last_num
    if last_num == 0 or last_num == 5:
        fives_and_zeroes += 1
    n //= 10

print(count_3)
# if last_num_repeat == 0:
print(last_num_repeat)
# else: print(last_num_repeat - 1)
print(even_nums)
print(more_than_5_sum)
print(more_than_7_mult)
print(fives_and_zeroes)
