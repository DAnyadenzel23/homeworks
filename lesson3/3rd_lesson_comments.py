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
#Вывод значения по ключу - gets/values функции, gets можно задать 2-ой аргумент, потребуется в случае отсутствия
#первого аргумента(такого ключа в словаре), выдаст none, или можно прописать строку "Не найдено".

##person = {"name": "Kelly", "age":25, "city": "New york"}
##print(person.get('age'))
##print(person.get('heigh', 'Не указан рост в словаре'))

#Значениями словаря могут быть и списки
##team_strikers = {'Arsenal':['Saka', 'Jesus', 'Martinelly'], 'Mancity':['Foden', 'Haaland', 'Mahrez']}
##print(team_strikers['Arsenal'][0])

##d1 = {"a": 100, "b": 200, "c":300}
##d2 = {'a': 300, 'b': 200, 'd':400}
##print(d1["b"] == d2["b"])
#Вывод: True

#Объединить два словаря
##dict_1 = {'a': 100, 'b': 200, 'c': 300}
##dict_2 = {'d': 400, 'e': 500, 'f': 600}
##dict_3 = dict_1.copy()
##dict_3.update(dict_2)
##print(dict_3)

#Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.
#print(dict_3.get('a'))#можно вытащить через get  все значения и перемножить их a*b*c... или:
##cort = tuple(dict_3.values())
##print(cort[0]*cort[1]*cort[2]*cort[3]*cort[4]*cort[5])#или
##result = 1
##for i in dict_3:
  ##  result = result * dict_3[i]
##print(result)

#Создать словарь, в котором ключами будут их числа, а значениями их кубические значения
##dict_4 = {i: i**3 for i in range(1,11)}
##print(dict_4)

#Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом, чтобы элементы первого списка
#были ключами, а элементы второго — соответственно значениями нашего словаря.
##dict_5 = {'a': 10, 'b': 20, 'c': 30}
##dict_6 = {'d': 40, 'e': 50, 'f': 60}
##keyses = tuple(dict_5.keys())
##vals = tuple(dict_6.values())
##print(keyses)
##print(vals)
##dict_7 = {keyses[0]:vals[0], keyses[1]:vals[1], keyses[2]:vals[2]}
##print(dict_7)
#Чуть хитрее, zip создает из двух списков(кортежей или сэтов) создает один, состоящий из кортежей, а далее преобразуем в список через dict
##dictzip_7 = dict(zip(keyses, vals))
##print(dictzip_7)

#Создайте словарь из строки 'pythonist' следующим образом: в качестве ключей возьмите буквы строки,
#а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.
##my_str = 'pythonist'
##dict_8 = {i:my_str.count(i) for i in my_str}
##print(dict_8)
