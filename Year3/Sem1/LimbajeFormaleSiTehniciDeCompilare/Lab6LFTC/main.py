from Grammar import Grammar
from Parser import RecursiveDescentParser


def main():
    grammar = Grammar()
    grammar.readFromFile("g1.in")

    rd_parser = RecursiveDescentParser(grammar)

    input_string = "abdbbbc"
    #input_string = "sjhdf"
    #input_string = "id"


    # Initial parsing attempt
    print(f"Initial parsing for input string '{input_string}': {rd_parser.parse_input(input_string)}")

    # Demonstrate the functions
    print("\nExpanding non-terminal:")
    rd_parser.expand("S")
    print()

    print("Advancing:")
    rd_parser.advance()
    print()

    print("Momentary Insuccess:")
    rd_parser.momentary_insuccess()
    print(f"Index after momentary insuccess: {rd_parser.index}\n")

    print("Backtracking:")
    rd_parser.back()
    print(f"Index after backtracking: {rd_parser.index}\n")

    print("Another Try:")
    print(f"Another try result: {rd_parser.another_try()}\n")

    print("Success Check:")
    print(f"Is parsing successful? {rd_parser.success()}\n")


if __name__ == "__main__":
    main()
