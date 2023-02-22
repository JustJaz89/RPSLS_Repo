import random
from player import Player

class Computer(Player):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def choices(self):
        self.selected_gesture = random.randrange(0, 4)