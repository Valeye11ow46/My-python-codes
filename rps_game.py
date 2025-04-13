import random
while True:
    possible_actions = ['rock', 'paper', 'scissors']
    computer_action = random.choice(possible_actions)
    print('The choices are:\n rock \n paper\n scissors')
    user_action= input('Enter your choice: ')
    if user_action == computer_action:
        print(f'you picked:{user_action}\nyour opponent picked {computer_action}')
    elif user_action == 'rock':
        if computer_action == 'scissors':
            print('rock beats scissors, you win')
        else:
            print('paper beats rock, you lose')
    elif user_action == 'paper':
        if computer_action == 'rock':
            print('paper covers rock, you win')
        else:
            print('scissors cuts paper, you lose')
    elif user_action == 'scissors':
        if computer_action == 'paper':
            print('scissors cuats paper, you win')
        else:
            print('rock samshes scissors, you lose')
    thanks = print('thanks for playing')
    next_game=input('Would you like to play again yes/no: ')
    if next_game == 'no':
        break
    else:
        print('next game')

