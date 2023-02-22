import random

while('true'):
    player_one = input('Please enter the number for Rock(1), Paper(2), Scissors(3), Lizard(4), Spock(5): ')
    player_two = random.randint(1,5)

if player_two == 1:
   player_two = 'Rock'
elif player_two == 2:
    player_two = 'Paper'
elif player_two == 3:
    player_two = 'Scissors'
elif player_two == 4:
    player_two = 'Lizard'
elif player_two == 5:
    player_two = 'Spock'
else:
    print("Invalid input.")

if (player_one == player_two):
    print("It's a tie!")

elif player_one == 'Rock':
    if player_two == 'Scissors':
       print('player_one wins! Rock breaks Scissors')
    else:
       print('player_two wins!')

elif player_one == 'Paper':
   if player_two == 'Rock':
       print('player_two wins! Paper covers Rock!')
   else: 
       print('player_one wins!')

elif player_one == 'Scissors':
   if player_two == 'Paper':
      print('player_one wins! Scissors cut Paper!')
   else:
      print('player_two wins!')
    
elif player_one == 'Rock':
    if player_two == 'Lizard':
       print('player_one wins! Rock crushes Lizard')
    else:
       print('player_one wins!')

elif player_one == 'Spock':
    if player_two == 'Scissors':
       print('player_one wins! Spock smashes Scissors')
    else:
        print('player_two wins!')

elif player_one == 'Lizard':
    if player_two == 'Scissors':
       print('player_two wins! Scissors decapitates Lizard!')
    else:
        print('player_one wins!')

elif player_one == 'Paper':
    if player_two =='Lizard':
        print('player_two wins! Lizard eats Paper!')
    else:
        print('player_one wins!') 

elif player_one == 'Spock':
    if player_two == 'Paper':
        print('player_two wins! Paper disproves Spock')
    else:
        print('player_one wins!')

elif player_one == 'Spock':
    if player_two == 'Rock':
        print('player_one wins! Spock Vaporizes Rock')
    else:
        print('player_two wins!') 

# else:
#     pass