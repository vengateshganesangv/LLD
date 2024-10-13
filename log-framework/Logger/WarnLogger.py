from Logger.Logger import Logger
from Publisher.Publisher import Publisher
from data.LogLevel import LogLevel

class WarnLogger(Logger):

    def __init__(self, next_logger: Logger, log_publisher: Publisher):
        self.next_logger = next_logger
        self.log_publisher = log_publisher

    def log(self, log_level, message):
        if log_level.get_level() == LogLevel.WARN.get_level():
            self.log_publisher.notify(f"{LogLevel.WARN} {message}")
        self.next_logger.log(log_level, message)
