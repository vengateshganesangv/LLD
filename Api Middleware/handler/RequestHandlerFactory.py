from handler.ValidationHandler import ValidationHandler
from handler.AuthenticationHandler import AuthenticationHandler
from handler.AuthorisationHandler import AuthorisationHandler
from handler.IdleHandler import IdleHandler
from managers.UserManager import UserManager
from managers.TokenManager import TokenManager
from handler.RequestHandler import RequestHandler

class RequestHandlerFactory:
    @staticmethod
    def get_handler(api_name) -> RequestHandler:
        return ValidationHandler(
            AuthenticationHandler(
                AuthorisationHandler(
                    IdleHandler(),
                    UserManager()
                ),
                TokenManager()
            )
        )
