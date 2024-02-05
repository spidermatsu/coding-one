#dice roller

# Make a dice roller program using Object Oriented Concepts. The user should be able to define:

#     how many sides there are on a dice
#     how many dice there are
#     how many times the dice are rolled

# Add any additional features you think such an application would need.


import random

class dice:
    def __init__(self, diceSides=6, diceCount=1):
        self.diceSides = diceSides
        self.diceCount = diceCount

    def roll(self):
        return [random.randint(1, self.diceSides) for _ in range(self.diceCount)]

def main():
    #input
    diceSides = input("how many sides on dice?")
    diceCount = input("how many dice are there?")
    diceRolls = input("how many rolls?")
    dice_roller = dice(diceSides, diceCount)

    for i in range(int(diceRolls)):
        roll = dice_roller.roll()
        print(roll)

main()