from abc import ABC, abstractmethod
from subscriber.CricketSubscriber import CricketSubscriber

class CricketPublisher(ABC):
    
    @abstractmethod
    def subscribe(self, subscriber: CricketSubscriber):
        """Subscribe a CricketSubscriber to the publisher."""
        pass

    @abstractmethod
    def unsubscribe(self, subscriber: CricketSubscriber):
        """Unsubscribe a CricketSubscriber from the publisher."""
        pass

    @abstractmethod
    def notify_all(self, runs: int, wickets: int, overs: float):
        """Notify all subscribers with the latest cricket scores."""
        pass

    @abstractmethod
    def get_runs(self) -> int:
        """Get the number of runs."""
        pass

    @abstractmethod
    def get_wickets(self) -> int:
        """Get the number of wickets."""
        pass

    @abstractmethod
    def get_overs(self) -> float:
        """Get the number of overs."""
        pass
