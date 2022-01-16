import json

class ActivityType():
	@classmethod
	@property
	def playing(cls):
		return 0

class Activity(object):
	def __init__(self, name : str, type : ActivityType) -> None:
		super().__init__()
		self.name = name
		self.type = type