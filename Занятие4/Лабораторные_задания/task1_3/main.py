def count_even_numbers(list_numbers: list) -> int:
    list_even_numbers = [value for value in list_numbers if value % 2 == 0]

    return len(list_even_numbers)

if __name__ == "__main__":
    print(count_even_numbers(list(range(1, 25))))
