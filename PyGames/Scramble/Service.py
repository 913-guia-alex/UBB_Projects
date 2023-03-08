import random
from Domain import *

class Service:
    def __init__(self, repository):
        self.repository = repository

    def start_game(self):
        word_or_sentence = self.repository.get_random_entry()
        scrambled_sentence = self.scramble_sentence(word_or_sentence)
        score = len(scrambled_sentence) - scrambled_sentence.count(" ")
        game = Scramble(scrambled_sentence, score)
        return game

    def scramble_sentence(self, sentence):
        """
        Scrambles the sentence by shuffling the letters in each word,
        except for the first and last letters.
        """
        words = sentence.split(" ")
        scrambled_words = []
        for word in words:
            if len(word) < 3:
                scrambled_words.append(word)
            else:
                first_letter = word[0]
                last_letter = word[-1]
                middle_letters = list(word[1:-1])
                random.shuffle(middle_letters)
                scrambled_word = first_letter + "".join(middle_letters) + last_letter
                scrambled_words.append(scrambled_word)
        scrambled_sentence = " ".join(scrambled_words)
        return scrambled_sentence

    def swap_letters(self, game, word1, letter1, word2, letter2):
        """
        Swaps the letters at the given indices in the sentence.
        """
        words = game.scrambled_sentence.split(" ")
        w1_index = words.index(word1)
        w2_index = words.index(word2)

        if letter1 > len(word1) or letter2 > len(word2):
            raise ValueError("Invalid letter index")
        if w1_index == w2_index:
            raise ValueError("Letters are in the same word")

        word1_list = list(word1)
        word2_list = list(word2)
        word1_list[letter1], word2_list[letter2] = word2_list[letter2], word1_list[letter1]
        words[w1_index] = "".join(word1_list)
        words[w2_index] = "".join(word2_list)
        game.scrambled_sentence = " ".join(words)
        game.score -= 1
        return game

    def check_win(self, game, original_sentence):
        """
        Check if the scrambled sentence is the same as the original sentence
        """
        if game.scrambled_sentence == original_sentence:
            return True
        else:
            return False

    def check_lose(self, game):
        """
        Check if the score is equal to 0
        """
        if game.score == 0:
            return True
        else:
            return False
