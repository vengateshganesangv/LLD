from publisher.CricketPublisher import CricketPublisher
from subscriber.CricketSubscriber import CricketSubscriber
from abc import abstractmethod

class AbstractCricketSubscriber(CricketSubscriber):
    def __init__(self, subject: CricketPublisher):
        self._subject = subject
    
    def get_subject(self):
        return self._subject

    @abstractmethod
    def update(self):
        pass
