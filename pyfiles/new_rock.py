import random

user= input('Enter:')
comp= random.choice(['r', 's', 'p'])
def guess():
    while user== comp:
        return 'tie b'
    while user!= comp:
        if user=='r' and comp=='p':
            return 'I win'
        elif user=='r' and comp=='s':
            return 'You  win'
        elif user=='p' and comp=='r':
            return 'You win'
        elif user=='s' and comp=='r':
            return 'I win'
        elif user=='p' and comp=='s':
            return 'I win'
        else:
            return 'You win'

print(guess())
