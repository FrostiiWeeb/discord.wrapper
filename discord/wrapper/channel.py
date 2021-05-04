import aiohttp, asyncio, sys, datetime   
   
# https://discord.com/developers/docs/resources/user

# https://github.com/kyb3r/pycord/blob/dev/pycord/api/http.py

# https://cdn.discordapp.com/avatars/746807014658801704/ed8582aa1e1e0f9b873d06951d3a37fc.webp?size=1024

class Channel:
    
    def __init__(self, data = {"id": "444", "name": "null", "nsfw": False, "topic": "null", "last_message_id": "444"}):            
        self.id = int(data["id"])
        self.name = str(data["name"])
        self.is_nsfw : bool = data["nsfw"]
        self.topic = str(data["topic"])     
        self.last_message_id = int(data["last_message_id"])
        self.DISCORD_EPOCH = 1420070400000
      
    
    def snowflake_time(id: int) -> datetime.datetime:
        timestamp = ((id >> 22) + self.DISCORD_EPOCH) / 1000
        return datetime.datetime.utcfromtimestamp(timestamp).replace(tzinfo=datetime.timezone.utc)          
                        
    def __repr__(self) -> str:
        fmt = f"id={self.id!r} name={self.name!r} is_nsfw={self.is_nsfw!r} topic={self.topic!r} last_message_id={self.last_message_id!r}"
        return "<Channel {}>".format(fmt)
    
        