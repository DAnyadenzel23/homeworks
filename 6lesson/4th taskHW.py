'''Используя random.sample сгенерируйте список случайных элементов. Используйте List comprehension.'''
import random

a = input('entar any elements: ').split( )
print(a)
b = [elem for elem in random.sample(a, 3)]
print(b)