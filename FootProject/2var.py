import random
import itertools

class Teams:
    '''lst_of_teams = []'''
    def __init__(self, name, attack, midfield, defend, points=0, ):
        self.name = name
        self.attack = attack
        self.midfield = midfield
        self.defend = defend
        self.points = points
        '''Teams.lst_of_teams.append(self)'''
    '''def __str__(self):
        return "{}{}{}{}{}".format(self.name,self.attack,self.midfield,self.defend,self.points)'''

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

    '''def print_the_table(self):'''

def match(team_1,team_2):
    '''team_1 = Teams(team1)
    team_2 = Teams(team2)'''
    goal_1 = 0
    goal_2 = 0
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
    print(''f'{team_1.name}: {goal_1} - {goal_2} :{team_2.name}\n{team_1.name} заработал уже {team_1.points} очков\n{team_2.name} заработал уже {team_2.points} очков')

def championship(list_of_teams):
    list_of_matches = []
    for teams in itertools.combinations(list_of_teams, 2):
        list_of_matches.append(teams)
    print('Результаты матчей:')
    print(list_of_matches)
    for i in range(len(list_of_matches)):
        match(str(list_of_matches[i][0]), str(list_of_matches[i][1]))








Arsenal = Teams('Arsenal',88, 90, 90)
ManCity = Teams('ManCity',90,92,91)
Tottenham = Teams('Tottenham',80,80,70)


#match(Arsenal, Tottenham)
#print(Teams.lst_of_teams)

championship(Teams.lst_of_teams)