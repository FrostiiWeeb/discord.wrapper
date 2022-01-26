import aiohttp, asyncio, sys

class BearerBot():
	def __init__(self, token : str) -> None:
		self.token = token

	async def set_session(self):
		self.__session = aiohttp.ClientSession(headers={"Authorization": "Bearer {}".format(self.token)})

	async def set_user(self):
		...