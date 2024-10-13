from Logger.DebugLogger import DebugLogger
from Logger.InfoLogger import InfoLogger
from Logger.WarnLogger import WarnLogger
from Logger.ErrorLogger import ErrorLogger
from Logger.AnalyticsLogger import AnalyticsLogger
from Logger.FatalLogger import FatalLogger
from Logger.IdleLogger import IdleLogger
from publisher.LogPublisher import LogPublisher
from subscriber.ConsoleSubscriber import ConsoleSubscriber
from subscriber.FileSubscriber import FileSubscriber

class LoggerFactory:
    def __init__(self):
        self.debug_info_pub = LogPublisher()
        self.debug_info_pub.subscribe(ConsoleSubscriber())
        self.warn_and_above_pub = LogPublisher()
        self.warn_and_above_pub.subscribe(ConsoleSubscriber())
        self.warn_and_above_pub.subscribe(FileSubscriber("./log.txt"))

    def get_logger(self):
        return DebugLogger(
            InfoLogger(
                WarnLogger(
                    ErrorLogger(
                        AnalyticsLogger(
                            FatalLogger(
                                IdleLogger(),
                                self.warn_and_above_pub
                            ),
                            self.warn_and_above_pub
                        ),
                        self.warn_and_above_pub
                    ),
                    self.warn_and_above_pub
                ),
                self.debug_info_pub
            ),
            self.debug_info_pub
        )
