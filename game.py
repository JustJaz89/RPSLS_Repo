from typing import Self
from player import Player
from human import Human
from ai import Computer


class Game:
    def __init__(self):
        self.player_one = Human("Richard")
        self.player_two = Human("Marley")

    def display_greeting(self):
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

    def play_round(self):
        self.player_one.choices()
        self.player_two.choices()
        self.compare_gesture()

    def run_game(self):
        self.display_greeting()
        self.determine_game_mode()
        self.play_round() 

    def determine_game_mode(self):
        user_input = input("press1 for PvP, press 2 for PvC (computer) > ")
        if user_input =="1":
           self.player_two = Human("Marley")
        elif user_input =="2":
           self.player_two = Computer("Marley")

    def compare_gesture(self):
        if (self.player_one.selected_gesture == self.player_two.selected_gesture):
            print("It's a tie!")

        elif self.player_one.selected_gesture == 'Rock':
            if self.player_two.selected_gesture == 'Scissors':
                print(f'{self.player_one.name} wins! Rock breaks Scissors')
            elif self.player_two.selected_gesture == "Lizard":
                print(f'{self.player_one.name} wins! Rock crushes Lizard')
            else:
                print(f'{self.player_two.name} wins!')

        elif self.player_one.selected_gesture == 'Paper':
            if self.player_two.selected_gesture == 'Rock':
                print(f'{self.player_one.name} wins! Paper covers Rock!')
            elif self.player_two.selected_gesture == "Spock":
                print(f'{self.player_one.name} wins! Paper disproves Spock')
            else: 
                print(f'{self.player_two.name} wins!')

        elif self.player_one.selected_gesture == 'Scissors':
            if self.player_two.selected_gesture == 'Paper':
                print(f'{self.player_one.name} wins! Scissors cut Paper!')
            elif self.player_two.selected_gesture == "Lizard":
                print(f'{self.player_one.name} wins! Scissors decapitates Lizard')
            else:
                print(f'{self.player_two.name} wins!')

        elif self.player_one.selected_gesture == 'Spock':
            if self.player_two.selected_gesture == 'Scissors':
                print(f'{self.player_one.name} wins! Spock smashes Scissors')
            elif self.player_two.selected_gesture == 'Rock':
                print(f'{self.player_one.name} wins! Spock vaperizes Rock')
            else:
                print(f'{self.player_two.name} wins!')

        elif self.player_one.selected_gesture == 'Lizard':
            if self.player_two.selected_gesture == 'Spoke':
                print(f'{self.player_two.name} wins! Lizard poisons Spock!')
            elif self.player_two.selected_gesture == 'Paper':
                print(f'{self.player_one.name} wins! Lizard eats Paper')
            else:
                print(f'{self.player_one.name} wins!')


#     print("")
#     print("Player chooses " + name + ".")
#     print("Computer chooses " + computer_name + ".")
#     print(winner)




# else:
#     pass
# player = player_choice()
# player.computer()
