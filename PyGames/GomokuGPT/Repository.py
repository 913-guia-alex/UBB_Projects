from random import *

class HangmanRepository:
    def __init__(self):
        self.words = ['python', 'java', 'javascript', 'c++', 'swift']
        shuffle(self.words,random)

    def get_random_word(self):
        return self.words[1]

    def add_word(self, word):
        self.words.append(word)

    def remove_word(self, word):
        self.words.remove(word)