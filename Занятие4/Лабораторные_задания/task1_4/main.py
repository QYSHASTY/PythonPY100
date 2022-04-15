def more_than_mean(list_numbers: list):
    avr_of_list = sum(list_numbers) / len(list_numbers)  # найти среднее арифметическое списка
    return [value for value in list_numbers if value > avr_of_list]  # с помощью list comprehension вернуть новый список


if __name__ == "__main__":
    print(more_than_mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
