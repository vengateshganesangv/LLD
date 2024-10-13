
import time
from data.rate_limit import RateLimit
from data.request import Request
from interface.rate_limiter_interface import IRateLimiter


class TokenBucketLimiter(IRateLimiter):
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens: dict[str, float] = {}
        self.last_refill_time: dict[str, float] = {}

    def is_allowed(self, request: Request) -> RateLimit:
        key = f"{request.user_id}:{request.resource}"
        now = time.time()
        
        if key not in self.tokens:
            self.tokens[key] = self.capacity
            self.last_refill_time[key] = now

        time_passed = now - self.last_refill_time[key]
        new_tokens = time_passed * self.refill_rate
        self.tokens[key] = min(self.capacity, self.tokens[key] + new_tokens)
        self.last_refill_time[key] = now

        if self.tokens[key] >= 1:
            self.tokens[key] -= 1
            return RateLimit(is_allowed=True)
        else:
            wait_time = (1 - self.tokens[key]) / self.refill_rate
            return RateLimit(is_allowed=False, retry_after=wait_time)