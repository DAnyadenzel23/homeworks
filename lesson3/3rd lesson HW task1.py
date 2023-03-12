'''1. Напишите программу, считывающую одно число N - номер месяца, и выводящую, сколько в  этом месяце дней и его название. (используйте словари)'''
n =int(input('Введите порядковый номер месяца(от 1 до 12): '))

months_dict ={1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}

month_result = list(months_dict.values())[n-1]
print(month_result)

if n==2:
    print('в этом месяце 28 дней')
elif n%2==0:
    print('в этом месяце 30 дней')
else:
    print('в этом месяце 31 дней')






