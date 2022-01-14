import typing, inspect


class MessageCreate(object):
    """
    The class for the `on_message` events.
    """

    def __init__(self, callback: typing.Callable, type: str) -> None:
        super().__init__()
        self.callback = callback
        self.type = type
        if not inspect.iscoroutinefunction(callback):
            raise RuntimeError("Callback not coroutine.")


class Ready(object):
    """
    The class for the `on_ready` events.
    """

    def __init__(self, callback: typing.Callable, type: str = "ready") -> None:
        super().__init__()
        self.callback = callback
        self.type = type
        if not inspect.iscoroutinefunction(callback):
            raise RuntimeError("Callback not coroutine.")
