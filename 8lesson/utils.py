
def user_exists(name,user_lst):
    for user in user_lst:
        if user.name == name:
            return True
    return False


def log_correct(name,password,User_lst):
    for user in User_lst:
        if user.name == name and user.password == password:
            return True
    return False