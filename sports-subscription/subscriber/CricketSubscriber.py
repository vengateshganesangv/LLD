from abc import ABC, abstractmethod

class CricketSubscriber(ABC):
    
    @abstractmethod
    def update(self):
        """Update the subscriber with data from the publisher."""
        pass
