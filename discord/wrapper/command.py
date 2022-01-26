import typing, sys

class SlashCommand(object):
	def __init__(self, name : str, callback : typing.Callable, type : int = 2) -> None:
		self.name = name
		self.callback = callback
		self.type = type