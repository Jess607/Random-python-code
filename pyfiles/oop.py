class Employee:
    raise_amt=1.04
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.email= first + last + '@company.com'
        self.full= first +  ' ' + last
        self.pay=pay

    def percent(self):
        return self.pay/100

    def get_raise(self):
        return self.pay * self.raise_amt

    @classmethod
    def setRaiseAmt(cls, amount):
        cls.raise_amt = amount

class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang):
        super().__init__( first, last, pay)
        self.prog_lang=prog_lang

    def __repr__(self):
        return '{}-{}'. format(self.first, self.last)

    def __str__(self):
        return '{}-{}'. format(self.first, self.last)

    def __add__(self, other):
        return self.pay + other.pay

emp_1=Employee('Jess', 'Ogwu', 50000)
emp_2=Employee('Jess', 'Ogwu', 60000)
emp_3=Developer('Jey', 'Ghy', 20999, 'python')
emp_4=Developer('Jey', 'Ghy', 20999, 'python')

emp_2.raise_amt=1.05

# class method may be used to set variables for diff. classes


print(emp_1.percent())
print(emp_2.get_raise())
print(emp_3)
print(emp_3 + emp_4)

Employee.setRaiseAmt(1.05)

print(Employee.raise_amt)
