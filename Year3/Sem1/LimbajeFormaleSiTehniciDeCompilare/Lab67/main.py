from grammar import Grammar
from parser_algorithm import ParserAlgorithm
import os


def main():
    grammar_file_path = "g2.txt"
    output_file_path = os.path.splitext(os.path.basename(grammar_file_path))[0] + ".out"
    word_g3 = ["a", "c", "d", "b", "c", "d"]
    word_g2 = ["a", "c", "b", "c"]

    grammar = Grammar.from_file(grammar_file_path)
    parser_algorithm = ParserAlgorithm(grammar, word_g2)
    parser_algorithm.execute(output_file_path)


if __name__ == "__main__":
    main()