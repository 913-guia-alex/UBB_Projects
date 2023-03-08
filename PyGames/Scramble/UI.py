class UI:
    def __init__(self, service):
        self._service = service

    def start(self):
        """Main function to start the game"""
        self._service.start_game()
        while not self._service.is_game_over():
            self.display_scrambled_sentence()
            command = input("Enter your command (swap <word1> <letter1> - <word2> <letter2>) or 'exit': ")
            if command == "exit":
                break
            try:
                self._service.process_command(command)
            except Exception as e:
                print(e)
        self.display_scrambled_sentence()
        if self._service.is_game_won():
            print("Congratulations! You won!")
        else:
            print("Sorry, you lost. Better luck next time!")

    def display_scrambled_sentence(self):
        """Display the current scrambled sentence"""
        scrambled_sentence = self._service.get_scrambled_sentence()
        print(scrambled_sentence)
        print("Score: ", self._service.get_score())
