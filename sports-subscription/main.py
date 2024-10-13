from publisher.ESPNCricketScoreBoardPublisher import ESPNCricketScoreBoardPublisher
from subscriber.PredictedCricketScoreSubscriber import PredictedCricketScoreSubscriber

ESPNChannel = ESPNCricketScoreBoardPublisher()
person_A = PredictedCricketScoreSubscriber(ESPNChannel)
person_B = PredictedCricketScoreSubscriber(ESPNChannel)
ESPNChannel.notify_all(10,0,0.5)
ESPNChannel.notify_all(20,0,1.5)
