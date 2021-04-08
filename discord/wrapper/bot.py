import asyncio
<<<<<<< HEAD
=======
import websockets
>>>>>>> e13b87682e850c26e831292bb19976027a2c79c2
import json
import asyncio
import aiohttp
import json
from .gateway import Gateway
from .intents import Intents
<<<<<<< HEAD
from .http_client import HTTPClient
=======
>>>>>>> e13b87682e850c26e831292bb19976027a2c79c2
import random
import string
import functools
import inspect
import time
import traceback
from collections import deque
<<<<<<< HEAD
 
=======
import sys, asyncio
>>>>>>> e13b87682e850c26e831292bb19976027a2c79c2

class InvokeError(Exception):
	def __init__(self, message):
		super.__init__(message)

class Bot:
	"""
	A class for discord bots.
	
	Attributes
    ----------	
	
	http_token : str
		The token for the bot.
	intents : int
		The priveliged intents.
	command_prefix : str
		The command prefix for the bot.	
	"""
	def __init__(self, command_prefix : str = None, intents : int = 0, token : str = None):
<<<<<<< HEAD
		self.http = HTTPClient(self)
		self.token = token
		self.intents = intents
		self.command_prefix = command_prefix
		
	
	def close(self):
		"""
		:function:
			
		The function to close the websocket connection.
		"""
		
		Gateway().close()
=======
		self.http_token = token		
		self.intents = intents
		self.command_prefix = command_prefix
>>>>>>> e13b87682e850c26e831292bb19976027a2c79c2

		
	def run(self):
		"""
		:function:
			
		the function to run the bot.
		"""
		try:
<<<<<<< HEAD
			payload = Gateway().connect(str(self.token), self.intents)
		except Exception as e:
			raise InvokeError(e)																									
=======
			payload = Gateway().connect(str(self.http_token), self.intents)
			print(payload)
		except Exception as e:
			raise InvokeError(e)
		
	
	async def fetch_channel(self, channel_id : int):
		"""
		Fetches a channel from discord.
		
		channel_id : int
			The channel id to fetch.
		"""
		try:
			BASE = f"https://discordapp.com/api/channels/{channel_id}"
			headers = { "Authorization":"Bot {}".format(self.http_token),
            "User-Agent":"myBotThing (http://some.url, v0.1)",
            "Content-Type":"application/json", }
            
            

			
			async with aiohttp.ClientSession() as session:
				async with session.get(BASE, headers=headers) as resp:
					data = await resp.json()
					return json.dumps(data)
		except Exception as e:
			raise InvokeError(e)		
>>>>>>> e13b87682e850c26e831292bb19976027a2c79c2
