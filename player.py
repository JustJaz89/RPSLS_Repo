import random

class Player():
    def __init__(self):
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.selected_gesture = ""
    
    def choices(self):
        player_is_running = True
        while player_is_running == True:
            player_choice = input('Please enter the number for Rock(1), Paper(2), Scissors(3), Lizard(4), Spock(5): ')
            if player_choice == "0":
                self.selected_gesture = 'Rock'
                break
            elif player_choice == "1":
                self.selected_gesture = 'Paper'
                break
            elif player_choice == "2":
                self.selected_gesture = 'Scissors'
                break
            elif player_choice == "3":
                self.selected_gesture = 'Lizard'
                break
            elif player_choice == "4":
                self.selected_gesture = 'Spock'
                break
            # player_two = random.randint(0, 4)
        # if player_one in player_choices:
        #     print("Your move!")

player = Player()
player.choices()

# else:
#     print("Invalid input.")