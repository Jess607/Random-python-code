class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.age = initialAge
        if initialAge>0:
            self.age = initialAge
        else:
            self.age=0
            print('Age is not valid, setting age to 0.')
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age <13:
            return 'you are young'
        elif self.age>=13 and self.age<18:
            return 'you are a teenager'
        else:
            return 'you are old'
    def yearPasses(self,t):
        self.age= int(self.age) + int(t)
        return self.amIOld()

        # Increment the age of the person in here

person_1=Person(16)
print(person_1.amIOld())
print(person_1.yearPasses(3))
#print(person_1.amIOld())
