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

input = ("How many players? 1 or 2?")

input = ("""Enter a number for your selection: 
1. Rock
2. Paper
3. Scissors
4. Lizard
5. Spock
""")

def number_to_name(number):
    if number == 1:
        return "Rock"
    elif number == 2:
        return "Paper"
    elif number == 3:
        return "Scissors"
    elif number == 4:
        return "Lizard"
    elif number == 5:
        return "Spock"
    else:
        return "Error"