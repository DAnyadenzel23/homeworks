
'''Лямбда функция - анонимная,безименная функция, которая отрабатывается только локально, к ней нельзя будет обратиться'''
# Как правило, используется с другими функциями в связке.

def multy(x):
    return x**2
#print(list(map(multy, [1, 2, 3, 4])))
## Или же это выражение-функция в одну строчку, резултат один
#print(list(map(lambda x:x**2,[1, 2, 3, 4])))
#[1, 4, 9, 16]

#list1 = [2,3,4,5]
#list2 = [20,30,40,50,66]
#print(list(map(lambda a,b:a+b, list1,list2)))
##Если в списках разное количество элекментов, то функция мап(лямбда) проделывается только до наименьшего общего индекса
#[22, 33, 44, 55]

#list_3 = [11,24,46,33]
#print(list(filter(lambda x:x%2!=0,list_3)))'''находим нечетные значения'''
#[11, 33]

#dictionary_places = [{'team':'Arsenal','place': 1},{'team':'Mancity','place': 2}]
#print(list(filter(lambda x: x['team']=='Mancity', dictionary_places))[0]['place'])
#2

'''Вызов модуля'''

from calculator.calc_funcs import read_input,calculate

num_1,num_2,sign = read_input()
print(num_1, sign, num_2, end=' = ')
result = calculate(num_1, num_2, sign)
if result is not None:
    print(result)