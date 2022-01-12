import json
import asyncio, functools
import aiohttp
import json
from string import Template
from io import StringIO
import ast
import uvloop, sys

from aiohttp.hdrs import AUTHORIZATION


INDENTIFY = """{
  "op": 2,
  "d": {
    "token": "$token",
    "intents": $intents,
    "properties": {
      "$os": "linux",
      "$browser": "$browser",
      "$device": "$device"
    }
  }
}"""

class InvokeError(Exception):
    def __init__(self, message):
        super.__init__(message)


class Gateway:
	def __init__(self, bot):
		self.bot = bot
		self.heartbeat = {"op": 1,"d": 251}
		
	async def get_data(self):
		data = await self.ws.receive_str()
		print(data)
		return data
		
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
			
		t = Template('{"op": 2,"d": {"token": "$token","intents": $intents, "properties": {"$os": "linux","$browser": "discord.wrapper","$device": "discord.wrapper"}, "status": "online", "since": 91879201, "afk": false},"s": null,"t": null}')

		t = t.substitute(token=token, intents=intents, os="$os", browser="$browser", device="$device")
		return t
		
	async def close(self):
		"""
        The |async| function to close the connection.
        """
		await self.ws.close()

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
				autoclose=False
            )
			heartbeat_event = await self.get_data()
			heartbeat_event = json.loads(heartbeat_event)
			if heartbeat_event["op"] == 10:
				heartbeat = self.heartbeat
				heartbeat = json.dumps(heartbeat)
				protocol = self.identify_json(token, intents)	
				protocol = json.dumps(protocol)
				await self.ws.send_str(heartbeat)
				print(await self.get_data())
				await self.ws.send_json(protocol)
				while True:
					await asyncio.sleep(5)
					print(await self.get_data())
					await asyncio.sleep(5)
		except Exception:
			import traceback
			traceback.print_exc()
			
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
			loop = asyncio.new_event_loop()
			asyncio.set_event_loop(loop)
			asyncio.ensure_future(self.connect_ws(token, intents), loop=loop)
			loop.run_forever()
		except KeyboardInterrupt:
			sys.exit(1)
			
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
			loop = asyncio.new_event_loop()
			asyncio.set_event_loop(loop)
			asyncio.ensure_future(self.connect_ws(token, intents), loop=loop)
			loop.run_forever()
		except KeyboardInterrupt:
			sys.exit(1)
