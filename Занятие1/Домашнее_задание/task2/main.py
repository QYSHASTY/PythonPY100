time_in_min = int(input("Введите время выполнения одного задания в минутах:    "))

sec_min = 60  # в минуте 60 секунд
numb_of_tasks = 10

print("Среднее время для выполнения", numb_of_tasks, "заданий", time_in_min * numb_of_tasks / sec_min, "часов")