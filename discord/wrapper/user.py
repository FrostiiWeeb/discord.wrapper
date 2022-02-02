import aiohttp, asyncio, sys, datetime
from .http_client import HTTPClient


# https://discord.com/developers/docs/resources/user

# https://github.com/kyb3r/pycord/blob/dev/pycord/api/http.py

# https://cdn.discordapp.com/avatars/746807014658801704/ed8582aa1e1e0f9b873d06951d3a37fc.webp?size=1024


class User:

    def __init__(
        self, http : HTTPClient, data : dict
    ) -> None:
        self.username = ...
        for i in data:
            setattr(self, i, data[i])
        self.name = self.username
        self.DISCORD_EPOCH = 1420070400000
        self.created_at = self.snowflake_time(self.id)
        self.http = http

    async def send(self):
        ...

    def snowflake_time(self, id: int) -> datetime.datetime:
        timestamp = ((id >> 22) + self.DISCORD_EPOCH) / 1000
        return datetime.datetime.utcfromtimestamp(timestamp).replace(
            tzinfo=datetime.timezone.utc
        )

    def __repr__(self) -> str:
        fmt = f"id={self.id!r} name={self.name!r} discriminator={self.discriminator!r} bot={self.bot!r}"
        return "<User {}>".format(fmt)


class ClientUser(User):
    def __init__(self, http: HTTPClient, data: dict) -> None:
        super().__init__(http, data)
        self.bot = True