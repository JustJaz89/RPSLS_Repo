import player
import human
import ai

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

# def number_to_name(number):
#     if number == 0:
#         return "Rock"
#     elif number == 1:
#         return "Spock"
#     elif number == 2:
#         return "Paper"
#     elif number == 3:
#         return "Lizard"
#     elif number == 4:
#         return "Scissors"
#     else:
#         return "Enter a valid number, 0-4: "

def rpsls(name):
    import random

    player_number = number_to_name(name)
    computer_number = random.randrange(5)
    difference = (player_number - computer_number) & 5

    if difference == 0:
        winner = "It's a tie!"
    elif difference < 3:
        winner = "Player wins!"
    else:
        winner = "Computer wins!"

    computer_name = number_to_name(computer_number)

    print("")
    print("Player chooses " + name + ".")
    print("Computer chooses " + computer_name + ".")
    print(winner)

def run_game():
    pass
