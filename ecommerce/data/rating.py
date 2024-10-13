from enum import Enum

class Rating(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5

    def get_val(self) -> int:
        return self.value