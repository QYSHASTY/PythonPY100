month = int(input("Задайте номер месяца"))  # TODO запросить месяц у пользователя. Номер месяца - целочисленное значение!

if month in range(3, 6):  # TODO записать условие через операторы or
    print("Весна")
elif month in range(6, 9):  # TODO проверить вхождение месяца в список месяцев лета
    print("Лето")
elif month in range(9, 11):  # TODO проверить вхождение месяца в кортеж месяцев осени
    print("Осень")
elif month in range(1, 3) or month == 12:  # TODO проверить вхождение месяца в множество месяцев лета
    print("Зима")
