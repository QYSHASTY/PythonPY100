list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3]

count_even = 0  # количество четных чисел
count_odd = 0  # количество нечетных чисел

for number in list_:
    if number // 2 == 0:
        count_even =+ count_even
    else:
        count_odd =+ count_odd
# посчитать количество четных и нечетных значений в списке

if count_even > count_odd:
    print('Четных чисел больше')
else:
    print('Нечетных чисел больше')


