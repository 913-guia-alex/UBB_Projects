from Service import *


# check if the input is of type int
def check_int(cond):
    try:
        int(cond)
        return True
    except ValueError:
        return False


class UI:
    def __init__(self):
        self.service = Service()
        self.service.StartGame()
        self.domain = self.service.domain

    def print_board(self):
        print('  0 1 2 3 4 5 6')
        for row in self.domain.board:
            print('|' + '|'.join(row) + '|')

    # define a function that takes the first empty row in a column and checks if the move is valid
    def get_next_open_row(self, column):
        for i in range(5, -1, -1):
            if self.domain.board[i][column] == ' ':
                return i
        if self.domain.board[0][column] != ' ':
            print('Invalid move! You can not make a move in a full column!')
            return -1

    # function that makes a move for the computer
    def make_computer_move(self):
        while True:
            col = random.randint(0, 6)
            print('Computer move: ' + str(col))
            self.service.check_computer_won()
            row = self.get_next_open_row(col)
            if self.domain.board[row][col] == ' ':
                self.domain.board[row][col] = 'O'
                self.domain.player_turn = True
                self.domain.computer_turn = False
                self.domain.count += 1
                self.service.check_computer_won()
                break

    # function that makes a move for the player
    def make_player_move(self):
        while True:
            col = input('Enter column: ')
            if check_int(col) == False:
                print('Invalid type!')
                continue
            col = int(col)
            if col < 0 or col > 6:
                print('Invalid column!')
                continue
            self.service.check_player_won()
            row = self.get_next_open_row(col)
            if self.domain.board[row][col] == ' ':
                self.domain.board[row][col] = 'X'
                self.domain.player_turn = False
                self.domain.computer_turn = True
                self.domain.count += 1
                self.service.check_player_won()
                break

    # make a function that plays the came player vs computer
    def play(self):
        while True:
            if self.domain.computer_winner:
                print('Computer won!')
                break
            if self.domain.player_winner:
                print('Player won!')
                break
            if self.domain.count == 41:
                print('Tie!')
                break
            self.print_board()
            if self.domain.player_turn:
                self.make_player_move()
            else:
                self.make_computer_move()

    def run(self):
        self.play()
