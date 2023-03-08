from Domain import Board
from Service import Service
from UI import Console
from Validation import Validation

validation = Validation()
board = Board()
service = Service(board)
start = Console(service, board, validation)

start.start()