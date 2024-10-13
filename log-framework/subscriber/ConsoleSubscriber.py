from subscriber.Subscriber import Subscriber

class ConsoleSubscriber(Subscriber):
    def update(self, message: str):
        print(message)
