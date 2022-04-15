if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 4, -3, -6, 8, 6, 9]

    avr_of_list = sum(list_) / len (list_)
    new_list = [value - avr_of_list for value in list_]

    print(new_list)
