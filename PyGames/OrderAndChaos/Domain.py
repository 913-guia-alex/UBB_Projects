# Write the domain class for the game Order and Chaos strategy game . The game plays on 6x6 board and the 2 players
# are order(the computer) and chaos(human player) and they take turn to place X or O on the board The game ends when
# one of the player wins or the board is full The player wins if he has 5 X or O in a row, column or diagonal The
# computer wins the board is full and the player has not won Players can choose to place X or O on the board The
# computer will place X or O on the board
class ChaosAndOrder:
    def __init__(self):
        self.board = [[' ' for i in range(6)] for j in range(6)]
        self.count = 0
        self.check_winner = None
        self.gameover = False
        self.player_won = False
        self.computer_won = False
        self.player_turn = True
        self.computer_turn = False
        self.winner = None

    def get_board(self):
        return self.board

    def get_player(self):
        return self._player

    def get_computer(self):
        return self._computer

    def get_count(self):
        return self._count

    def get_winner(self):
        return self._winner

    def get_gameover(self):
        return self._gameover

    def get_player_won(self):
        return self._player_won

    def get_computer_won(self):
        return self._computer_won

    def get_tie(self):
        return self._tie

    def get_player_turn(self):
        return self._player_turn

    def get_computer_turn(self):
        return self._computer_turn

    def set_board(self, board):
        self._board = board

    def set_player(self, player):
        self._player = player

    def set_computer(self, computer):
        self._computer = computer

    def set_count(self, count):
        self._count = count

    def set_winner(self, winner):
        self._winner = winner

    def set_gameover(self, gameover):
        self._gameover = gameover

    def set_player_won(self, player_won):
        self._player_won = player_won

    def set_computer_won(self, computer_won):
        self._computer_won = computer_won

    def set_tie(self, tie):
        self._tie = tie

    def set_player_turn(self, player_turn):
        self._player_turn = player_turn

    def set_computer_turn(self, computer_turn):
        self._computer_turn = computer_turn
