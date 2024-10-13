class Response:
    def __init__(self, body=None, status=None):
        self.body = body
        self.status = status

    def get_body(self):
        return self.body

    def set_body(self, value):
        self.body = value

    def get_status(self):
        return self.status

    def set_status(self, value):
        self.status = value

