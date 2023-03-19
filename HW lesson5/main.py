
from utils import change_calc

price = float(input('Введите стоимость товара: '))
enter_money = input('Введите внесенные купюры: ').split()
result = change_calc(price, enter_money)

print(result)
