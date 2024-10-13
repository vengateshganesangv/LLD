from dataclasses import dataclass
from common.pair import Pair

@dataclass
class Move:
    source: Pair
    destination: Pair