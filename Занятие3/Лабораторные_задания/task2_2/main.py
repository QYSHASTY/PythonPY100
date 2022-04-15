def is_palindrome(str_: str):
    str_new = ''.join(str_.lower().split())
    print(str_new)

    if str_new == str_new[::-1]:
        print("Строка палиндром")
    else:
        print("Строка не палиндром")

if __name__ == "__main__":
    is_palindrome("Кит на море не романтик")
    is_palindrome("Прочая строка")
