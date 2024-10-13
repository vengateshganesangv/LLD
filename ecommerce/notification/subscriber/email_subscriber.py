from subscriber import Subscriber

class EmailSubscriber(Subscriber):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f"Sending email to {self.email}: {message}")