from abc import ABC, abstractmethod
from data.LogLevel import LogLevel

class Logger(ABC):
    @abstractmethod
    def log(self, log_level: LogLevel, message: str):
        pass
