def get_unique_words(str_words: str):

    words_list = str_words.split(" ")  # разделить строку по пробелам
    un_list = list(set(words_list))

    return un_list

    print(un_list)


if __name__ == "__main__":
    print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
