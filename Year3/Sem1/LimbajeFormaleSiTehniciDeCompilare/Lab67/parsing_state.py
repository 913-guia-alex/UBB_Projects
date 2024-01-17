from enum import Enum

class ParsingState(Enum):
    """
    Enumeration representing different parsing states.

    - NORMAL: The normal parsing state.
    - BACK: The backtracking parsing state.
    - FINAL: The final parsing state.
    - ERROR: The error parsing state.
    """

    NORMAL = "q"
    BACK = "b"
    FINAL = "f"
    ERROR = "e"

    def __str__(self):
        """
        Returns the character representation of the parsing state.
        """
        return self.value
