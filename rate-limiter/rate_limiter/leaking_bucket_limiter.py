import time
from data.rate_limit import RateLimit
from data.request import Request
from interface.rate_limiter_interface import IRateLimiter
import heapq

class LeakingBucketLimiter(IRateLimiter):
    def __init__(self, capacity: int, leak_rate: float):
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.buckets: dict[str, list[float]] = {}

    def is_allowed(self, request: Request) -> RateLimit:
        key = f"{request.user_id}:{request.resource}"
        now = time.time()
        
        if key not in self.buckets:
            self.buckets[key] = []

        while self.buckets[key] and self.buckets[key][0] <= now - (1 / self.leak_rate):
            heapq.heappop(self.buckets[key])

        if len(self.buckets[key]) < self.capacity:
            heapq.heappush(self.buckets[key], now)
            return RateLimit(is_allowed=True)
        else:
            next_available = self.buckets[key][0] + (1 / self.leak_rate)
            return RateLimit(is_allowed=False, retry_after=next_available - now)