from abc import ABC, abstractmethod

class AbstractCache(ABC):
    def __init__(self, capacity: int, eviction_policy):
        self.capacity = capacity
        self.cache = {}
        self.eviction_policy = eviction_policy

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def put(self, key, value):
        pass
