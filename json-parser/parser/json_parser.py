from abc import ABC, abstractmethod

class JsonParser(ABC):
    @abstractmethod
    def parse(self, json_text):
        pass

    @abstractmethod
    def to_string(self, json):
        pass