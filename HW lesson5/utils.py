

banknotes = {5000, 2000, 1000, 500, 100, 50, 10, 5, 2, 1, 0.50, 0.10, 0.05, 0.01}
bank_list = sorted(banknotes,reverse=True)


def change_calc(price, enter_money):
    enter_sum = list(map(float, enter_money))
    sum_enter = sum(enter_sum)  #Общая сумма, внесенная покупателем
    change1 = sum_enter - price#Сдача
    change = round(change1,2)#Округляем до второго знака


    if sum_enter<price:
        print('Недостаточно внесенных средств')
    elif sum_enter==price:
        print('Сдача не требуется')
    else:
        print('Сдача: ', change)
        change_list = []  # Пустой список, в который будут падать купюры и монеты
        while change != 0:
            for i in bank_list:
                if change//i>0:
                    n = change/i#количество данных купюр
                    for p in range(int(n)):
                        change_list.append(i)
                    change -= i*n
        return change_list





price = float(input('Введите стоимость товара: '))
enter_money = input('Введите внесенные купюры: ').split()
print(change_calc(price, enter_money))
