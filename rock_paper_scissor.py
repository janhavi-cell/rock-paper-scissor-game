import random

item_list = ['rock','paper','scissor']

user_choice = input('Enter your choice = ')
computer_choice = random.choice(item_list)

print(f'User choice = {user_choice}, Computer choice = {computer_choice}')

if user_choice == computer_choice:
    print('Both chooses same: Match Tie')

elif user_choice == 'rock':
    if computer_choice == 'paper':
        print('Paper covers Rock = Computer wins')
    else:
        print('Rock smashes Scissor = You win')

elif user_choice == 'paper':
    if computer_choice == 'scissor':
        print('Scissor cuts Paper = Computer wins')
    else:
        print('Paper covers Rock = You win')

elif user_choice == 'scissor':
    if computer_choice == 'paper':
        print('Scissor cuts paper = You win')
    else:
        print('Rock smashes Scissor = Computer wins')

