from abc import ABC, abstractmethod
from subscriber.FootBallSubscriber import FootBallSubscriber

class FootBallPublisher(ABC):
    
    @abstractmethod
    def subscribe(self, subscriber: FootBallSubscriber):
        """Subscribe a FootBallSubscriber to the publisher."""
        pass

    @abstractmethod
    def unsubscribe(self, subscriber: FootBallSubscriber):
        """Unsubscribe a FootBallSubscriber from the publisher."""
        pass

    @abstractmethod
    def notify_all(self, goals1: int, goals2: int, duration: float):
        """Notify all subscribers with the latest cricket scores."""
        pass

    @abstractmethod
    def get_goals1(self) -> int:
        """Get the number of Goals by Team 1."""
        pass

    @abstractmethod
    def get_goals2(self) -> int:
        """Get the number of Goals by Team 2."""
        pass

    @abstractmethod
    def get_duration(self) -> float:
        """Get the total duration elapsed"""
        pass
