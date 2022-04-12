DAYS_OF_YEAR = 365  # количество дней в году

start_year = int(input("Введите год своего рождения в формате yyyy  "))   #  запросить у пользователя год рождения
current_year = int(input("Введите текущуй год в формате yyyy  "))  # запросить у пользователя текущий год

days_of_life = (current_year - start_year) * DAYS_OF_YEAR  # посчитать и распечатать количество прожитых дней
print("Примерное число прожитых дней:")
print(days_of_life)
