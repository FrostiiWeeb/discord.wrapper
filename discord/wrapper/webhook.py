from email import header
import aiohttp, asyncio, sys
from .embed import Embed

class Webhook():
	def __init__(self, url : str, username : str = None):
		self.url = url
		self.username = username
	
	async def set_session(self):
		user_agent = "DiscordBot (https://github.com/FrostiiWeeb/discord.wrapper {0}) Python/{1[0]}.{1[1]} aiohttp/{2}"
		self.user_agent = user_agent.format(
            "x.x.x", sys.version_info, aiohttp.__version__
        )
		self.headers = {
			"User-Agent": self.user_agent
		}
		self.__session = aiohttp.ClientSession()

	async def send(self, content : str = None, embed : Embed = None):
		await self.set_session()
		payload = {
			"content": content,
		}
		if embed:
			payload["embeds"] = [embed.to_dict()]
		if self.username:
			payload["username"] = self.username
		async with self.__session.post(self.url, json=payload) as resp:
			await self.__session.close()
			return resp.status