banknotes = {5000, 2000, 1000, 500, 100, 50, 10, 5, 2, 1, 0.50, 0.10, 0.05, 0.01}
bank_list = sorted(banknotes, reverse=True)# Сортировка от большей к меньшей банкнот-->
                                           # для выдачи наименьшего количества купюр

def change_calc(price, enter_money):
    cash_deposited1 = list(map(float, enter_money))# Делаем список с данными типа float
    cash_deposited = sum(cash_deposited1)  #Общая сумма, внесенная покупателем
    change1 = cash_deposited - price#Сдача
    change = round(change1, 2)#Округляем до второго знака
    if price <= 0:
        print('Некорректно введена стоимость товара')
        raise ValueError('Некорректно введена стоимость товара')
    if sum_enter < price:
        print('Недостаточно внесенных средств')
        raise ValueError('Недостаточно внесенных средств')
    elif sum_enter == price:
        print('Сдача не требуется')
        return 'Сдача не требуется'
    else:
        print('Сдача: ', change)
        change_list = []  # Пустой список, в который будут падать купюры и монеты в сдачу
        while change != 0:
            for i in bank_list:
                if change//i > 0:
                    numb_of_bills = change//i#количество данных купюр
                    for p in range(int(numb_of_bills)):
                        change_list.append(i)
                        change = round(change, 2) - i
        return change_list

if __name__=='__main.py':
    price = float(input('Введите стоимость товара: '))
    enter_money = input('Введите внесенные купюры: ').split()
    result = change_calc(price, enter_money)
