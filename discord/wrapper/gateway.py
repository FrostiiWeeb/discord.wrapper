import json
import asyncio, functools
import aiohttp
import json
from string import Template
from io import StringIO
import ast

class InvokeError(Exception):
	def __init__(self, message):
		super.__init__(message)
	            
    
class Gateway:
	def __init__(self, bot):
		self.bot = bot 
	
	async def get_data(self):
		   data = await self.ws.receive()
		   return data.data					  
			
	def identify_json(self, token : str, intents : int):
		"""
		The identify payload to authorize the bot.
		
		Attributes
		----------
		
		token : str
			The token of the bot.
		intents : int
			The intents for the bot.
		"""
		
		t = Template('{"op": 2,"d": {"token": "$token","intents": $intents, "properties": {"$os": "linux","$browser": "discord.wrapper","$device": "discord.wrapper"}, "status": "dnd", "since": 91879201, "afk": false},"s": null,"t": null}')
		t = t.substitute(token=str(token), intents=intents, os="$os", browser="$browser", device="$device")

		return t
	
	
	async def close(self):
		"""
		The |async| function to close the connection.
		"""
				
		await self.ws.close()
		
	async def start(self, _token : str, _intents : int):
		"""
		Function to connect the bot to discord.
		
		Attributes
		----------
		
		_token : str
			The token of the bot.
		_intents : int
			The intents for the bot.
		"""		
		try:
			self.ws = await aiohttp.ClientSession().ws_connect("wss://gateway.discord.gg/?v=6&encoding=json") 
			my_data = await self.get_data()
			my_data_str = str(my_data)
			my_io = StringIO(my_data_str)
			my_lines = my_io.read()
			data_list = my_lines.split()	
			my_dict_with_list = []
			for my_list in data_list:
			
			    my_new_data = json.loads(my_list)
			    my_new_n_data = json.dumps(my_new_data)
			    my_dict_with_list.append(json.loads(my_new_n_data))
			for data in my_dict_with_list:			   
			    if data['op'] == 10:
			        
			        heartbeat = '{"op": 1,"d": 251}'
			        p = self.identify_json(_token, _intents)
			        p_l = json.loads(p)
			        p_j = json.dumps(p_l)
			        h = json.loads(heartbeat)
			        h_json = json.dumps(h)
			        await self.ws.send_str(h_json)		
			        await self.ws.send_str(p_j)
			        await self.get_data()           			  
			        		          		
		except Exception as e:
			print(e)
	
	def connect(self, token : str, intents : int):
		"""
		The actual function to connect the bot to discord.
		
		Attributes
		----------
		
		token : str
			The token of the bot.
		intents : int
			The intents for the bot.
		"""		
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)
		asyncio.ensure_future(self.start(token, intents), loop=loop)
		loop.run_forever()																					