from handler.RequestHandler import RequestHandler

class ValidationHandler(RequestHandler):
    def __init__(self, next_handler: RequestHandler):
        self.next_handler = next_handler

    def handle(self, request):
        if not request.header or not request.header.strip():
            raise ValueError("empty header")
        if not request.body or not request.body.strip():
            raise ValueError("empty body")
        print("Validation Passed")
        self.next_handler.handle(request)
