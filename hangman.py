import random

def Play():
    x = ' '
    word = random.choice(read_file(x))
    word_uppercase = word.upper()
    word_data = set(word_uppercase)
    used_letter = set()

    while len(word_data) > 0:
        print ('You have used these letters:',' '.join(used_letter))
        word_list = [ x if x in used_letter else '-' for x in word_uppercase ]
        print('Current word: ',' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in word_data - used_letter:
            used_letter.add(user_letter)
        elif user_letter in used_letter:
            print(f'You have used {user_letter}.')
        if len(used_letter) == len(word_data):
            print(f'You win! the word is {word_uppercase}!')
            break

def read_file(i): #import words from wordlist.txt
    myfile = open('wordlist.txt','r')
    data = myfile.read()
    word_of_the_list = data.split('\n') 
    #create a list by spliting \n
    #ref to https://www.geeksforgeeks.org/how-to-read-text-file-into-list-in-python/ 
    myfile.close()
    return word_of_the_list

Play()