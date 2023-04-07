"""
Напишите класс Character обладающий 3 характеристиками: атака, здоровье, уклоенине
FIGHTER = {"health": 5, "attack": 3, "dodge": 1}
THIEF = {"health": 2, "attack": 3, "dodge": 4}
MAGE = {"health": 1, "attack": 5, "dodge": 4}
TYPES = {"fighter": FIGHTER, "thief": THIEF, "mage": MAGE}

Класс имеет следующие методы:
Распределение атрибутов как описано выше: character_1 = Character("fighter")
Атака
Получение урона в случае если увернуться не удалось.
Уклонение: каждое очко уклонения умножается на 5. Результат уклонения зависит от рандомно генерируемого числа
от 0 до 100. Если это число меньше или равно навыка уклонения, то герой уклоняется от атаки.
Смерть: если здоровье меньше 1.

Напишите функцию которая заставит сразиться разных героев друг с другом 100 раз. Выведите счет.
"""

from random import randint



FIGHTER = {"health": 5, "attack": 3, "dodge": 1}
THIEF = {"health": 2, "attack": 3, "dodge": 4}
MAGE = {"health": 1, "attack": 5, "dodge": 4}
TYPES = {"fighter": FIGHTER, "thief": THIEF, "mage": MAGE}

class Character():

    _health = 0
    _attack = 0
    _dodge = 0
    def __init__(self, char_type):
       self.char_type = char_type
       self.distribution()

    def distribution(self):
        typ_dict = TYPES[self.char_type]
        self._health = typ_dict['health']
        self._attack = typ_dict['attack']
        self._dodge = typ_dict['dodge']

    def attack(self,other_guy):
        

    def take_dam(self):    # Получение урона


    def dod(self):    #Уклонение
        x = randint(0,100)
        if self._dodge*5 >= x:


