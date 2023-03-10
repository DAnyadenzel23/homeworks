#my_stng = 'Hello world!'
#for i in range(len(my_stng)):
 #   if my_stng[i] =='l':
  #      print(my_stng[i])

#name = input('Введите имя: ')
#s_name = input('Введите фамилию: ')
#flngs = input('Введите инфу о себе: ')
#print('My name is {}. My second name is {}.Я {}'.format(name,s_name,flngs))
#print(name.count('i')+s_name.count('i')+flngs.count('i'))

#txt ='Ramsdale.White.Saliba.Gabriel.Zinchenko'
#print(txt.split("."))

#for i in txt.split("."):
 #   print('Министр обороны: '+i)

#list = [2,4,5,19,90]

#for i in list:
 #   if i%2==0:
  #      print(i)


'''Заводим список с n оличеством элементов и сами объекты через input'''
#n = int(input('Введите количество элементов списка: '))
#lst = []
#for i in range(n):
    #lst.append(input())

#print(lst)
'''Заводим список с n оличеством элементов и сами объекты через input'''


"""Кортежи - те же списки, но неизменяемые, в остальном все то же самое"""
#tpl =(2,5,6,'Kokonuts',True,[])#можно задавать его без скобок, просто черз запятую объекты
#print(tpl[-2])
#print(type(tpl))
##True
##<class 'tuple'>
"""Кортежи - те же списки, но неизменяемые, в остальном все то же самое"""

"""Тип данных - SET - Неупорядоченная коллекция элементов"""
#sets={1,2,3,4}#Сэты не имеют индексов
#sets_2={4,7,8}#Элементы так же можно добавлять через add, вставляться будут в случйное место в этом массиве
#sets_3={4,6,7,8}#Так же можно и удалять через Remove()
#sets_2.add(6)
#sets_3.remove(7)
#print(sets_2)
#print(sets_3)
##{8, 4, 6, 7} - sets_2 новый, после использования add
##{8, 4, 6} - sets_3 новый, после использования remove
#print(sets.intersection(sets_2))
#print(sets_2.union(sets_3))
#print(sets_2.difference(sets))
##{4} - выделение общего у сэта и сэта_2
##{4, 6, 7, 8} - объединение сэта_2 и сэта_3. Без повторов!!!
##{8, 6, 7} - различия, а именно чем сэт_2 отличается от сэта!!!

"""Dict - словари - неизменяемая коллекция данных, хранящая пары: Ключ и значение. Тоже неупорядоченно хранятся внутри объекты."""

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
