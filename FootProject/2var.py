# Двум игрокам (миллионерам, новоявленным владельцам клубов) предстоит попробовать вывести свои команды со дна второго дивизиона.
# Каждый сезон Вы можете тратить очки улчшения на атаку, полузащиту и оборону, чтобы сделать команду сильнее.
# Выберете себе по команде: PythonTeam или Gornyak. Рекомендуемое количество сезонов: 7-8 сезонов, но Вы можете попробовать и за 6.
# Тот, кто раньше приведет свою команду на вершину таблицы 1 ДИВИЗИОНА, тот победил. УДАЧИ!!!
import random
import itertools
from units.unit import championship

class Teams:

    def __init__(self, name, attack, midfield, defend, points=0):
        self.name = name
        self.attack = attack
        self.midfield = midfield
        self.defend = defend
        self.points = points


    #рассчет силы атаки
    def goal_attempt(self):
        power_attack = (self.attack + self.midfield)/2
        return power_attack

    #рассчет силы обороны
    def def_attempt(self):
        power_deffend = (self.midfield + self.defend)/2
        return power_deffend
    #заработанные очки
    def bank_of_points(self, points):
        self.points += points
        return self.points

    #улучшение атаки
    def transfer_to_attack(self, upgrade_attack):
        self.attack += upgrade_attack
        return self.attack

    #улучшение полузащиты
    def transfer_to_midfield(self, upgrade_midfield):
        self.midfield += upgrade_midfield
        return self.midfield

    #улучшение обороны
    def transfer_to_defend(self, upgrade_defend):
        self.defend += upgrade_defend
        return self.defend

# Создаем экземпляры класса Teams, а также список 1 ДИВИЗИОНА, в него записываем эти самые экзмепляры
Arsenal = Teams('Arsenal', 92, 91, 92)
ManCity = Teams('ManCity', 90, 92, 91)
Tottenham = Teams('Tottenham', 80, 80, 70)
Newcastle = Teams('Newcastle', 83, 88, 94)
ManUnited = Teams('ManUnited', 87, 88, 85)
Division_1_teams = [Arsenal, ManCity, Tottenham, Newcastle, ManUnited]

#Всё тоже самое для 2 ДИВИЗИОНА
Liverpool = Teams('Liverpool', 86, 82, 86)
Brighton = Teams('Brighton', 86, 84, 83)
AstonVilla = Teams('AstonVilla', 79, 83, 81)
Fulham = Teams('Fulham', 80, 73, 77)
PythonTeam = Teams('PythonTeam', 77, 75, 78)
Gornyak = Teams('Gornyak', 78, 75, 77)
Division_2_teams = [Liverpool, Brighton, AstonVilla,  Fulham,  PythonTeam, Gornyak]


# вводим и проверяем число введенных сезонов на правильность ввода
def check_input():
    while True:
        try:
            num_of_seasons_from_user = int(input('Введите количество сезонов: '))
            return num_of_seasons_from_user
        except ValueError:
            print('вводите число')
            continue

def transfer_window_pt():
    try:
        lst_of_upgrades_pt = input('распределите очки усиления для команды PythonTeam: ').split()
        nums_of_upgrades_pt = [int(i) for i in lst_of_upgrades_pt]
        att_up_pt, mid_up_pt, def_up_pt = nums_of_upgrades_pt
        if sum(nums_of_upgrades_pt) <= 10:
           PythonTeam.transfer_to_attack(att_up_pt)
           PythonTeam.transfer_to_midfield(mid_up_pt)
           PythonTeam.transfer_to_defend(def_up_pt)
        else:
            print('PythonTeam попали в трасферный бан, эти очки не защитаны, так как попытались потратить больше 10,АХАХАХАХ')
    except ValueError:
        print('Внимательно! Вводите числа!')
        return transfer_window_pt()

def transfer_window_gk():
    try:
        lst_of_upgrades_gk = input('распределите очки улучшения для команды Gornyak: ').split()
        nums_of_upgrades_gk = [int(i) for i in lst_of_upgrades_gk]
        att_up_gk, mid_up_gk, def_up_gk = nums_of_upgrades_gk
        if sum(nums_of_upgrades_gk) <= 10:
            Gornyak.transfer_to_attack(att_up_gk)
            Gornyak.transfer_to_midfield(mid_up_gk)
            Gornyak.transfer_to_defend(def_up_gk)
        else:
            print('Gornyak попали в трасферный бан, эти очки не защитаны, так как попытались потратить больше 10,АХАХАХАХ')
    except ValueError:
        print('Внимательно! Вводите числа!')
        return transfer_window_gk()


def print_the_table(div_1, div_2):
    print('РЕЗУЛЬТАТЫ В ПЕРВОМ ДИВИЗИОНЕ:')
    for i in range(len(div_1)):
        print(div_1[i].name, div_1[i].points)
    print('РЕЗУЛЬТАТЫ ВО ВТОРОМ ДИВИЗИОНЕ:')
    for i in range(len(div_2)):
        print(div_2[i].name, div_2[i].points)

# Стартуем, вводим количество сезонов

num_of_seasons_from_user = check_input()
for num in range(num_of_seasons_from_user):
    championship(Division_1_teams)
    championship(Division_2_teams)

    # Находим вылетевшие  и поднявшиеся команды, отсортировав по количеству набранных очков по убыванию внутри каждого из дивизионов
    Division_1_teams.sort(key=lambda x: x.points, reverse=True)
    Division_2_teams.sort(key=lambda x: x.points, reverse=True)
    print(num+1,' СЕЗОН:')
    print_the_table(Division_1_teams, Division_2_teams)
    if Division_1_teams[0].name == 'PythonTeam' or Division_1_teams[0].name == 'Gornyak':
        print('Поздравляем команду ' + Division_1_teams[0].name + '. Вы победили и стали чеспионом 1Дивизиона')
        break

    else:
        print('Команды на повышение в ' + str(num + 1) + 'сезоне:')
        print(Division_2_teams[0].name, Division_2_teams[1].name)
        print('Команды на понижение в ' + str(num + 1) + 'сезоне:')
        print(Division_1_teams[-2].name, Division_1_teams[-1].name)

        # Перемещаем команды между дивизионами внутри общего списка
        all_teams = Division_1_teams + Division_2_teams
        num_of_teams = len(all_teams)
        if num_of_teams%2 == 0:
            all_teams[int(num_of_teams/2 - 1)], all_teams[int(num_of_teams/2)] = all_teams[int(num_of_teams/2)], all_teams[int(num_of_teams/2 - 1)]
            all_teams[int(num_of_teams / 2 - 2)], all_teams[int(num_of_teams/2 + 1)] = all_teams[int(num_of_teams/2 + 1)], all_teams[int(num_of_teams/2 - 2)]
        else:
            all_teams[4], all_teams[5] = all_teams[5], all_teams[4]
            all_teams[3], all_teams[6] = all_teams[6], all_teams[3] # условимся, что если добавляются новые команды,  то они заходят во второй дивизион
                                                                    # в первом дивизионе пусть всегда будет 5 команд

        #стираем очки с прошлого сезона
        for team in all_teams:
            team.points = 0
        #вновь разбиваем на два дивизиона
        new_1st_div = all_teams[0:5]
        new_2nd_div = all_teams[5:]

        Division_2_teams.clear()
        Division_1_teams.clear()

        Division_1_teams += new_1st_div
        Division_2_teams += new_2nd_div
        # Вызываем функцию трансферное окно и распределяем очки улучшения
        if num+1 < num_of_seasons_from_user:
            print('Пришло время усилиться, потратьте очки усиления, чтобы в сумме было НЕ БОЛЕЕ 10, усилить можно АТАКУ,ПОЛУЗАЩИТУ И ОБОРОНУ, соответственно')
            print('Вводите целые числа через пробел')
            transfer_window_pt()
            transfer_window_gk()
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')
        else:
            print(' У Вас кончились денежки, а Вы так и не стали чемпионами.КОНЕЦ. Никто не победил')

