import datetime

class Passport():
    def __init__(self,name,sname,birthd,country,num_pus):
        self.name = name
        self.sname = sname
        self.birthd = birthd
        self.country = country
        self.num_pus = num_pus
    def print_inf(self):
        print('name: ',self.name,'sname: ', self.sname, 'date of birth: ',self.birthd, 'country of birth: ', self.country, 'num of passport: ',self.num_pus)


class ForeignPassport(Passport):
    def __init__(self,name,sname,birthd,country,num_pus,visa,ex_date):
        super().__init__(name,sname,birthd,country,num_pus)
        self.visa = visa
        self.ex_date = ex_date

    def print_inf(self):
        super().print_inf()
        print('visa: ', self.visa)

    def days_before(self):
        now = datetime.date.now()
        days_to_end_visa = self.ex_date - now
        print(days_to_end_visa)


    def next_visa(self):
        list_of_visavar = [7, 30, 180,365,730,1460]
        for item in list_of_visavar:
            if item > days_to_end_visa:
                print("Next Visa for: ", item+1 ,'days')



list_of_pasport = []

for item in Passport:
    list_of_pasport.append(item)
