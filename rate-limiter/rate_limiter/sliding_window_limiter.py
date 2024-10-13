import time
from data.rate_limit import RateLimit
from data.request import Request
from interface.rate_limiter_interface import IRateLimiter
import heapq

class SlidingWindowLimiter(IRateLimiter):
    def __init__(self, requests_per_window: int, window_size: int):
        self.requests_per_window = requests_per_window
        self.window_size = window_size
        self.requests: dict[str, list[float]] = {}

    def is_allowed(self, request: Request) -> RateLimit:
        key = f"{request.user_id}:{request.resource}"
        now = time.time()

        if key not in self.requests:
            self.requests[key] = []

        while self.requests[key] and self.requests[key][0] <= now - self.window_size:
            heapq.heappop(self.requests[key])

        if len(self.requests[key]) < self.requests_per_window:
            heapq.heappush(self.requests[key], now)
            return RateLimit(is_allowed=True)
        else:
            oldest = self.requests[key][0]
            retry_after = oldest + self.window_size - now
            return RateLimit(is_allowed=False, retry_after=retry_after)