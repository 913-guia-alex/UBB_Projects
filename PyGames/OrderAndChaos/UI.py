from Service import *
import random


class UI:
    def __init__(self):
        self.service = Service()
        self.service.StartGame()
        self.domain = self.service.domain

    # function that prints the board with the X and O and the empty cells and the numbers of the rows and columns
    def print_board(self):
        print('  0 1 2 3 4 5')
        for i in range(6):
            print(i, end=' ')
            for j in range(6):
                print(self.domain.board[i][j], end=' ')
            print()

    # function that computes the player move and checks if the game is over and choose from X or O
    def player_move(self):
        while True:
            row = int(input('Enter row: '))
            col = int(input('Enter column: '))
            if row < 0 or row > 5 or col < 0 or col > 5:
                print('Invalid row or column!')
                continue
            sign = str(input('Enter X or O: '))
            if sign != 'X' and sign != 'O':
                print('Invalid sign!')
                continue
            self.service.check_winner(row, col)
            if self.domain.board[row][col] == ' ':
                self.domain.board[row][col] = sign
                self.domain.player_turn = False
                self.domain.computer_turn = True
                self.domain.count += 1
                break

    # function that computes the computer move and checks if the game is over
    def computer_move(self):
        while True:
            row = random.randint(0, 5)
            col = random.randint(0, 5)
            choose = ['X', 'O']
            self.service.check_winner(row, col)
            if self.domain.board[row][col] == ' ':
                self.domain.board[row][col] = random.choice(choose)
                self.domain.player_turn = True
                self.domain.computer_turn = False
                self.domain.count += 1
            break

    # function that plays the game and checks if the game is over , at every move from the player he can choose X or O
    def play(self):
        while True:
            if self.domain.player_won or self.domain.computer_won:
                if self.domain.player_won:
                    print('You won!')
                else:
                    print('Computer won!')
                break
            self.print_board()
            if self.domain.player_turn:
                self.player_move()
            else:
                self.computer_move()

    def run(self):
        self.play()
