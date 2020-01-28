import string
import random

robot_names = set()


class Robot:
    ROBOT_NAME_LETTERS = 2
    ROBOT_NAME_NUMBERS = 3

    def __init__(self):
        self.name = ""
        self.create_new_name()

    def create_new_name(self):
        upper_alphabet = string.ascii_uppercase
        naming_successful = False
        while not naming_successful:
            self.name = ""
            for i in range(self.ROBOT_NAME_LETTERS):
                self.name += random.choice(upper_alphabet)
            for i in range(self.ROBOT_NAME_NUMBERS):
                self.name += str(random.randrange(10))
            if self.name not in robot_names:
                robot_names.add(self.name)
                naming_successful = True
        print(self.name)
        return self.name

    def reset(self):
        self.create_new_name()
