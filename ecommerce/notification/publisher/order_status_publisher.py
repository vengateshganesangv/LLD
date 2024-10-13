from publisher import Publisher

class OrderStatusPublisher(Publisher):
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_all(self, message):
        for subscriber in self.subscribers:
            subscriber.notify(message)