# Import all the modules

import asyncio, sys
import json
import asyncio
import aiohttp
import json
from .gateway import Gateway
from .intents import Intents
from .http_client import HTTPClient
from .user import ClientUser
from .channel import *
from .guild import Guild
from .content import Content
import random
import string
import functools
import inspect
import time
import traceback
from collections import deque
import subprocess, functools
import logging, typing, inspect
from .events import *


class Bot:
    """
        A class for discord bots.

        Parameters
    ----------

        token : str
                The token for the bot.
        intents : int
                The privileged intents.

    """

    def __init__(self, token: str, *, intents: int = 0, self_bot: bool = False):
        self.http = HTTPClient(str(token), self_bot)
        self.intents = intents
        self.cache = {}
        self.token = token
        self.gateway = Gateway(self)
        self.commands = {}
        self.guilds = []
        self.unavailable_guilds = []
        self.events = []
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.http.__session = aiohttp.ClientSession()

    async def send_message(self, channel_id: int, message: str):
        return await self.http.send_message(channel_id=channel_id, content=message)

    async def get_guild_data(self):
        """
                :function:

        A function to get the bot\'s guild data.

        """
        call = await self.http.get("/users/@me/guilds")
        return call

    async def get_user_data(self):
        """
        :function:

        A function to get the bot\'s user data.

        """
        call = await self.http.get("/users/@me")
        return call

    async def fetch_channel(self, id: int):
        """
        :function:

        A function to fetch a channel.

        .. note::
            This is an API call, not from the bots cache.
        """
        if id in self.cache:
            return self.cache[str(id)]
        call = await self.http.get("/channels/{id}")
        return call

    async def init(self):
        """
        :function:

        This function initializes the bot to have its attributes.
        """
        user = await self.get_user_data()
        guilds = await self.get_guild_data()
        print(guilds)
        for guild in guilds:
            try:
                self.guilds.append(
                    Guild(
                        int(guild["id"]),
                        guild["name"],
                        guild["icon"],
                        guild["description"],
                        guild["splash"] or None,
                        guild["discovery_splash"] or None,
                        guild["features"],
                        guild["emojis"],
                        guild["banner"] or None,
                        guild["owner_id"],
                        self.user.id,
                        guild["region"] or None,
                        guild["afk_chnnale_id"] or None,
                        guild["afk_timeout"] or None,
                        guild["system_channel_id"] or None,
                        guild["widget_enabled"],
                        guild["widget_channel_id"] or None,
                        guild["verification_level"],
                        guild["roles"],
                        guild["default_message_notifications"],
                        guild["mfa_level"] or None,
                        guild["explicit_content_filter"],
                        guild["max_presences"],
                        guild["max_members"],
                        guild["vanity_url_code"],
                        guild["premium_tier"],
                        guild["premium_subscription_count"],
                        guild["system_channel_flags"],
                        guild["preferred_local"],
                        guild["rules_channel_id"] or "",
                        guild["public_updates_channel_id"] or None,
                    )
                )
            except KeyError:
                pass

    def event(self):
        def command_wrapper(func: typing.Callable) -> typing.Callable:
            self.add_listener(func)

        return command_wrapper

    def add_listener(self, function: typing.Callable):
        if function.__name__ == "on_message":
            self.events.append(MessageCreate(callback=function, type="message"))
        if function.__name__ == "on_ready":
            self.events.append(Ready(callback=function))

    async def close(self):
        """
        :function:

        The function to close the websocket connection.
        """

        await self.gateway.close()

    def run(self):
        """
        :function:

        A function to run the bot.

        .. warning::
            This is a blocking function, so if you try to run any code after this function, it won\'t run.
        """
        asyncio.get_event_loop().run_until_complete(
            asyncio.gather(self.gateway.connect(str(self.token), self.intents)),
        )
