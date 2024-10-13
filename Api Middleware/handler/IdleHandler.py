from handler.RequestHandler import RequestHandler

class IdleHandler(RequestHandler):
    def handle(self, request):
        print("All done")
