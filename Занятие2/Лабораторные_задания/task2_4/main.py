if __name__ == "__main__":
    phrase = "Hello,world"

    initial_offset = 5  # TODO чему равно начальное смещение?

    for index, value in enumerate(phrase):  # TODO как за один раз получать пару индекс-значение?
        print(" " * (index + initial_offset), value)  # TODO как тогда должен выглядеть индекс?
    # TODO как использовать начальное смещение в команде enumerate?
