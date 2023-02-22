from player import Player
from human import Human
from ai import Computer

class Game:
    def __init__(self):

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

def run_game():
    if (Human == Computer):
        print("It's a tie!")

    elif Human == 'Rock':
        if Computer == 'Scissors':
            print('Player wins! Rock breaks Scissors')
        else:
            print('Computer wins!')

    elif Human == 'Paper':
        if Computer == 'Rock':
            print('Computer wins! Paper covers Rock!')
        else: 
            print('Player wins!')

    elif Human == 'Scissors':
        if Computer == 'Paper':
            print('Player wins! Scissors cut Paper!')
        else:
            print('Computer wins!')
        
    elif Human == 'Rock':
        if Computer == 'Lizard':
            print('Player wins! Rock crushes Lizard')
        else:
            print('Player wins!')

    elif Human == 'Spock':
        if Computer == 'Scissors':
            print('Player wins! Spock smashes Scissors')
        else:
            print('Computer wins!')

    elif Human == 'Lizard':
        if Computer == 'Scissors':
            print('Computer wins! Scissors decapitates Lizard!')
        else:
            print('Player wins!')

    elif Human == 'Paper':
        if Computer =='Lizard':
            print('Computer wins! Lizard eats Paper!')
        else:
            print('Player wins!') 

    elif Human == 'Spock':
        if Computer == 'Paper':
            print('Computer wins! Paper disproves Spock')
        else:
            print('Player wins!')

    elif Human == 'Spock':
        if Computer == 'Rock':
            print('Player wins! Spock Vaporizes Rock')
        else:
            print('Computer wins!') 

#     print("")
#     print("Player chooses " + name + ".")
#     print("Computer chooses " + computer_name + ".")
#     print(winner)

def run_game():
    run_game


# else:
#     pass
# player = player_choice()
# player.computer()
