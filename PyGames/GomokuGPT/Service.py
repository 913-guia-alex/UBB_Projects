from Domain import *
from random import *

class HangmanService:
    def __init__(self, repository):
        self.repository = repository
        self.hangman = None

    def start_game(self):
        word = self.repository.get_random_word()
        self.hangman = Hangman(word)

    def guess(self, letter):
        return self.hangman.guess(letter)

    def display(self):
        return self.hangman.display()

