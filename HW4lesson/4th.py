'''Дан список чисел. Определить количество элементов, которые больше двух своих соседей, и вывести
    количество таких элементов.'''

lst = list(map(int, input('введите список: ').split()))

def neighbors_list(lst):
    res = 0
    for i in range(1, len(lst[:-2])):
        if lst[i-1]<lst[i]>lst[i+1]:
            res+=1
        else:
            pass
    return(res)

print(neighbors_list(lst))








