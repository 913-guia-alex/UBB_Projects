from Repository import *
from Service import *

class HangmanUI:
    def __init__(self, service):
        self.service = service

    def start(self):
        self.service.start_game()
        while self.service.hangman.status == 'playing':
            print(self.service.display())
            letter = input("Guess a letter: ")
            result = self.service.guess(letter)
            if result == 'win':
                print("You win!")
                break
            elif result == 'lose':
                print("You lose!")
                break
            elif result == 'already guessed':
                print("You already guessed that letter.")
            elif result == 'correct':
                print("Correct!")
            elif result == 'incorrect':
                print("Incorrect.")


