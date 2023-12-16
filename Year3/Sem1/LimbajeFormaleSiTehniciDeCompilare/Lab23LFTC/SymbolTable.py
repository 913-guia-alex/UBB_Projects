from typing import Any, Tuple
from HashTable import HashTable


class SymbolTable:
    def __init__(self, size: int):
        self.size = size
        self.identifiers_table = HashTable(size)
        self.constants_table = HashTable(size)

    def add_identifier(self, key: Any) -> Tuple[int, int]:
        return self.identifiers_table.add(key)

    def has_identifier(self, key: Any) -> bool:
        return self.identifiers_table.contains(key)

    def get_position_identifier(self, key: Any) -> Tuple[int, int]:
        return self.identifiers_table.get_position(key)

    def add_constant(self, key: Any) -> Tuple[int, int]:
        return self.constants_table.add(key)

    def has_constant(self, key: Any) -> bool:
        return self.constants_table.contains(key)

    def get_position_constant(self, key: Any) -> Tuple[int, int]:
        return self.constants_table.get_position(key)

    def __str__(self):
        identifiers_structure = f"Identifiers: {self.identifiers_table}"
        constants_structure = f"Constants: {self.constants_table}"
        return f"Symbol Table Representation:\n{identifiers_structure}\n{constants_structure}"
