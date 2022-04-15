def get_month_count(money_capital, salary, spend, inflation):
    current_money = money_capital
    get_month_count = 0

    while True:
        current_money = current_money + salary - spend
        # print(spend, current_money)

        if current_money <= 0:
            break

        get_month_count += 1
        spend = spend + spend * inflation

        # print(spend, current_money)
        # print('_____')

    return get_month_count


if __name__ == "__main__":
    print(get_month_count(100000, 10000, 15000, 0.05))
