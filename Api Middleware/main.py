from data.Request import Request
from handler.RequestHandlerFactory import RequestHandlerFactory

RequestHandlerFactory.get_handler("playVideo").handle(
                Request("abc", "def", "ghi")
        )