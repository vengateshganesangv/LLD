from publisher.FootBallPublisher import FootBallPublisher
from subscriber.FootBallSubscriber import FootBallSubscriber
from abc import abstractmethod

class AbstractFootBallSubscriber(FootBallSubscriber):
    def __init__(self, subject: FootBallPublisher):
        self._subject = subject

    def get_subject(self):
        return self._subject

    @abstractmethod
    def update(self):
        pass
