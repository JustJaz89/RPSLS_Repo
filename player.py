import random

class Player():
    def __init__(self):
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.selected_gesture = ""

player_choices = ["0", "1", "2", "3", "4"]

class Player():
    def __init__(self) -> None:
        self.gestures = ['Rock', 'paper', 'Scissors', 'Lizard', 'Spock']
        self.selected_gesture = ''
    def choices(self):      
        Player_is_running = True
        while Player_is_running == True:
            player_choices = input('Please enter number for Rock(0), Paper(1), Scissors(2), Lizard(3), Spock(4): ')
            if player_choices == '0':
                self.selected_gesture = 'Rock'
                break
            elif player_choices == '1':
                self.selected_gesture = 'Paper'
                break
            elif player_choices == '2':
                self.selected_gesture = 'Scissors'
                break
            elif player_choices == '3':
                self.selected_gesture = 'Lizard'
                break
            elif player_choices == '4':
                self.selected_gesture = 'Spock'
                break    
    
player = Player()
player.choices()

# if (player_one == player_two):
#     print("It's a tie!")

# elif player_one == 'Rock':
#     if player_two == 'Scissors':
#        print('player_one wins! Rock breaks Scissors')
#     else:
#        print('player_two wins!')

# elif player_one == 'Paper':
#    if player_two == 'Rock':
#        print('player_two wins! Paper covers Rock!')
#    else: 
#        print('player_one wins!')

# elif player_one == 'Scissors':
#    if player_two == 'Paper':
#       print('player_one wins! Scissors cut Paper!')
#    else:
#       print('player_two wins!')

# elif player_one == 'Spock':
#     if player_two == 'Scissors':
#        print('player_one wins! Spock smashes Scissors')
#     else:
#         print('player_two wins!')

# elif player_one == 'Lizard':
#     if player_two == 'Scissors':
#        print('player_two wins! Scissors decapitates Lizard!')
#     else:
#         print('player_one wins!')

# elif player_one == 'Paper':
#     if player_two =='Lizard':
#         print('player_two wins! Lizard eats Paper!')
#     else:
#         print('player_one wins!') 

# elif player_one == 'Spock':
#     if player_two == 'Paper':
#         print('player_two wins! Paper disproves Spock')
#     else:
#         print('player_one wins!')

# elif player_one == 'Spock':
#     if player_two == 'Rock':
#         print('player_one wins! Spock Vaporizes Rock')
#     else:
#         print('player_two wins!') 