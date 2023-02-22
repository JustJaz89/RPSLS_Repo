import random

player_choices = ["0", "1", "2", "3", "4"]

class Player():
    def __init__(self) -> None:
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
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
                #player_two = random.randint(0,4)
       # if player_one in player_choices:
            #print('Your move!')
    

