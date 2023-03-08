class Hangman:
    def __init__(self, word):
        self.word = word
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.status = 'playing'

    def guess(self, letter):
        if letter in self.guessed_letters:
            return 'already guessed'
        if self.status != 'playing':
            return 'game over'
        self.guessed_letters.add(letter)
        if letter in self.word:
            if set(self.word) == self.guessed_letters:
                self.status = 'win'
                return 'win'
            else:
                return 'correct'
        else:
            self.incorrect_guesses += 1
            if self.incorrect_guesses >= 6:
                self.status = 'lose'
                return 'lose'
            else:
                return 'incorrect'

    def display(self):
        display = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += '_'
        return display
