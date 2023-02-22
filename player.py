import random

class Player:
    def __init__(self, name):
        self.name = name

    def number_to_name(number):
        if number == 0:
            return "Rock"
        elif number == 1:
            return "Spock"
        elif number == 2:
            return "Paper"
        elif number == 3:
            return "Lizard"
        elif number == 4:
            return "Scissors"
        else:
            return "Enter a valid number, 0-4: "

    def rpsls(player_choice):
        print("")
        print("Player chooses " + player_choice)
        player_number = number_to_name(player_choice)
        computer_number = random.randrange(0, 5)
        computer_choice = number_to_name(computer_number)
        print("Computer chooses " + computer_choice)

        if computer_number - player_number > 0:
            if computer_number - player_number > 2:
                print("Player wins!")
            elif computer_number - player_number <= 2:
                print("Computer wins!")
        elif computer_number - player_number < 0:
            if (computer_number - player_number) %5 > 2:
                print("Player wins!")
            elif computer_number - player_number <= 2:
                print("Computer wins!")
        elif computer_number == player_number:
            print("Player and computer tie!")
        else:
            print("Invalid input.")

# rpsls(0)
# rpsls(1)
# rpsls(2)
# rpsls(3)
# rpsls(4)