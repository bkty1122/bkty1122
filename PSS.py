import random

def Play():
    user = input("What's your choice? Paper Scissors Stone " )
    computer = random.choice(['P','S','R'])
    if user == computer:
        print('tie')
    elif win(user, computer):
        print('win')
    elif (user != 'P' or 'S' or 'R'):
        print('Invaild input')
    else:
        print('loss')

def win(me, O): #两个variables, 之后要放返上去play 果边
    if (me == 'P'and O == 'S') or (me == 'S'and O == 'P') or (me == 'R'and O == 'S'):
        return True
    else:
        return False

#写好，包含check data vaildity!!

Play()