import random 

#user= int(input('Enter:'))
comp= random.randint(0,100)
lis=[]
for i in range(5):
    lis.append(int(input('Enter:')))
def random():
    if comp in lis:
        return ('comp is', comp, 'you are correct')

    else:
        return ('sorry, wrong number comp is', comp)


print(random())
