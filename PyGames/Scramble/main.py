from Repository import *
from  Service import *
from UI import *


class Main:
    def __init__(self):
        self.__repository = Repository()
        self.__service = Service(self.__repository)
        self.__ui = UI(self.__service)

    def start(self):
        self.__ui.start()

if __name__ == "__main__":
    Main().start()