class Person:
    def __init__(self):
        self.name=None
        self.position=None
        self.date_of_birth=None
        
    def __str__(self):
        return f'{self.name} born on {self.date_of_birth} ' + \
            f'works at {self.position}'
    
    @staticmethod
    def new():
        #print('new')
        return PersonBuilder()
    
class PersonBuilder:
    def __init__(self):
        #print('Here')
        self.person=Person()
        
    def build(self):
        #print('build')
        return self.person
    
class PersonInfoBuilder(PersonBuilder):
    def called(self,name):
        #print('called')
        self.person.name=name
        return self
    
class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self,position):
        #print('works')
        self.person.position=position
        return self
    
class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self,date_of_birth):
        #print('dob')
        self.person.date_of_birth=date_of_birth
        return self
    
pb=PersonBirthDateBuilder()
me=pb\
    .called('Harsh')\
    .works_as_a('Lead Software Engineer')\
    .born('10/6/1990')\
    .build()
    
print(me)        