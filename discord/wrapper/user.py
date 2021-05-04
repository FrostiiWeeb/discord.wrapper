import aiohttp, asyncio, sys, datetime  
    

# https://discord.com/developers/docs/resources/user

# https://github.com/kyb3r/pycord/blob/dev/pycord/api/http.py

# https://cdn.discordapp.com/avatars/746807014658801704/ed8582aa1e1e0f9b873d06951d3a37fc.webp?size=1024

class User:
    
    def __init__(self, data = {"username": "null", "id": "444", "bot": True, "mfa_enabled": "null", "avatar": "null", "discriminator": "0000"}):
        self.name = data['username']
        self.id = int(data['id'])
        self.bot = data['bot']
        self.mfa = data['mfa_enabled']	
        self.avatar = data['avatar']
        self.discriminator = int(data['discriminator'])
        			         
        self.DISCORD_EPOCH = 1420070400000
        self.created_at = self.snowflake_time(self.id)
             

    def snowflake_time(self, id: int) -> datetime.datetime:
        timestamp = ((id >> 22) + self.DISCORD_EPOCH) / 1000
        return datetime.datetime.utcfromtimestamp(timestamp).replace(tzinfo=datetime.timezone.utc)         
                        
    def __repr__(self) -> str:
        fmt = f"id={self.id!r} name={self.name!r} discriminator={self.discriminator!r} bot={self.bot!r}"
        return "<User {}>".format(fmt)

class ClientUser:
    
    def __init__(self, data = {"username": "null", "id": "444", "bot": True, "mfa_enabled": "null", "avatar": "null", "discriminator": "0000"}):
        self.name = data['username']
        self.id = int(data['id'])
        self.bot = data['bot']
        self.mfa = data['mfa_enabled']	
        self.avatar = data['avatar']
        self.discriminator = int(data['discriminator'])
        			         
        self.DISCORD_EPOCH = 1420070400000
        self.created_at = self.snowflake_time(self.id)
             

    def snowflake_time(self, id: int) -> datetime.datetime:
        timestamp = ((id >> 22) + self.DISCORD_EPOCH) / 1000
        return datetime.datetime.utcfromtimestamp(timestamp).replace(tzinfo=datetime.timezone.utc)         
                        
    def __repr__(self) -> str:
        fmt = f"id={self.id!r} name={self.name!r} discriminator={self.discriminator!r} bot={self.bot!r}"
        return "<ClientUser {}>".format(fmt)
    
        