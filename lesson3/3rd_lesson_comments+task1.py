
n =int(input('Введите порядковый номер месяца(от 1 до 12): '))

months_dict ={1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}

for k, v in months_dict.items():
    if k==n:
        print(v)


if n==2:
    print('в этом месяце 28 день')
elif n%2==0:
    print('в этом месяце 30 дней')
else:
    print('в этом месяце 31 дней')


q = int(input('Вводим количес тво элементов списка: '))

list =[]
for i in range(q):
    list.append(input())

print(list)

