from handler.RequestHandler import RequestHandler
from managers.UserManager import UserManager

class AuthorisationHandler(RequestHandler):
    def __init__(self, next_handler: RequestHandler, user_manager: UserManager):
        self.next_handler = next_handler
        self.user_manager = user_manager

    def handle(self, request):
        if not self.user_manager.is_subscribed(request.token):
            raise RuntimeError("Authorization failed")
        print("Authorisation passed")
        self.next_handler.handle(request)
