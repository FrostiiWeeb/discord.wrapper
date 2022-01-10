import asyncio
import aiohttp


class Intents:

    """
    Discord privileged intents.

    """

    @classmethod
    def all(cls):
        return 28671

    @classmethod
    def members(cls):
        return 255

    @classmethod
    def presences(cls):
        return 32512
