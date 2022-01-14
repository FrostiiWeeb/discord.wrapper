import sys


class PrintException:
    def __init__(self, message: str = None):
        self.message = message

    def send_error(self) -> None:
        print(self.message, file=sys.stderr)


class BaseException(Exception):
    def __init__(self, message: str = None):
        super().__init__(message)


class LoginFailure(BaseException):
    def __init__(self, message: str = "Invalid Token Passed"):
        super().__init__(message=message)
