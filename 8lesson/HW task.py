class Person():

    def __init__(self, name, age, place_of_birth,totem_animal):
        self.name = name
        self.age = age
        self.place_of_birth = place_of_birth
        self.totem_animal = totem_animal

    def introduce(self):
        print('- Hello, my name is %s. I am %d years old. My place of birth is %s.' %(self.name, self.age, self.place_of_birth))
        if self.totem_animal is None:
            print('I don`t have a pet')
        else:
            print('My pet is ', self.totem_animal)

    def age_person(self,grow_up = 1):
        self.age += grow_up

    def age_difference(self, other_person):
        differ = self.age - other_person.age
        print('- Age difference is ', differ)


    def fellow_countrymen(self, other_person):
        if self.place_of_birth == other_person.place_of_birth:
            print(' - Doesn`t matter, fellow countrymen! ')
        else:
            print('Villaribo and Villabadgo')

class Student(Person):
    def __init__(self, name, age, place_of_birth, totem_animal, university, diploma_topic, gpa, postgraduate_year):
        self.university = university
        self.diploma_topic = diploma_topic
        self.gpa = gpa
        self.postgraduate_year = postgraduate_year
        super().__init__(name, age, place_of_birth, totem_animal)

    def introduce(self):
        super().introduce()
        print('I study at the university %s. My diploma topic is %s. My gpa is %f. '
              'I plan to go to graduate school for %d years'%(self.university, self.diploma_topic,
                                                              self.gpa, self.postgraduate_year))

person1 = Person('Daniil', 30, 'Olenegorsk', totem_animal=None)
person1.introduce()
print('\n')
person2 = Person('Ekaterina', 30, 'Olenegorsk', 'dog Kasatka')
person2.introduce()
print('\n')
person1.age_person()
print('- Aged again. Now i am ', person1.age)
print('\n')
person1.age_difference(person2)
print('\n')
person2.fellow_countrymen(person1)
print('\n')

student1 = Student('Maksim', 27, 'Vsevolozhsk', 'turtle Boris', 'GUMRF', 'electric drive', 4.7, 3)
print(student1.name)
print(student1.age)
print(student1.place_of_birth)
print(student1.university)
print(student1.diploma_topic)
print(student1.gpa)
print(student1.postgraduate_year)
print('\n')
student1.introduce()
student1.age_person()
print('- Aged again. Now i am ', student1.age)

student1.age_difference(person2)

person2.fellow_countrymen(student1)