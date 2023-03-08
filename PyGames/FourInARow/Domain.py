#create a domain class for the game connect four:
class ConnectFour:
    def __init__(self):
        self.board = [[' ' for i in range(7)] for j in range(6)]
        self.player = 'X'
        self.computer = 'O'
        self.player_winner = False
        self.computer_winner = False
        self.move_count = 0
        self.count = 0
        self.player_turn = True
        self.computer_turn = False
        self.tie = False

    def get_board(self):
        return self.board

    def get_player(self):
        return self.player

    def get_computer(self):
        return self.computer

    def get_player_winner(self):
        return self.player_winner

    def get_computer_winner(self):
        return self.computer_winner

    def get_move_count(self):
        return self.move_count

    def get_game_over(self):
        return self.game_over

    def get_winner(self):
        return self.winner

    def get_turn(self):
        return self.turn

    def set_board(self, board):
        self.board = board

    def set_player(self, player):
        self.player = player

    def set_computer(self, computer):
        self.computer = computer

    def set_player_winner(self, player_winner):
        self.player_winner = player_winner

    def set_computer_winner(self, computer_winner):
        self.computer_winner = computer_winner

    def set_move_count(self, move_count):
        self.move_count = move_count

    def set_game_over(self, game_over):
        self.game_over = game_over

    def set_winner(self, winner):
        self.winner = winner

    def set_turn(self, turn):
        self.turn = turn




