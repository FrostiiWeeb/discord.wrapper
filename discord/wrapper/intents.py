import asyncio
import aiohttp

class Intents:
	
	"""
	Discord priveliged intents.

    """
	
	def all(self):
		return 28671
		
	def members(self):
		return 255
		
	def presences(self):
		return 32512