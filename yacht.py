"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
from collections import defaultdict

YACHT = 12
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    singles = {ONES: 1, TWOS: 2, THREES: 3, FOURS: 4, FIVES: 5, SIXES: 6}
    big_straight_dices = {2, 3, 4, 5, 6}
    little_straight_dices = {1, 2, 3, 4, 5}

    if category == YACHT:
        if all(x == dice[0] for x in dice):
            return 50
        else:
            return 0
    elif category in singles:
        return sum(x for x in dice if x == singles.get(category))
    elif category == CHOICE:
        return sum(dice)
    elif category == LITTLE_STRAIGHT:
        if set(dice) == little_straight_dices:
            return 30
        else:
            return 0
    elif category == BIG_STRAIGHT:
        if set(dice) == big_straight_dices:
            return 30
        else:
            return 0
    elif category == FOUR_OF_A_KIND:
        dices = defaultdict(int)
        for x in dice:
            dices[x] += 1
        for key in dices:
            if dices.get(key) >= 4:
                return 4 * key
        return 0
    elif category == FULL_HOUSE:
        dices = defaultdict(int)
        dices_set = set()
        for x in dice:
            dices[x] += 1
            dices_set.add(x)
        if len(dices_set) == 2:
            for key in dices:
                if dices.get(key) == 3:
                    return sum(dice)
            return 0
        return 0
