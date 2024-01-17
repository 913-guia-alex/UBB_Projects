import copy
from queue import Queue
from node import Node
from parsing_strategy import ParserStrategy
from parsing_configuration import ParsingConfiguration
from parsing_state import ParsingState


class ParserAlgorithm:
    def __init__(self, grammar, sequence):
        """
        Initializes the ParserAlgorithm.

        Parameters:
        - grammar: The grammar for parsing.
        - sequence: The input sequence to parse.
        """
        self.grammar = grammar
        self.initial_configuration = ParsingConfiguration(beta=[grammar.get_start_symbol()])
        self.strategy = ParserStrategy(grammar.production_rules.copy())
        self.sequence = sequence

    def execute(self, output_file_path):
        #Executes the parsing algorithm and writes the output to a file.

        config = self.execute_algorithm()

        if config.s == ParsingState.FINAL:
            output = self.get_table_from_config(config)
        else:
            output = "ERROR"

        print(output)
        with open(output_file_path, 'w') as file:
            file.write(output)

    def execute_algorithm(self):
        #Executes the parsing algorithm.

        config = copy.deepcopy(self.initial_configuration)
        step = 1

        while config.s != ParsingState.FINAL and config.s != ParsingState.ERROR:
            print(f"{step}: {config} ", end="")
            if config.s == ParsingState.NORMAL:
                if config.i == len(self.sequence) + 1 and not config.beta:
                    # SUCCESS
                    print("SUCCESS")
                    self.strategy.success(config)
                    config = config.next
                else:
                    if config.beta and self.grammar.is_non_terminal_symbol(config.beta[-1]):
                        # EXPAND
                        print("EXPAND")
                        self.strategy.expand(config)
                        config = config.next
                    elif config.i - 1 < len(self.sequence) and config.beta and \
                            config.beta[-1] == self.sequence[config.i - 1]:
                        # ADVANCE
                        print("ADVANCE")
                        self.strategy.advance(config)
                        config = config.next
                    else:
                        # MOMENTARY INSUCCESS
                        print("MOMENTARY INSUCCESS")
                        self.strategy.momentary_insuccess(config)
                        config = config.next
            elif config.s == ParsingState.BACK:
                if self.grammar.is_terminal_symbol(config.alpha[-1]):
                    # BACK
                    print("BACK")
                    self.strategy.back(config)
                    config = config.next
                else:
                    # ANOTHER TRY
                    print("ANOTHER TRY")
                    self.strategy.another_try(config)
                    config = config.next

            step += 1

        print(config)
        return config

    def get_table_from_config(self, config):
        """
        Converts the final parsing configuration to a table representation.

        Parameters:
        - config: The final parsing configuration.

        Returns:
        - str: String representation of the parsing table.
        """
        sb = [f"Sequence: {self.sequence}\n"]

        for row in self.config_to_table(config):
            sb.append("{:<15} {:<15} {:<15} {:<15}\n".format(row[0], row[1], row[2], row[3]))

        return ''.join(sb)

    def config_to_table(self, config):
        """
        Converts the final parsing configuration to a table representation.

        Parameters:
        - config: The final parsing configuration.

        Returns:
        - list: List representing the parsing table.
        """
        return self.tree_to_table(self.alpha_to_tree(self.get_alpha_from_config(config)))

    def get_alpha_from_config(self, config):
        #Extracts the alpha part from the final parsing configuration.


        alpha = []
        for entry in reversed(config.alpha_to_list_of_productions_string()):
            symbol, number = entry
            if self.grammar.is_non_terminal(symbol):
                production_rule_rhs = self.grammar.get_lhs_of_ith_production_rule_of_symbol(symbol, number)
                alpha.append((symbol, production_rule_rhs))
        return alpha

    def alpha_to_tree(self, alpha):
        #Converts the alpha part to a tree structure.


        lhs = alpha[-1][0]

        tree = []
        root = Node(lhs)
        tree.append(root)
        queue = Queue()
        queue.put(root)

        while not queue.empty():
            current_node = queue.get()
            production_rule_rhs = alpha.pop()[1]

            for i in range(len(production_rule_rhs)):
                rhs_element = production_rule_rhs[i]

                child = Node(rhs_element, current_node)
                if i != 0:
                    child.left = tree[-1]
                tree.append(child)
                if self.grammar.is_non_terminal_symbol(rhs_element):
                    queue.put(child)

        return tree

    @staticmethod
    def tree_to_table(tree):
        #Converts the tree structure to a table representation.


        table = [["index", "info(alpha)", "parent(index_m)", "right sibling(beta)"]]

        for i, node in enumerate(tree):
            row = [str(i + 1), node.symbol, str(tree.index(node.parent) + 1) if node.parent else "-",
                   str(tree.index(node.left) + 1) if node.left else "-"]
            table.append(row)

        return table

