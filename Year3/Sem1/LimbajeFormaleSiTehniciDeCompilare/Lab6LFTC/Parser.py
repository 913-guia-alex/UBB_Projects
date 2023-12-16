from Grammar import Grammar


class RecursiveDescentParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.input_string = ""
        self.index = 0

    def expand(self, non_terminal):
        """
        Expands a non-terminal based on the grammar rules.

        Parameters:
        - non_terminal (str): The non-terminal to expand.

        Returns:
        - bool: True if the expansion is successful, False otherwise.
        """
        if non_terminal in self.grammar.P:
            production = self.grammar.P[non_terminal]
            if not isinstance(production, list):
                production = [production]

            for rhs in production:
                if self.try_production(rhs):
                    return True
            return False
        return False

    def try_production(self, production):
        """
        Tries to match the current input against a production.

        Parameters:
        - production (list): The production to match.

        Returns:
        - bool: True if the production is successfully matched, False otherwise.
        """
        original_index = self.index
        for symbol in production:
            if symbol in self.grammar.N:
                if not self.expand(symbol):
                    self.index = original_index
                    return False
            elif symbol in self.grammar.E:
                if self.index < len(self.input_string) and symbol == self.input_string[self.index]:
                    self.advance()
                else:
                    self.index = original_index
                    return False
            elif symbol == Grammar.EPSILON:
                continue  # Epsilon production, no need to match anything
            else:
                return False
        return True

    def advance(self):
        """Advances the parser's index to the next input symbol."""
        self.index += 1

    def momentary_insuccess(self):
        """Handles momentary insuccess by resetting the parser's index."""
        self.index = 0

    def back(self):
        """Backtracks the parser by decrementing the index."""
        self.index -= 1

    def another_try(self):
        """
        Performs another try by resetting the index and attempting to parse again.

        Returns:
        - bool: True if another try is successful, False otherwise.
        """
        self.momentary_insuccess()
        return self.parse()

    def success(self):
        """Checks if the parser successfully parsed the entire input."""
        return self.index == len(self.input_string)

    def parse(self):
        """
        Main parsing function. Parses the input string using the provided grammar.

        Returns:
        - bool: True if the parsing is successful, False otherwise.
        """
        start_symbol = self.grammar.S
        if start_symbol not in self.grammar.P:
            return False  # Invalid grammar, starting symbol has no production rules

        return self.expand(start_symbol)

    def parse_input(self, input_string):
        """
        Parses the input string using the Recursive Descent Parser.

        Parameters:
        - input_string (str): The input string to parse.

        Returns:
        - bool: True if parsing is successful, False otherwise.
        """
        self.input_string = input_string
        return self.parse()
