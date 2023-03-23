'''1. Напишите программу, принимающую на вход слова через запятую и выводящую слова в алфавитном порядке.
 Используйте List comprehension.'''

random_order_words = input("Enter any words:").split(",")
not_random_order_words = sorted([w.upper() for w in random_order_words])
print(not_random_order_words)

