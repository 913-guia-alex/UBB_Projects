

class Domain:
    def __init__(self, sentence):
        self.sentence = sentence
        self.guesses = []
        self.guessesLeft = 6
        self.SentenceGuessed = False

    def getSentence(self):
        return self.sentence

    def getGuesses(self):
        return self.guesses

    def getGuessesLeft(self):
        return self.guessesLeft

    def getSentenceGuessed(self):
        return self.SentenceGuessed

    def setSentence(self, sentence):
        self.sentence = sentence

    def setGuesses(self, guesses):
        self.guesses = guesses

    def setGuessesLeft(self, guessesLeft):
        self.guessesLeft = guessesLeft

    def setSentenceGuessed(self, SentenceGuessed):
        self.SentenceGuessed = SentenceGuessed
