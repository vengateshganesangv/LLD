from Logger.Logger import Logger
from publisher.Publisher import Publisher
from data.LogLevel import LogLevel

class InfoLogger(Logger):
    def __init__(self, next_logger: Logger, log_publisher: Publisher):
        self.next_logger = next_logger
        self.log_publisher = log_publisher

    def log(self, log_level: LogLevel, message: str):
        if log_level == LogLevel.INFO:
            self.log_publisher.notify(f"{LogLevel.INFO} {message}")
        self.next_logger.log(log_level, message)