class IllegalStateError(Exception):
    """Exception raised for errors in the ATM's state.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Illegal action for current ATM state"):
        self.message = f"{message}"
        super().__init__(self.message)