from collections import OrderedDict
from parsing_state import ParsingState


class ParsingConfiguration:
    def __init__(self, s=ParsingState.NORMAL, i=1, alpha=None, index_mapping=None, beta=None):
        #Initializes a parsing configuration.

        self.s = s
        self.i = i
        self.alpha = alpha or []  # List representing the alpha part of the configuration
        self.index_mapping = index_mapping or OrderedDict()  # Mapping of alpha indices to production rule numbers
        self.beta = beta or []  # List representing the beta part of the configuration
        self.next = None  # Reference to the next parsing configuration

    def __str__(self):
        #Returns a string representation of the parsing configuration.

        alpha_string = ""
        index = 0
        for symbol in self.alpha:
            alpha_string += symbol
            if index in self.index_mapping:
                alpha_string += "[" + str(self.index_mapping[index]) + "]"
            if index < len(self.alpha) - 1:
                alpha_string += " "
            index += 1

        beta_string = " ".join(self.beta)
        result_string = "({}, {}, {}, {})".format(str(self.s), str(self.i), alpha_string, beta_string)
        return result_string

    def alpha_to_list_of_productions_string(self):
        #Converts the alpha part of the configuration to a list of tuples representing symbols and their production rule numbers.

        alpha_list = []
        index = 0
        for symbol in self.alpha:
            if index in self.index_mapping.keys():
                local_rule_number = self.index_mapping[index]
                alpha_list.append((symbol, local_rule_number))
            index += 1
        return alpha_list
