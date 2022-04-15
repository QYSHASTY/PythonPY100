def get_list_number_divisors(number):
    get_list_number_divisors = []
    current_number = number

    for num in range(number, 0, -1):
        if number % (current_number) == 0:
             get_list_number_divisors.append(num)
        current_number -= 1


    return get_list_number_divisors

if __name__ == "__main__":
    print(get_list_number_divisors(2 ** 16))



