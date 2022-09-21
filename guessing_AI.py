from ast import Global, Store
import random
#https://docs.python.org/3/library/random.html random package functions


def guess_computer(x):
    feedback = ' '
    while feedback != 'C':
        low = 1
        high = x 
        guess = random.randint(low, high)
        feedback = input(f'Is your number equals to {guess}? H for higher, L for lower, C for correct. ')
        if feedback == 'H':
            high = guess + 1
        elif feedback == 'L':
            low = guess - 1
        elif feedback == 'C':
            print(f'The number is {guess}!')
            break
        else:
            print('invaild typing')


guess_computer(10)

