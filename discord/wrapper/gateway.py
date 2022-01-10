import json
import asyncio, functools
import aiohttp
import json
from string import Template
from io import StringIO
import ast
import uvloop

from aiohttp.hdrs import AUTHORIZATION


class InvokeError(Exception):
    def __init__(self, message):
        super.__init__(message)


class Gateway:
    def __init__(self, bot):
        self.bot = bot

    async def get_data(self):
        data = await self.ws.receive()
        return data.data

    def identify_json(self, token: str, intents: int):
        """
                The identify payload to authorize the bot.

        Attributes
        ----------

        token : str
                The token of the bot.
        intents : int
                The intents for the bot.
        """
        t = '{"op": 2,"d": {"token": "{0}","intents": {1}, "properties": {"$os": "linux","$browser": "discord.wrapper","$device": "discord.wrapper"}, "status": "dnd", "since": 91879201, "afk": false},"s": null,"t": null}'.format(
            str(token), intents
        )

        return t

    async def close(self):
        """
        The |async| function to close the connection.
        """
        await self.ws.close()

    async def connect_ws(self, _token: str, _intents: int):
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
            self.ws = await aiohttp.ClientSession().ws_connect(
                "wss://gateway.discord.gg/?v=6&encoding=json"
            )
            events = await self.get_data()
            stringio = StringIO(events)
            lines = stringio.read()
            array = lines.split()
            dict_list = []
            for data in lines:
                new_data_json = json.loads(data)
                new_data = json.dumps(new_data_json)
                dict_list.append(json.loads(new_data))
            for data in dict_list:
                if data["op"] == 10:
                    heartbeat = '{"op": 1,"d": 251}'
                    protocol = self.identify_json(_token, _intents)
                    protocol = json.loads(protocol)
                    hearbeat = json.loads(heartbeat)
                    await self.ws.send_json(heartbeat)
                    await self.ws.send_json(protocol)
                    await self.get_data()

        except Exception as e:
            print(e)

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
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        asyncio.ensure_future(self.connect_ws(token, intents), loop=loop)
        loop.run_forever()

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
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        uvloop.install()
        loop = uvloop.new_event_loop()
        asyncio.set_event_loop(loop)
        asyncio.ensure_future(self.connect_ws(token, intents), loop=loop)
        loop.run_forever()
