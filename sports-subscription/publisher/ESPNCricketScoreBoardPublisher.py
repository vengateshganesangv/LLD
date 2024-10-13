from subscriber.CricketSubscriber import CricketSubscriber
from publisher.CricketPublisher import CricketPublisher

class ESPNCricketScoreBoardPublisher(CricketPublisher):
    def __init__(self):
        self._runs = 0
        self._wickets = 0
        self._overs = 0.0
        self._subscribers: list[CricketSubscriber] = []

    def subscribe(self, subscriber: CricketSubscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber: CricketSubscriber):
        self._subscribers.remove(subscriber)

    def notify_all(self, runs: int, wickets: int, overs: float):
        self._runs = runs
        self._wickets = wickets
        self._overs = overs
        for subscriber in self._subscribers:
            subscriber.update()

    def get_runs(self) -> int:
        return self._runs

    def get_wickets(self) -> int:
        return self._wickets

    def get_overs(self) -> float:
        return self._overs

    def get_subscribers(self) -> list[CricketSubscriber]:
        return self._subscribers
