def read_input():
    inp_enter = input().split()
    num_1 = inp_enter[0]
    num_2 = inp_enter[1]
    sign = inp_enter[2]
    return int(num_1), int(num_2), sign

def calculate(num_1,num_2,sign):
    if sign =='+':
         return num_1+num_2
    elif sign == '-':
        return num_1-num_2
    elif sign =='*':
        return num_1*num_2
    elif sign == '/':
        if num_2 ==0:
            print('чумачечий')
        else:
            return num_1/num_2


if __name__=='__main__':
    read_input()
