import aiohttp, asyncio, json, sys

class HTTPClient:
	"""Represents an http client sending requests to discord."""
	
	def __init__(self, token : str):
		
						
		self.__session = aiohttp.ClientSession()	
		user_agent = 'DiscordBot (https://github.com/FrostiiWeeb/discord.wrapper {0}) Python/{1[0]}.{1[1]} aiohttp/{2}'
		self.user_agent = user_agent.format("0.2.1", sys.version_info, aiohttp.__version__)
		self.token = str(token)		
		self.headers = {
		"Authorization": "Bot {}".format(self.token),
		"User-Agent": self.user_agent,
		"Content-Type": "application/json"
		}
		
	async def fetch_channel(self, channel_id : int):
		"""
		Fetches a channel from discord.
		
		channel_id : int
			The channel id to fetch.
		"""
		try:
			BASE = f"https://discordapp.com/api/channels/{channel_id}"
			headers = self.headers
            
            

			
			async with aiohttp.ClientSessiom() as session:
				async with session.get(BASE, headers=headers) as resp:
					data = await resp.json()
					return json.dumps(data)
					await session.close()
		except Exception as e:
			print(e)
			
	async def send_message(self, channel_id=None, content=None, *, embed=None):
		"""
		Sends a message to discord.
		"""
		
		headers = self.headers
		
		payload = {
		"content": content,
		"embed": embed
		}
		
		async with aiohttp.ClientSession() as session:
			await session.post("https://discordapp.com/api/channels/{}/messages".format(channel_id), headers=headers, data = json.dumps(payload))
			await session.close()
					
		
	async def fetch_message(self, channel_id : int, message_id : int):
		"""
		Fetches a channel from discord.
		
		channel_id : int
			The channel id to fetch.
		message_id : int
			The message id to fetch.			
		"""
		try:			
			BASE = f"https://discordapp.com/api/channels/{channel_id}/messages/{message_id}"
			headers = self.headers
            
            

			
			async with session.get(BASE, headers=headers) as resp:
				data = await resp.json()
				return json.dumps(data)
		except Exception as e:
			print(e)