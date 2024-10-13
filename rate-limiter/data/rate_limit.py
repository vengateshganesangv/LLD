from dataclasses import dataclass

@dataclass
class RateLimit:
    is_allowed: bool
    retry_after: float = 0