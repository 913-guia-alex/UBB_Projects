from Domain import *
from random import randint


class Service:
    def __init__(self):
        self.domain = Domain("")
        self.startGame()

    def getRandomSentence(self):
        file = open("sentences.txt", "r")
        sentences = file.readlines()
        number = randint(0, len(sentences) - 1)
        sentence = sentences[number]
        return sentence

    def printSentence(self):
        sentence = self.domain.getSentence()
        words = sentence.split(" ")
        for word in words:
            for i in range(len(word)):
                if i == 0 or i == len(word) - 1:
                    print(word[i], end="")
                elif word[i] in self.domain.getGuesses():
                    print(word[i], end="")
                else:
                    print("_", end="")
            print(" ", end="")
        print()

    def addSentence(self, sentence):
        words = sentence.split(" ")
        if len(words) < 2:
            print(words)
            return False
        for word in words:
            if len(word) <= 2:
                return False
            for i in range(len(word)):
                if not word[i].islower() or not word[i].isalpha():
                    return False
        file_object = open('sentences.txt', 'a')
        file_object.write(sentence)
        file_object.close()

    def guessLetter(self, letter):
        if self.domain.getGuessesLeft() == 0:
            return False
        if letter in self.domain.getGuesses():
            return False
        self.domain.getGuesses().append(letter)
        if letter not in self.domain.getSentence():
            self.domain.setGuessesLeft(self.domain.getGuessesLeft() - 1)
            return False
        return True

    def startGame(self):
        sentence = self.getRandomSentence()
        self.domain.setSentence(sentence)
        self.domain.setGuesses([])
        self.domain.setGuessesLeft(6)
        self.domain.setSentenceGuessed(False)

    def isSentenceGuessed(self):
        sentence = self.domain.getSentence()
        words = sentence.split(" ")
        for word in words:
            for i in range(len(word)):
                if i == 0 or i == len(word) - 1:
                    continue
                if word[i] not in self.domain.getGuesses():
                    return False
        self.domain.setSentenceGuessed(True)
        return True
