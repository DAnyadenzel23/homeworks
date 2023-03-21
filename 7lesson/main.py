
n = int(input('Введите число: '))

def func1(n):
    lst = []
    while len(lst)<=n:
        for elem in range(n):
            if n<=0:
                print('число должно быть положительным')
            else:
                for p in range(elem):
                    lst.append(elem)
    return lst

print(func1(n))