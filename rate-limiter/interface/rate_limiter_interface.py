from abc import ABC, abstractmethod
from data.rate_limit import RateLimit
from data.request import Request

class IRateLimiter(ABC):
    @abstractmethod
    def is_allowed(self, request: Request) -> RateLimit:
        pass