class Request:
    def __init__(self, header, body, token):
        self.header = header
        self.body = body
        self.token = token

    def get_header(self):
        return self.header

    def set_header(self, value):
        self.header = value

    def get_body(self):
        return self.body

    def set_body(self, value):
        self.body = value

    def get_token(self):
        return self.token

    def set_token(self, value):
        self.token = value

