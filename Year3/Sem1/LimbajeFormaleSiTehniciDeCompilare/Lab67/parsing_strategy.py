from parsing_state import ParsingState
import copy


class ParserStrategy:
    def __init__(self, production_rules):
        #Initializes the ParserStrategy with production rules.

        self.production_rules = production_rules

    def expand(self, configuration):
        #Expands the configuration by applying production rules.

        configuration.next = copy.deepcopy(configuration)
        next_config = configuration.next

        symbol = next_config.beta.pop()
        next_config.alpha.append(symbol)
        index_mapping_key = len(next_config.alpha) - 1

        if index_mapping_key not in next_config.index_mapping:
            next_config.index_mapping[index_mapping_key] = 1

        production_number = next_config.index_mapping[index_mapping_key]
        first_production_rule_of_symbol = self.get_lhs_of_ith_production_rule_of_symbol(symbol, production_number)

        next_config.beta.extend(reversed(first_production_rule_of_symbol))

    @staticmethod
    def advance(configuration):
        #Advances the parsing configuration.

        configuration.next = copy.deepcopy(configuration)
        configuration.next.i += 1
        configuration.next.alpha.append(configuration.next.beta.pop())

    @staticmethod
    def momentary_insuccess(configuration):
        #Marks the parsing configuration as momentarily unsuccessful.

        configuration.next = copy.deepcopy(configuration)
        configuration.next.s = ParsingState.BACK

    @staticmethod
    def back(configuration):
        #Moves back in the parsing configuration.

        configuration.next = copy.deepcopy(configuration)
        configuration.next.i -= 1
        configuration.next.beta.append(configuration.next.alpha.pop())

    def another_try(self, configuration):
        #Attempts another parsing iteration.

        configuration.next = copy.deepcopy(configuration)
        next_config = configuration.next

        A = next_config.alpha[-1]
        j = next_config.index_mapping[len(next_config.alpha) - 1]

        lhs_of_current_production_rule = self.get_lhs_of_ith_production_rule_of_symbol(A, j)

        try:
            lhs_of_next_production_rule = self.get_lhs_of_ith_production_rule_of_symbol(A, j + 1)

            next_config.s = ParsingState.NORMAL

            for _ in range(len(lhs_of_current_production_rule)):
                next_config.beta.pop()

            next_config.beta.extend(reversed(lhs_of_next_production_rule))
            next_config.index_mapping[len(next_config.alpha) - 1] = j + 1
        except IndexError:
            starting_symbol = list(self.production_rules.keys())[0][0]
            if next_config.i == 1 and A == starting_symbol:
                next_config.s = ParsingState.ERROR

                next_config.index_mapping.pop(len(next_config.alpha) - 1)
                next_config.alpha.pop()

                for _ in range(len(lhs_of_current_production_rule)):
                    next_config.beta.pop()
            else:
                next_config.index_mapping.pop(len(next_config.alpha) - 1)
                next_config.alpha.pop()

                for _ in range(len(lhs_of_current_production_rule)):
                    next_config.beta.pop()

                next_config.beta.append(A)

    @staticmethod
    def success(configuration):
        #Marks the parsing configuration as successful.

        configuration.next = copy.deepcopy(configuration)
        configuration.next.s = ParsingState.FINAL

    def get_lhs_of_ith_production_rule_of_symbol(self, symbol, i):
        """
        Retrieves the left-hand side of the i-th production rule for a given symbol.

        Returns:
        - list: The left-hand side of the production rule.
        """
        production_rules_of_symbol_with_spaces = self.production_rules[symbol][i-1][0]
        production_rules_of_symbol = []
        for prod in production_rules_of_symbol_with_spaces:
            if prod != " ":
                production_rules_of_symbol.append(prod)
        return list(production_rules_of_symbol)
