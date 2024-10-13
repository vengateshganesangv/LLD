from collections import deque
import time
from data.rate_limit import RateLimit
from data.request import Request
from interface.rate_limiter_interface import IRateLimiter

class FixedWindowLimiter(IRateLimiter):
    def __init__(self, requests_per_window: int, window_size: int):
        self.requests_per_window = requests_per_window
        self.window_size = window_size
        self.windows: dict[str, deque] = {}

    def is_allowed(self, request: Request) -> RateLimit:
        key = f"{request.user_id}:{request.resource}"
        now = time.time()
        current_window = now // self.window_size

        if key not in self.windows:
            self.windows[key] = deque()

        while self.windows[key] and self.windows[key][0][0] < current_window:
            self.windows[key].popleft()

        if not self.windows[key] or self.windows[key][-1][0] < current_window:
            self.windows[key].append((current_window, 1))
            return RateLimit(is_allowed=True)
        elif self.windows[key][-1][1] < self.requests_per_window:
            self.windows[key][-1] = (current_window, self.windows[key][-1][1] + 1)
            return RateLimit(is_allowed=True)
        else:
            next_window = (current_window + 1) * self.window_size
            return RateLimit(is_allowed=False, retry_after=next_window - now)