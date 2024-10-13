from abstract_cache import AbstractCache


class LRUCache(AbstractCache):
    def __init__(self, capacity: int, eviction_policy):
        super().__init__(capacity, eviction_policy)

    def get(self, key):
        if key in self.cache:
            self.eviction_policy.update(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.eviction_policy.update(key)
        else:
            if len(self.cache) >= self.capacity:
                evicted_key = self.eviction_policy.evict()
                if evicted_key:
                    del self.cache[evicted_key]
            self.cache[key] = value
            self.eviction_policy.update(key)
