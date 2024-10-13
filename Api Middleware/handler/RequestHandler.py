from abc import ABC, abstractmethod
from data.Request import Request

class RequestHandler(ABC):
    @abstractmethod
    def handle(self, request: Request):
        pass
