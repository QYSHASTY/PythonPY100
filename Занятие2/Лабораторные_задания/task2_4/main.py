if __name__ == "__main__":
    phrase = "Hello,world"

    initial_offset = 5  # чему равно начальное смещение?

    for index, value in enumerate(phrase):  # как за один раз получать пару индекс-значение?
        print(" " * (index + initial_offset), value)  # как тогда должен выглядеть индекс?
    # как использовать начальное смещение в команде enumerate?
