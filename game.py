from player import Player
from human import Human
from computer import Computer

class Game:
    def __init__(self) -> None:
        pass

    greeting = """Welcome to Rock Paper Scissors Lizard Spock!

    Best out of three matches wins!

    Rules for game:
    Scissors cut Paper
    Paper covers Rock
    Rock crushes Scissors
    Rock crushes Lizard
    Lizard poisons Spock
    Spock smashes Scissors
    Scissors decapitates Lizard
    Lizard eats Paper
    Paper disproves Spock
    Spock vaporizes Rock
    """

    print(greeting)

    gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    gestures = input(f"""Player, please enter a number for your selection: 
    0. Rock
    1. Spock
    2. Paper
    3. Lizard
    4. Scissors
    """)

input = ("How many players? 1 or 2?")

#     print("")
#     print("Player chooses " + name + ".")
#     print("Computer chooses " + computer_name + ".")
#     print(winner)

def run_game():
    pass

if (human == ai):
    print("It's a tie!")

elif player_choice == 'Rock':
    if player_two == 'Scissors':
       print('Player wins! Rock breaks Scissors')
    else:
       print('Computer wins!')

elif player_one == 'Paper':
   if player_two == 'Rock':
       print('Computer wins! Paper covers Rock!')
   else: 
       print('Player wins!')

elif player_one == 'Scissors':
   if player_two == 'Paper':
      print('Player wins! Scissors cut Paper!')
   else:
      print('Computer wins!')
    
elif player_one == 'Rock':
    if player_two == 'Lizard':
       print('Player wins! Rock crushes Lizard')
    else:
       print('Player wins!')

elif player_one == 'Spock':
    if player_two == 'Scissors':
       print('Player wins! Spock smashes Scissors')
    else:
        print('Computer wins!')

elif player_one == 'Lizard':
    if player_two == 'Scissors':
       print('Computer wins! Scissors decapitates Lizard!')
    else:
        print('Player wins!')

elif player_one == 'Paper':
    if player_two =='Lizard':
        print('Computer wins! Lizard eats Paper!')
    else:
        print('Player wins!') 

elif player_one == 'Spock':
    if player_two == 'Paper':
        print('Computer wins! Paper disproves Spock')
    else:
        print('Player wins!')

elif player_one == 'Spock':
    if player_two == 'Rock':
        print('Player wins! Spock Vaporizes Rock')
    else:
        print('Computer wins!') 

# else:
#     pass
player = Player()
player.choices()
