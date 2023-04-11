
arsenal = {'attack': 88, 'midfield': 89, 'defend': 85, 'points': 0}
man_city = {'attack': 82, 'midfield': 92, 'defend': 89, 'points': 0}
newcastle = {'attack': 79, 'midfield': 84, 'defend': 93, 'points': 0}
tottenham = {'attack': 84, 'midfield': 84, 'defend': 84, 'points': 0}
man_united = {'attack': 85, 'midfield': 85, 'defend': 82, 'points': 0}
Devision_1_teams = {'Arsenal': arsenal, 'Man_city': man_city, 'Newcastle': newcastle, 'Tottenham': tottenham,
                    'Man_united': man_united}

aston_villa = {'attack': 88, 'midfield': 89, 'defend': 85, 'points': 0}
liverpool = {'attack': 88, 'midfield': 89, 'defend': 85, 'points': 0}
brighton = {'attack': 88, 'midfield': 89, 'defend': 85, 'points': 0}
brentford = {'attack': 88, 'midfield': 89, 'defend': 85, 'points': 0}
fulham = {'attack': 88, 'midfield': 89, 'defend': 85, 'points': 0}
Devision_2_teams = {'Aston_villa': aston_villa, 'Liverpool': liverpool, 'Brighton': brighton, 'Brentford': brentford,
                    'Fulham': fulham}

#Создали  словари 10 команд разбитых на два дивизиона

import random
import itertools

class Team:
    _att = 0
    _def = 0
    _mid = 0
    _point = 0

    def __init__(self, team_name):
        self._team_name = team_name
        self.give_attribute()

    def __str__(self):
        return self._team_name

    def give_attribute(self):
        all_teams_dict = Devision_2_teams | Devision_1_teams
        teams_dict = all_teams_dict[self._team_name]
        self._att = teams_dict['attack']
        self._def = teams_dict['defend']
        self._mid = teams_dict['midfield']
        self._point = teams_dict['points']

    #рассчет силы атаки
    def goal_attempt(self):
        power_attack = (self._att + self._mid)/2
        return power_attack

    #рассчет силы обороны
    def def_attempt(self):
        power_deffend = (self._mid + self._def)/2
        return power_deffend
    #заработанные очки
    def bank_of_points(self, points):
        self._point += points
        return self._point

def match(team1, team2):
    team_1 = Team(team1)
    team_2 = Team(team2)
    goal_1 = 0
    goal_2 = 0
    """phys_form_team_1 = random.randint(85, 115) / 100  # коэфициент физической формы и пр. случайных факторов
    phys_form_team_2 = random.randint(85, 115) / 100  # коэфициент физической формы и пр. случайных факторов
    не завожу в переменную отдельную, чтобы в матче присутстввовало больше элемента случайности"""
    for i in range(6):
        gaol_attempt1 = team_1.goal_attempt()*random.randint(80, 120) / 100 - team_2.def_attempt()*random.randint(80, 120) / 100
        gaol_attempt2 = team_2.goal_attempt()*random.randint(80, 120) / 100 - team_1.def_attempt()*random.randint(80, 120) / 100
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

    print(''f'{team1}: {goal_1} - {goal_2} :{team2}\n{team1} заработал уже {team_1._point} очков')



def championship(dict_of_teams):
    list_of_matches = []
    for teams in itertools.combinations(dict_of_teams, 2):
        list_of_matches.append(teams)
    print('Результаты матчей:')

    for i in range(len(list_of_matches)):
        match(str(list_of_matches[i][0]), str(list_of_matches[i][1]))


championship(Devision_1_teams)


