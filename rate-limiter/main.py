import time
from data.request import Request
from factory.rate_limiter_factory import RateLimiterFactory


if __name__ == "__main__":
    limiters = {
        "Token Bucket": RateLimiterFactory.create_limiter({
            'type': 'token_bucket',
            'capacity': 3,
            'refill_rate': 0.01666666666666666666666666666667  # 0.01 tokens per second
        }),
        "Leaking Bucket": RateLimiterFactory.create_limiter({
            'type': 'leaking_bucket',
            'capacity': 5,
            'leak_rate': 0.5  # 0.5 requests per second
        }),
        "Fixed Window": RateLimiterFactory.create_limiter({
            'type': 'fixed_window',
            'requests_per_window': 3,
            'window_size': 10  # 10 seconds
        }),
        "Sliding Window": RateLimiterFactory.create_limiter({
            'type': 'sliding_window',
            'requests_per_window': 3,
            'window_size': 10  # 10 seconds
        })
    }

    request = Request(user_id="user123", resource="/api/resource")

    for name, limiter in limiters.items():
        print(f"\n{name} Limiter:")
        for i in range(7):
            result = limiter.is_allowed(request)
            print(f"Request {i+1}: Allowed: {result.is_allowed}, Retry After: {result.retry_after:.2f}s")
            time.sleep(1)