A = int(input("введите число"))

cond_1 = A % 2 == 0
cond_2 = A % 3 == 0

if cond_1 or cond_2:
    print('Число number кратно 2 или 3')
