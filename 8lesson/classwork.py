
class Rocket():
    def __init__(self):
        #Каждая рокета имеет координаты (x,y)
        self.x =0
        self.y =0

    def move_up(self):
        #Присваиваем рокете движение по у
        self.y+=1

#my_rocket = Rocket()
#print('Позиция по оси у: ',my_rocket.y)

#my_rocket.move_up()
#print('Позиция по оси у: ',my_rocket.y)

#my_rocket.move_up()
#print('Позиция по оси у: ',my_rocket.y)
'''Вывод:
Позиция по оси у:  0
Позиция по оси у:  1
Позиция по оси у:  2'''

##Создаем список объектов класса Роккет
##Применяется имеющийся метод к каждому объекту класса по отдельности, каждый обект хранится в отдельном месте
##и не связан с остальными
my_rockets = [Rocket() for i in range(0, 3)]
my_rockets[0].move_up()
my_rockets[0].move_up()
my_rockets[1].move_up()

for rocket in my_rockets:
    print('Позиция по оси у: ', rocket.y)

'''Вывод:
Позиция по оси у:  2
Позиция по оси у:  1
Позиция по оси у:  0'''

