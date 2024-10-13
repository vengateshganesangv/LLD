from publisher.FootBallPublisher import FootBallPublisher
from subscriber.FootBallSubscriber import FootBallSubscriber

class FootBallScorePublisher(FootBallPublisher):
    def __init__(self):
        self._goals1 = 0
        self._goals2 = 0
        self._duration = 0.0
        self._subscribers: list[FootBallSubscriber] = []

    def subscribe(self, subscriber: FootBallSubscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: FootBallSubscriber):
        self._subscribers.remove(subscriber)

    def notify_all(self, goals1: int, goals2: int, duration: float):
        self._goals1 = goals1
        self._goals2 = goals2
        self._duration = duration
        for subscriber in self._subscribers:
            subscriber.update()

    def get_goals1(self) -> int:
        return self._goals1

    def get_goals2(self) -> int:
        return self._goals2

    def get_duration(self) -> float:
        return self._duration
