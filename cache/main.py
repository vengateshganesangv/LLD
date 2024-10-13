from factory.cache_factory import CacheFactory


def test_cache(cache, operations):
    print(f"\n{cache.__class__.__name__}:")
    for op, key, value in operations:
        if op == 'put':
            cache.put(key, value)
            print(f"Put: ({key}, {value})")
        elif op == 'get':
            result = cache.get(key)
            print(f"Get: {key} -> {result}")

def main():
    caches = {
        "LRU Cache": CacheFactory.create_cache({
            'type': 'lru',
            'capacity': 2
        }),
    }

    # Test operations
    operations = [
        ('put', 1, 1),
        ('put', 2, 2),
        ('get', 1, None),
        ('put', 3, 3),
        ('get', 2, None),
        ('put', 4, 4),
        ('get', 1, None),
        ('get', 3, None),
        ('get', 4, None),
    ]

    for name, cache in caches.items():
        test_cache(cache, operations)

if __name__ == "__main__":
    main()