class MissingKeysError(Exception):
    status_code = 400

    def __init__(self, required_fields: list[str] = None, received: list[str] = None) -> None:
        self.requireds = required_fields
        self.received = received

    def message(self):
        return {
            "Required fields": self.requireds,
            "Received": self.received
        }