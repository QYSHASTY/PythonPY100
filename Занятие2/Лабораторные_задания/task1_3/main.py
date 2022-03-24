A = int(input("введите число A"))
B = int(input("введите число B"))

sum_of_sq = A ** 2 + B ** 2
sq_of_sum = (A + B) ** 2

if sum_of_sq < sq_of_sum:
    print('Cумма квадратов меньше квадрата суммы')

elif sum_of_sq > sq_of_sum:
    print('Cумма квадратов больше квадрата суммы')

else:
    print('Cумма квадратов равна квадрату суммы')
