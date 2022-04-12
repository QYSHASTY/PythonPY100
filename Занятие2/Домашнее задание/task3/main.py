A = int(input("введите число A  "))
B = int(input("введите число B  "))
C = int(input("введите число C  "))

cond_1 = A < 45
cond_2 = B < 45
cond_3 = C < 45

if cond_1 and (not cond_2) and (not cond_3):
    print('Только число А меньше 45')

elif (not cond_1) and cond_2 and (not cond_3):
    print('Только число B меньше 45')

elif (not cond_1) and (not cond_2) and cond_3:
    print('Только число C меньше 45')

else:
    print('Невозможно определить какие числа меньше 45')

