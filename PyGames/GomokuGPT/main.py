from UI import *


class Main:
    def __init__(self):
        self.repository = HangmanRepository()
        self.service = HangmanService(self.repository)
        self.ui = HangmanUI(self.service)

    def run(self):
        self.ui.start()


if __name__ == '__main__':
    Main().run()