if __name__ == "__main__":

    list_ = list(range(10))
    print(list_)
    print(list_[9])


    list_[0], list_[9] = list_[9], list_[0]
    print(list_)

    pass
