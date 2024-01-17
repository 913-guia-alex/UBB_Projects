import unittest
import copy
from collections import OrderedDict
from parsing_strategy import ParserStrategy
from parsing_configuration import ParsingConfiguration
from parsing_state import ParsingState

class TestParserStrategy(unittest.TestCase):
    def setUp(self):
        production_rules = {"S": [("a S b S", 1), ("a S", 2), ("c", 3)]}
        self.config= ParsingConfiguration(beta=["S"])
        self.strategy = ParserStrategy(production_rules.copy())

    def test_expand(self):
        self.strategy.expand(self.config)
        self.assertEqual(["S"], self.config.next.alpha)
        self.assertEqual(["S", "b", "S", "a"], self.config.next.beta)

    def test_advance(self):
        self.strategy.advance(self.config)
        self.assertEqual(2, self.config.next.i)
        self.assertEqual(["S"], self.config.next.alpha)
        self.assertEqual([], self.config.next.beta)

    def test_momentary_insuccess(self):
        self.strategy.momentary_insuccess(self.config)
        self.assertEqual(ParsingState.BACK, self.config.next.s)

    def test_back(self):
        self.strategy.advance(self.config)
        self.assertEqual(2, self.config.next.i)
        self.assertEqual(["S"], self.config.next.alpha)
        self.assertEqual([], self.config.next.beta)
        self.config = self.config.next
        self.strategy.back(self.config)
        self.assertEqual(1, self.config.next.i)
        self.assertEqual([], self.config.next.alpha)
        self.assertEqual(["S"], self.config.next.beta)

    def test_another_try(self):
        self.config.s = ParsingState.BACK
        self.config.i = 3
        self.config.alpha = ["S", "a", "S", "a", "S"]
        self.config.index_mapping = OrderedDict([(0, 1), (2, 1), (4, 1)])
        self.config.beta = ["S", "b", "S", "b", "S", "b", "S", "a"]
        self.strategy.another_try(self.config)
        self.assertEqual(["S", "a", "S", "a", "S"], self.config.next.alpha)
        self.assertEqual(["S", "b", "S", "b", "S", "a"], self.config.next.beta)

    def test_success(self):
        self.strategy.success(self.config)
        self.assertEqual(ParsingState.FINAL, self.config.next.s)

if __name__ == "__main__":
    unittest.main()