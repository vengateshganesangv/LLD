from data.LogLevel import LogLevel
from Logger.LoggerFactory import LoggerFactory

def main():
    logger_factory = LoggerFactory()
    logger = logger_factory.get_logger()
    logger.log(LogLevel.ERROR, "DB query failed")
    logger.log(LogLevel.DEBUG, "Received an empty response")

if __name__ == "__main__":
    main()
