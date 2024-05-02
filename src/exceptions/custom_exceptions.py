class NotFoundError(Exception):
    def __init__(self, message="Not Found Error"):
        self.message = message
        super().__init__(self.message)