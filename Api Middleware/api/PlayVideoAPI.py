from data.Request import Request
from data.Response import Response
from handler.RequestHandlerFactory import RequestHandlerFactory

class PlayVideoAPI:
    def play_video(self, request: Request) -> Response:
        RequestHandlerFactory.get_handler("playVideo").handle(request)
        return None
