import re

from SymbolTable import SymbolTable
from ScannerException import ScannerException
from FA import FA


class Scanner:
    def __init__(self):
        self.program = ""
        self.tokens = set()
        self.reserved_words = set()
        self.symbol_table = SymbolTable(47)
        self.PIF = []
        self.index = 0
        self.current_line = 1
        self.fa_identifiers = FA("C:\\Users\\Alex\\PycharmProjects\\Lab2LFTC\\identifier.in")
        self.fa_int_constants = FA("C:\\Users\\Alex\\PycharmProjects\\Lab2LFTC\\int_constant.in")

    def set_program(self, program: str):
        self.program = program

    def read_tokens(self, token_file: str):
        with open(token_file) as file:
            self.tokens = {token.strip() for token in file.readlines()}

        reserved = {"for", "break", "elseif", "if", "else", "while", "do", "read", "write", "boolean", "string",
                    "integer", "vector"}
        self.reserved_words = self.tokens.intersection(reserved)
        self.tokens -= self.reserved_words

    def skip_spaces(self):
        while self.index < len(self.program) and self.program[self.index].isspace():
            if self.program[self.index] == '\n':
                self.current_line += 1
            self.index += 1

    def skip_comments(self):
        if self.program.startswith("#", self.index):
            while self.index < len(self.program) and self.program[self.index] != '\n':
                self.index += 1

    def treat_int_constant(self):
        int_constant = self.fa_int_constants.get_next_accepted(self.program[self.index:])
        if int_constant:
            self.index += len(int_constant)
            position = self.symbol_table.add_constant(int(int_constant))
            self.PIF.append(("const", position))
            return True
        return False

    def treat_string_constant(self):
        string_constant_pattern = r'"[^"]*"'  # will match any string that starts and ends
        # with double quotes and contains any character except a double quote
        # between the opening and closing quotes.
        string_constant_match = re.match(string_constant_pattern, self.program[self.index:])

        if string_constant_match:
            string_constant_value = string_constant_match.group()
            position = self.symbol_table.add_constant(string_constant_value)
            self.PIF.append(("const", position))
            self.index += string_constant_match.end()
            return True
        return False

    def treat_identifier(self):
        identifier = self.fa_identifiers.get_next_accepted(self.program[self.index:])
        if identifier:
            if not self.check_if_valid(identifier, self.program[self.index:]):
                return False
            self.index += len(identifier)
            position = self.symbol_table.add_identifier(identifier)
            self.PIF.append(("identifier", position))
            return True
        return False

    def check_if_valid(self, possible_identifier, program_substring):
        if possible_identifier in self.reserved_words or possible_identifier in self.tokens:
            return True

        if program_substring.startswith(possible_identifier + " (integer") or \
                program_substring.startswith(possible_identifier + " (boolean") or \
                program_substring.startswith(possible_identifier + " (string") or \
                program_substring.startswith(possible_identifier + " (vector"):
            return True

        if (possible_identifier[0].isalpha() or possible_identifier[0] == '_') and all(
                char.isalnum() or char == '_' for char in possible_identifier):
            return True

        return self.symbol_table.has_identifier(possible_identifier)

    def treat_from_token_list(self):
        for token in self.tokens:
            if self.program.startswith(token, self.index):
                self.index += len(token)
                self.PIF.append((token, (-1, -1)))
                return True
        return False

    def next_token(self):
        self.skip_spaces()
        self.skip_comments()
        if self.index == len(self.program):
            return
        if self.treat_string_constant():
            return
        if self.treat_int_constant():
            return
        if self.treat_identifier():
            return
        if self.treat_from_token_list():
            return
        raise ScannerException(f"Lexical error: invalid token at line {self.current_line}, index {self.index}")

    def scan(self, program_file_name, token_file_name):
        try:
            self.read_tokens(token_file_name)

            with open(program_file_name) as file:
                self.set_program(file.read())

            self.index = 0
            self.PIF = []
            self.symbol_table = SymbolTable(20)
            self.current_line = 1

            while self.index < len(self.program):
                self.next_token()

            with open("PIF.out", "a") as pif_file:
                pif_file.write(program_file_name + ":\n\n")
                for token, position in self.PIF:
                    pif_file.write(f"{token} -> ({position[0]}, {position[1]})\n")

            # Writing identifiers to ST1.out
            with open("ST1.out", "a") as st1_file:
                st1_file.write("Identifiers:\n")
                identifiers = str(self.symbol_table.identifiers_table)
                st1_file.write(identifiers)

            # Writing constants (integers and strings) to ST2.out
            with open("ST2.out", "a") as st2_file:
                st2_file.write("Constants:\n")
                constants = str(self.symbol_table.constants_table)
                st2_file.write(constants)

            print("Lexically correct")

        except (FileNotFoundError, ScannerException) as e:
            print(e)
