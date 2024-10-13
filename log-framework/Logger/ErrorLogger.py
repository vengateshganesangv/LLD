from Logger.Logger import Logger
from publisher.Publisher import Publisher
from data.LogLevel import LogLevel

class ErrorLogger(Logger):

    def __init__(self, next_logger: Logger, log_publisher: Publisher):
        self.next_logger = next_logger
        self.log_publisher = log_publisher

    def log(self, log_level, message):
        if log_level.get_level() == LogLevel.ERROR.get_level():
            self.log_publisher.notify(f"{LogLevel.ERROR} {message}")
        self.next_logger.log(log_level, message)
