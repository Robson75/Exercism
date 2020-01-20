# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.masked_word = ['_' for _ in word]
        self.characters_remaining = word
        self.word = word
        self.letters_left = len(word)

    def guess(self, char):

        print(self.masked_word)
        if self.get_status() == STATUS_WIN:
            raise ValueError("You already got it right :)")
        elif self.get_status() == STATUS_LOSE:
            raise ValueError("You are already dead :(")
        else:
            if char in self.characters_remaining:
                occurrences = self.word.count(char)
                self.letters_left -= occurrences
                indices = [i for i, a in enumerate(self.word) if a == char]

                self.remove_character(char)
                for i in indices:
                    self.change_masked_word(i, char)
            else:
                self.remaining_guesses -= 1
        if self.letters_left == 0:
            self.status = STATUS_WIN
        elif self.remaining_guesses == -1:
            self.status = STATUS_LOSE
        print(self.get_status())

    def remove_character(self, char):
        self.characters_remaining = self.characters_remaining.replace(char, "")
        print("remaining: " + self.characters_remaining)

    def change_masked_word(self, index, char):
        self.masked_word[index] = char
        print("changed " + str(self.masked_word))

    def get_masked_word(self):
        return ''.join(self.masked_word)

    def get_status(self):
        return self.status


if __name__ == '__main__':
    hangman = Hangman("test")
    # hangman.guess("t")
