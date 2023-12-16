class Grammar:
    EPSILON = "epsilon"

    def __init__(self):
        # Initialize the Grammar class with empty sets/lists and an empty dictionary for productions
        self.N = []  # Non-terminals
        self.E = []  # Terminals
        self.S = ""  # Starting symbol
        self.P = {}  # Productions

    def __processLine(self, line: str):
        # Helper function to process a line and extract what comes after the '='
        return line.strip().split(' ')[2:]

    def readFromFile(self, file_name: str):
        """
        Reads the grammar from a file and populates the Grammar class attributes.

        Parameters:
        - file_name (str): The name of the file containing the grammar.

        Returns:
        None
        """
        with open(file_name) as file:
            # Read and process Non-terminals, Terminals, and the Starting symbol
            N = self.__processLine(file.readline())
            E = self.__processLine(file.readline())
            S = self.__processLine(file.readline())[0]

            file.readline()  # Skip the line containing 'P ='

            # Get all productions
            P = {}
            for line in file:
                split = line.strip().split('->')
                source = split[0].strip()
                sequence = split[1].lstrip(' ')
                sequence_list = []
                for c in sequence.split(' '):
                    sequence_list.append(c)

                # Add the production to the dictionary
                if source in P.keys():
                    P[source].append(sequence_list)
                else:
                    P[source] = [sequence_list]

            # Set the attributes of the Grammar object
            self.N = N
            self.E = E
            self.S = S
            self.P = P

    def checkCFG(self):
        """
        Checks if the provided grammar is a valid Context-Free Grammar (CFG).

        Returns:
        - bool: True if the grammar is a valid CFG, False otherwise.
        """
        hasStartingSymbol = False
        for key in self.P.keys():
            if key == self.S:
                hasStartingSymbol = True
            if key not in self.N:
                return False  # Production source is not a non-terminal

        if not hasStartingSymbol:
            return False  # Starting symbol not found in productions

        for production in self.P.values():
            for rhs in production:
                for value in rhs:
                    if value not in self.N and value not in self.E and value != Grammar.EPSILON:
                        return False  # Production contains an invalid symbol

        return True  # The grammar is a valid CFG

    def __str__(self):
        # Return a string representation of the Grammar object
        result = "N = " + str(self.N) + "\n"
        result += "E = " + str(self.E) + "\n"
        result += "S = " + str(self.S) + "\n"
        result += "P = " + str(self.P) + "\n"
        return result
