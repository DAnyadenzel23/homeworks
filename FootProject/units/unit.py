import random
import itertools
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