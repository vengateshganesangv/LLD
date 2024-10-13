from abc import ABC, abstractmethod

class FootBallSubscriber(ABC):
    @abstractmethod
    def update(self):
        pass
