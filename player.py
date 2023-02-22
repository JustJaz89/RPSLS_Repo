import random

player_choices = ['0,1,2,3,4']

class Player():
    def __init__(self) -> None:
        self.gestures = ['Rock', 'paper', 'Scissors', 'Lizad', 'Spock']
        self.selected_gesture = ''
    def choices(self):      
        Player_is_running = True
        while Player_is_running == True:
            player_choices = input('please enter rock(0), paper(1), scissors(2), lizard(3), spock(4): ')
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
                #player_two = random.randint(0,4)
       # if player_one in player_choices:
            #print('Your move!')
    
    
player = Player()
player.choices()

'''
if (player_one == player_two):
    print("It's a tie!")

elif player_one == 'Rock':
    if player_two == 'Scissors':
       print('Player_one wins! Rock breaks Scissors')
    else:
       print('Player_two wins!')

elif player_one == 'Paper':
   if player_two == 'Rock':
       print('Player_two wins! Paper covers Rock!')
   else: 
       print('Player_one wins!')

elif player_one == 'Scissors':
   if player_two == 'Paper':
      print('Player_one wins! Scissors cut Paper!')
   else:
      print('Player_two wins!')
    
elif player_one == 'Rock':
    if player_two == 'Lizard':
       print('Player_one wins! Rock crushes Lizard')
    else:
       print('Player_one wins!')

elif player_one == 'Spock':
    if player_two == 'Scissors':
       print('player_one wins! Spock smashes Scissors')
    else:
        print('Player_two wins!')

elif player_one == 'Lizard':
    if player_two == 'Scissors':
       print('player_two wins! Scissors decapitates Lizard!')
    else:
        print('Player_one wins!')

elif player_one == 'Paper':
    if player_two =='Lizard':
        print('player_two wins! Lizard eats Paper!')
    else:
        print('player_one wins!') 

elif player_one == 'Spock':
    if player_two == 'Paper':
        print('Player_two wins! Paper disproves Spock')
    else:
        print('player_one wins!')

elif player_one == 'Spock':
    if player_two == 'Rock':
        print('player_one wins! Spock Vaporizes Rock')
    else:
        print('Player_two wins!') 

print('your choice: ' + 'player_one' + "\n player_two's choice: " + player_two + "\nThank you for playing!")
print("Do you want to play again? (Y/N)")
ans = input()

if ans == 'n' or ans == 'N':
   break
'''