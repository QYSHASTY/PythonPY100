TAX_RATE = 0.13  # ставка подоходного налога

salary = int(input("Введите размер оклада:  "))   #  запросить у пользователя размер оклада

tax_value = salary * TAX_RATE  # размер налога
salary_net = salary - tax_value  # сумма на руки
print("Сумма налога: ", tax_value)
print("Сумма на руки: ", salary_net)
