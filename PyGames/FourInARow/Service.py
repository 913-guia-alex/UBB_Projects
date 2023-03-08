# create the Service class to handle the game logic:
from Domain import *
import random


class Service:
    def __init__(self):
        self.domain = ConnectFour()
        self.StartGame()

    def is_valid_move(self, column):
        if column < 0 or column > 6:
            return False
        if self.domain.board[0][column] != ' ':
            return False
        return True

    def check_player_won(self):
        if self.check_row() or self.check_col() or self.check_diag() or self.check_diag2() :
            self.domain.player_winner = True

    def check_computer_won(self):
        if self.check_row() or self.check_col() or self.check_diag() or self.check_diag2():
            self.domain.computer_winner = True

    # function that checks if there are 4 X in a row or 4 O in a row
    def check_row(self):
        for i in range(6):
            for j in range(4):
                if self.domain.board[i][j] == self.domain.board[i][j + 1] == self.domain.board[i][j + 2] == \
                        self.domain.board[i][j + 3] != ' ':
                    return True
        return False

    # function that checks if there are 4 X in a column or 4 O in a column
    def check_col(self):
        for i in range(7):
            for j in range(3):
                if self.domain.board[j][i] == self.domain.board[j + 1][i] == self.domain.board[j + 2][i] == \
                        self.domain.board[j + 3][i] != ' ':
                    return True
        return False

    # function that checks if there are 4 X in a diagonal or 4 O in a diagonal
    def check_diag(self):
        for i in range(3):
            for j in range(4):
                if self.domain.board[i][j] == self.domain.board[i + 1][j + 1] == self.domain.board[i + 2][j + 2] == \
                        self.domain.board[i + 3][j + 3] != ' ':
                    return True
        return False

    # function that checks if there are 4 X on the other diagonal or 4 O on the other diagonal
    def check_diag2(self):
        for i in range(3):
            for j in range(4):
                if self.domain.board[i][j + 3] == self.domain.board[i + 1][j + 2] == self.domain.board[i + 2][j + 1] == \
                        self.domain.board[i + 3][j] != ' ':
                    return True
        return False

    # function that starts the game:
    def StartGame(self):
        self.board = [[' ' for i in range(7)] for j in range(6)]
        self.player = 'X'
        self.computer = 'O'
        self.player_winner = False
        self.computer_winner = False
        self.move_count = 0
        self.winner = None
        self.turn = 'X'
        self.count = 0
        self.player_turn = False
        self.computer_turn = True
        self.tie = False
