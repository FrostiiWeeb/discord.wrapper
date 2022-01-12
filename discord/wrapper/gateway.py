import json
import asyncio, functools
import aiohttp
import json
from string import Template
from io import StringIO
import ast
import uvloop, sys
from .exceptions import *
from aiohttp.hdrs import AUTHORIZATION
from .user import ClientUser

class InvokeError(Exception):
    def __init__(self, message):
        super.__init__(message)


class Gateway:
	def __init__(self, bot):
		self.bot = bot
		self.heartbeat = {"op": 1,"d": 251}
		self.errors = {"4002": None}
		
	async def get_data(self):
		data = await self.ws.receive()
		if isinstance(data.data, int):
			data = data.data
			if data == 4004:
				raise LoginFailure()
			else:
				data = data
		return data.data
		
	def identify_json(self, token: str, intents: int = None):
		"""
        The identify payload to authorize the bot.

        Attributes
        ----------

        token : str
                The token of the bot.
        intents : int
                The intents for the bot.
        """
		if not intents:
			intents = 513
		IDENTIFY = {"op": 2,"d": {"token": self.bot.http.token,"properties": {"$os": sys.platform,"$browser": "$browser","$device": "$device"}, "intents": intents}}
		return json.dumps(IDENTIFY)
		
	async def close(self):
		"""
        The |async| function to close the connection.
        """
		await self.ws.close()

	async def on_ready(self, data):
		user = data["user"]
		session_id = data["session_id"]
		self.session_id = session_id
		self.bot.user = ClientUser(int(user["id"]) or None,user["username"],user["discriminator"],user["avatar"] or None,user["verified"] or None,user["email"] or None,user["flags"],None,None,None,user["public_flags"] or None,)
		for guild in data["guilds"]:
			from .guild import UnavailableGuild
			self.bot.unavailable_guilds.append(UnavailableGuild(True, guild["id"]))

	async def connect_ws(self, token : str, intents : int):
		"""
		Websocket to connect to discord.

        Attributes
        ----------

        _token : str
                The token of the bot.
        _intents : int
                The intents for the bot.
        """
		try:
			self.__session = aiohttp.ClientSession()
			self.ws = await self.__session.ws_connect(
                "wss://gateway.discord.gg/?v=8&encoding=json",
				autoclose=False,
				headers={'User-Agent': self.bot.http.user_agent}
            )
			heartbeat_event = await self.get_data()
			heartbeat_event = json.loads(heartbeat_event)
			if heartbeat_event["op"] == 10:
				heartbeat = self.heartbeat
				heartbeat = json.dumps(heartbeat)
				protocol = self.identify_json(token, intents)	
				await self.ws.send_str(heartbeat)
				await self.ws.send_str(protocol)
				while True:
					data = json.loads(await self.get_data())
					if data["t"] == "READY":
						print(data)
						await self.on_ready(data["d"])
					if data["op"] == 0:
						print(data)
					
		except Exception:
			import traceback
			traceback.print_exc()
			await self.ws.close()
			await self.__session.close()
			try:
				sys.exit(1)
			except SystemExit:
				import os
				os._exit(1)
			
	def connect(self, token: str, intents: int):
		"""
        The actual `blocking` function to connect the bot to discord.

        Attributes
        ----------

        token : str
                The token of the bot.
        intents : int
                The intents for the bot.
        """
		try:
			loop = self.bot.loop
			asyncio.ensure_future(self.connect_ws(token, intents), loop=self.bot.loop)
			loop.run_forever()
		except Exception:
			loop.stop()
			loop.close()
			
	async def start(self, token: str, intents: int):
		"""
        The actual function to connect the bot to discord.

        Attributes
        ----------

        token : str
                The token of the bot.
        intents : int
                The intents for the bot.
        """
		try:
			loop = self.bot.loop
			asyncio.ensure_future(self.connect_ws(token, intents), loop=loop)
			loop.run_forever()
		except KeyboardInterrupt:
			sys.exit(1)
