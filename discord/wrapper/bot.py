import asyncio
import json
import asyncio
import aiohttp
import json
from .gateway import Gateway
from .intents import Intents
from .http_client import HTTPClient
import random
import string
import functools
import inspect
import time
import traceback
from collections import deque
 

class InvokeError(Exception):
	def __init__(self, message):
		super.__init__(message)

class Bot:
	"""
	A class for discord bots.
	
	Attributes
    ----------	
	
	token : str
		The token for the bot.
	intents : int
		The priveliged intents.
	command_prefix : str
		The command prefix for the bot.	
	http : HTTPClient
	    The http client that sends requests to discord.
	"""
	def __init__(self, command_prefix : str = None, intents : int = 0, token : str = None):
                self.http = HTTPClient(str(token))
		self.token = token
		self.intents = intents
		self.command_prefix = command_prefix
		
	
	def close(self):
		"""
		:function:
			
		The function to close the websocket connection.
		"""
		
		Gateway().close()

		
	def run(self):
		"""
		:function:
			
		the function to run the bot.
		"""
		try:
			payload = Gateway().connect(str(self.token), self.intents)
			payload
		except Exception as e:
			raise InvokeError(e)															
