import typing, sys
from .author import Author
from .guild import Guild
import asyncio


class GuildNone:
    def __init__(self) -> None:
        self.id = None


class ChannelNone:
    def __init__(self) -> None:
        self.id = None


class Message:
    def __init__(self, data: dict):
        self.tts = data["tts"]
        try:
            data["member"]
            self.author = Author(data)
        except KeyError:
            self.author = Author(data)
        else:
            self.author = Author(data, data["member"])
            self.content = data["content"]
            if not data["referenced_message"]:
                self.referenced_message = None
            else:
                self.referenced_message = self.__init__(data["referenced_message"])
            self.attachments = data["attachments"]
            self.guild = GuildNone()
            self.guild.id = data["guild_id"]
            self.channel = ChannelNone()
            self.channel.id = data["channel_id"]
