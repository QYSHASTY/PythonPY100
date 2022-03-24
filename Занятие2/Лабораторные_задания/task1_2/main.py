A = int(input("введите число A"))
B = int(input("введите число B"))

cond_1 = A // 2 == 1
cond_2 = B // 2 == 1

if cond_1 or cond_2:
    print('Среди чисел A и B есть нечетные')
