# Пользователю предлагается поруководить командой PythonTeam и вывести ее на вершину 1 Дивизиона, для этого он может
# распределять очки улучшения между сезонами через специальную функцию, в которой будут задействованы методы класса Teams

import random
import itertools

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
Arsenal = Teams('Arsenal', 90, 90, 90)
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
PythonTeam = Teams('PythonTeam', 75, 75, 75)
Division_2_teams = [Liverpool, Brighton, AstonVilla,  Fulham,  PythonTeam]

def match(team_1, team_2):

    goal_1 = 0
    goal_2 = 0
    for i in range(6):
        gaol_attempt1 = team_1.goal_attempt()*random.randint(85, 115) / 100 - team_2.def_attempt()*random.randint(85, 115) / 100
        gaol_attempt2 = team_2.goal_attempt()*random.randint(85, 115) / 100 - team_1.def_attempt()*random.randint(85, 115) / 100
        if gaol_attempt1 > 0:
            goal_1 += 1
        else:
            pass
        if gaol_attempt2 > 0:
            goal_2 += 1
        else:
            pass
    if goal_1 > goal_2:
        points = 3
        team_1.bank_of_points(points)

    elif goal_2 > goal_1:
        points = 3
        team_2.bank_of_points(points)

    else:
        points = 1
        team_1.bank_of_points(points)
        team_2.bank_of_points(points)
    '''print(''f'{team_1.name}: {goal_1} - {goal_2} :{team_2.name}')'''

def championship(lst_of_teams):
    lst_of_matches = []
    for teams in itertools.combinations(lst_of_teams, 2):
        lst_of_matches.append(teams)
    '''print('Результаты матчей:')'''

    for i in range(len(lst_of_matches)):
        match(lst_of_matches[i][0], lst_of_matches[i][1])
        match(lst_of_matches[i][1], lst_of_matches[i][0])

'''def transfer_window:'''




num_of_seasons_from_user = int(input('Введите количество сезонов: '))
for num in range(num_of_seasons_from_user):
    championship(Division_1_teams)
    championship(Division_2_teams)

    # Находим вылетевшие команды из 1ДЕВИЗИОНА во 2ДЕВИЗИОН
    Division_1_teams.sort(key=lambda x: x.points, reverse=True)
    print('Команды на понижение в ' + str(num + 1) + 'сезоне:')
    print(Division_1_teams[-2].name)
    print(Division_1_teams[-1].name)

    # Находим поднявшиеся команды из 2ДЕВИЗИОНА в 1ДЕВИЗИОН
    Division_2_teams.sort(key=lambda x: x.points)
    print('Команды на повышение в ' + str(num + 1) + ' сезоне:')
    print(Division_2_teams[-1].name)
    print(Division_2_teams[-2].name)

    # Перемещаем команды между дивизионами внутри общего списка
    all_teams = Division_1_teams + Division_2_teams
    num_of_teams = len(all_teams)
    if num_of_teams%2 == 0:
        all_teams[int(num_of_teams/2)], all_teams[int(num_of_teams/2 + 1)] = all_teams[int(num_of_teams/2 + 1)], all_teams[int(num_of_teams/2)]
        all_teams[int(num_of_teams / 2 - 1)], all_teams[int(num_of_teams/2 + 2)] = all_teams[int(num_of_teams/2 + 2)], all_teams[int(num_of_teams/2 - 1)]
    else:
        all_teams[3], all_teams[4] = all_teams[5], all_teams[6] # условимся, что если добавляются новые команды,  то они заходят во второй дивизион
                                                                # в первом дивизионе пусть всегда будет 5 команд
    #вновь разбиваем на два дивизиона
    new_1st_div = all_teams[0:5]
    new_2nd_div = all_teams[5:]

    Division_2_teams.clear()
    Division_1_teams.clear()

    Division_1_teams += new_1st_div
    Division_2_teams += new_2nd_div
