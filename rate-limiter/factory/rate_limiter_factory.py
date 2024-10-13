from interface.rate_limiter_interface import IRateLimiter
from rate_limiter.fixed_window_limiter import FixedWindowLimiter
from rate_limiter.leaking_bucket_limiter import LeakingBucketLimiter
from rate_limiter.sliding_window_limiter import SlidingWindowLimiter
from rate_limiter.token_bucket_limiter import TokenBucketLimiter


class RateLimiterFactory:
    @staticmethod
    def create_limiter(config: dict[str, any]) -> IRateLimiter:
        limiter_type = config['type']
        if limiter_type == 'token_bucket':
            return TokenBucketLimiter(config['capacity'], config['refill_rate'])
        elif limiter_type == 'leaking_bucket':
            return LeakingBucketLimiter(config['capacity'], config['leak_rate'])
        elif limiter_type == 'fixed_window':
            return FixedWindowLimiter(config['requests_per_window'], config['window_size'])
        elif limiter_type == 'sliding_window':
            return SlidingWindowLimiter(config['requests_per_window'], config['window_size'])
        else:
            raise ValueError(f"Invalid rate limiter type: {limiter_type}")