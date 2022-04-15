def task(n: int, m: int) -> list:  # записать функцию с аннотацией типов
    list_ = list(range(n, m + 1))

    return [i ** 2 for i in list_]


if __name__ == "__main__":
    number_n = 10
    number_m = 20

    print(task(number_n, number_m))
