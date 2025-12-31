from random import randint
class die:
    def __init__(self):
       self.sides=20

    def roll_dice(self):
        for i in range(10):
          print(randint(1,self.sides))

pepper=die()

pepper.roll_dice()          