from abc import ABC, abstractmethod
#Subscriber Need To Implement These Three Thing Mandatory
class Publisher(ABC):
    @abstractmethod
    def subscribe(self, subscriber):
        pass

    @abstractmethod
    def unsubscribe(self, subscriber):
        pass

    @abstractmethod
    def notify(self, message):
        pass
