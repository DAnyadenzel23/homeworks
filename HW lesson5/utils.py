price = float(input('Введите стоимость товара: '))

enter_money =input('Введите внесенные купюры: ').split()
print(float(price))

enter_sum = list(map(float, enter_money))
print(enter_sum)

sum_enter = sum(enter_sum)
print(sum_enter)
banknotes = {5000, 2000, 1000, 500, 100, 50, 10, 5, 2, 1, 0.50, 0.10, 0.05, 0.01}
bank_list = sorted(banknotes,reverse=True)
print(bank_list)
def change_calc(price,sum_enter):
    change = sum_enter - price
    change_list = []
    while change != 0:
        for i in bank_list:
            if i <= change:
                change_list.append(i)
                change -= i

            else:
                pass
        return change, change_list
    print(change)
    print(change_list)
print(change_calc(price,sum_enter))