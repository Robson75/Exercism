from random import randint
import math


class Character:
    def __init__(self):
        self.NR_OF_ABILITIES = 6
        self. strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.set_ability_levels(self.NR_OF_ABILITIES)
        self.hitpoints = set_hitpoints(self.constitution)
        print(self.wisdom)

    def set_ability_levels(self, nr):
        ability_levels = [self.ability() for _ in range(nr)]
        self.strength = ability_levels[0]
        self.dexterity = ability_levels[1]
        self.constitution = ability_levels[2]
        self.intelligence = ability_levels[3]
        self.wisdom = ability_levels[4]
        self.charisma = ability_levels[5]

    def ability(self):
        # throw 4 dices and return the sum of the highest 3
        dices = [randint(1, 6) for _ in range(4)]
        dices_min = min(dices)
        return sum(dices) - dices_min


def set_hitpoints(constitution):
    return 10 + modifier(constitution)


def modifier(constitution):
    return math.floor((constitution - 10) / 2)






