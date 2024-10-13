
from subscriber.AbstractCricketSubscriber import AbstractCricketSubscriber
from publisher.CricketPublisher import CricketPublisher

class PredictedCricketScoreSubscriber(AbstractCricketSubscriber):
    def __init__(self, publisher: CricketPublisher):
        super().__init__(publisher)
        self._runs = 0
        self._wickets = 0
        self._overs = 0.0
        publisher.subscribe(self)

    def update(self):
        self._runs = self.get_subject().get_runs()
        self._wickets = self.get_subject().get_wickets()
        self._overs = self.get_subject().get_overs()
        # additional logic
        print(f"In PredictedScoreSubscriber: {self._runs} runs, {self._wickets} wickets, {self._overs} overs.")

    def get_runs(self) -> int:
        return self._runs

    def get_wickets(self) -> int:
        return self._wickets

    def get_overs(self) -> float:
        return self._overs

    def get_publishers(self) -> list[CricketPublisher]:
        return self._publishers