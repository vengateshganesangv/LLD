from enum import Enum

class LogLevel(Enum):
    DEBUG = 0
    INFO = 1
    WARN = 2
    ERROR = 3
    FATAL = 4
    #Like this way also we can access
    #level = LogLevel.INFO
    #print(level.get_level())  # Output: 1
    def get_level(self):
        return self.value