'''Дан список упорядоченный по неубыванию. Определить сколько в нем различных элементов'''

lst = list(map(int, input('введите список: ').split()))

def cool_list(lst):
    res = 1
    for i in range(0, len(lst)-1):
        if lst[i] != lst[i+1]:
            res+=1
        else:
            pass
    return(res)

print(cool_list(lst))