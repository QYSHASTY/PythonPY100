number = 123

d_1 = number // 100       # найти число сотен
d_2 = number % 100 // 10  # найти число десятков
d_3 = number % 10         # найти число единиц

list_digit = [d_1, d_2, d_3] # сформировать список чисел
print(list_digit)

print("Сумма цифр", sum(list_digit))  # сумма цифр
print("Количество цифр", len(list_digit))  # количество цифр
print("Минимальная цифра", min(list_digit))  # минимальная цифра
print("Максимальная цифра", max(list_digit))  # максимальная цифра
