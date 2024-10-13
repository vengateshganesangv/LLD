from publisher.Publisher import Publisher
from subscriber.Subscriber import Subscriber
#In this Publisher Other than subscriber no more instance variable is needed
#In notify also passing message alone so no need to set in instance variable and passing self is not needed
class LogPublisher(Publisher):
    def __init__(self):
        self.subscribers: Subscriber  = []

    def subscribe(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, message: str):
        for subscriber in self.subscribers:
            subscriber.update(message)
