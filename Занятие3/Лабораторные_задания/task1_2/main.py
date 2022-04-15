def get_factorial(number):
    current_factorial = 1

    for i in range(1, number + 1):
        current_factorial *= i

    return current_factorial



if __name__ == "__main__":
    print(get_factorial(5))
