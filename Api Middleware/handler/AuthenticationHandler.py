from handler.RequestHandler import RequestHandler
from data.Request import Request
from managers.TokenManager import TokenManager

class AuthenticationHandler(RequestHandler):
    def __init__(self, next_handler : RequestHandler, token_manager : TokenManager):
        self.next_handler = next_handler
        self.token_manager = token_manager

    def handle(self, request):
        email = self.token_manager.get_email_from_token(request.token)
        if not self.is_valid_email(email):
            raise RuntimeError("Authentication failed")
        print("Authentication passed")
        self.next_handler.handle(request)

    def is_valid_email(self, email):
        return True
