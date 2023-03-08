from Domain import *


class Service:
    def __init__(self):
        self.domain = ChaosAndOrder()
        self.StartGame()

    def StartGame(self):
        self.domain.player_turn = False
        self.domain.computer_turn = True
        self.domain.gameover = False
        self.domain.player_won = False
        self.domain.computer_won = False
        self.domain.count = 1
        self.domain.winner = None
        self.domain.board = [[' ' for i in range(6)] for j in range(6)]

    # check if the player has 5 X or O in a row, column or diagonal
    def check_winner(self, row, col):
        if self.check_row() or self.check_col() or self.check_diag() or self.check_diag2():
            self.domain.player_won = True
        if self.domain.count == 36:
            self.domain.computer_won = True

    # check if a row has 5 X or O in a row
    def check_row(self):
        for i in range(6):
            for j in range(2):
                if self.domain.board[i][j] == self.domain.board[i][j + 1] == self.domain.board[i][j + 2] == \
                        self.domain.board[i][j + 3] == self.domain.board[i][j + 4] != ' ':
                    return True
        return False

    # check if a column has 5 X or O in a row
    def check_col(self):
        for i in range(6):
            for j in range(2):
                if self.domain.board[j][i] == self.domain.board[j + 1][i] == self.domain.board[j + 2][i] == \
                        self.domain.board[j + 3][i] == self.domain.board[j + 4][i] != ' ':
                    return True
        return False

    # check if a diagonal has 5 X or O in a row
    def check_diag(self):
        for i in range(2):
            for j in range(2):
                if self.domain.board[i][j] == self.domain.board[i + 1][j + 1] == self.domain.board[i + 2][j + 2] == \
                        self.domain.board[i + 3][j + 3] == self.domain.board[i + 4][j + 4] != ' ':
                    return True
        return False

    # check if the second diagonal has 5 X or O in a row
    def check_diag2(self):
        for i in range(2):
            for j in range(2):
                if self.domain.board[i][j + 4] == self.domain.board[i + 1][j + 3] == self.domain.board[i + 2][j + 2] == \
                        self.domain.board[i + 3][j + 1] == self.domain.board[i + 4][j] != ' ':
                    return True
        return False
