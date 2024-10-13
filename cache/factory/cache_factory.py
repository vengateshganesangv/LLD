
from eviction_policies.lru_policy import LRUPolicy
from lru_cache import LRUCache


class CacheFactory:
    @staticmethod
    def create_cache(config):
        cache_type = config['type']
        capacity = config['capacity']

        if cache_type == 'lru':
            eviction_policy = LRUPolicy()
            return LRUCache(capacity, eviction_policy)
        else:
            raise ValueError(f"Unsupported cache type: {cache_type}")