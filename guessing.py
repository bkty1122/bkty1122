import random
#https://docs.python.org/3/library/random.html random package functions

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 #pre-define guess as 0 to prevent guest randomly input the same value as random number.
    #Since random_number cannnot smaller than 1, guess will not equal to random_number
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}:')) #f-string: can print int as string by simly adding {}
        if guess < random_number:
            print('Your number is too low.')
        elif guess > random_number:
            print('Your number is too high.')
    print(f'Good. You guess correct! The correct number is {x}!')

guess(10) #define number of x in guess function, and start the program.
