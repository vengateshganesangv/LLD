from subscriber.Subscriber import Subscriber

class FileSubscriber(Subscriber):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_writer = open(file_path, "a")

    def update(self, message: str):
        try:
            self.file_writer.write(message + "\n")
            self.file_writer.flush()
        except Exception as e:
            raise RuntimeError(str(e))

    def __del__(self):
        if self.file_writer:
            self.file_writer.close()
