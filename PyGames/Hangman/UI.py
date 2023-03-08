from Service import *


class UI:
    def __init__(self):
        self.service = Service()
        self.service.startGame()
        self.domain = self.service.domain

    def menu(self):
        print("1. Add a sentence")
        print("2. Start the game")
        print("3. Exit")
        choice = input("Your choice: ")
        if choice == "1":
            sentence = input("Enter the sentence: ")
            if self.service.addSentence(sentence):
                print("Sentence added!")
            else:
                print("Invalid sentence!")
        elif choice == "2":
            self.playGame()
        elif choice == "3":
            return

    def playGame(self):
        word_hangman = ["h______", "ha_____", "han____", "hang___", "hangm__", "hangma_", "hangman"]
        i = 0
        while True:
            self.service.printSentence()
            letter = input("Guess a letter: ")
            if len(letter) != 1 or not letter.islower() or not letter.isalpha():
                print("Invalid input! You need to input a small letter!")
                continue
            if self.service.guessLetter(letter):
                print("Correct!")
            else:
                print(word_hangman[i])
                i += 1
                print("Wrong!")
            print("Guesses left: " + str(self.domain.getGuessesLeft()))
            if self.domain.getGuessesLeft() == 0:
                print("You lost!")
                print("The sentence was: " + self.domain.getSentence())
                break
            if self.service.isSentenceGuessed():
                print("You won!")
                print("The sentence was: " + self.domain.getSentence())
                break
