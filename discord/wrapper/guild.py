import aiohttp, asyncio, sys, datetime  
    

# https://discord.com/developers/docs/resources/user

# https://github.com/kyb3r/pycord/blob/dev/pycord/api/http.py

# https://cdn.discordapp.com/avatars/746807014658801704/ed8582aa1e1e0f9b873d06951d3a37fc.webp?size=1024

class Guild:
    
    def __init__(self, data = {"name": "null", "id": "444", "features": ["null"], "owner_id": "888", "roles": [{"id": "2909267986263572999","name": "@everyone","permissions": "49794752","position": "100","color": "0",
      "hoist": False,
      "managed": False,
      "mentionable": False}], "approximate_member_count": 0}):
        self.name = data['name']
        self.id = int(data['id'])
        self.features = {}
        if not data['features'] == []:
            for f in data['features']:
                self.features[f] = True			         
        self.DISCORD_EPOCH = 1420070400000
        self.created_at = self.snowflake_time(self.id)
             

    def snowflake_time(self, id: int) -> datetime.datetime:
        timestamp = ((id >> 22) + self.DISCORD_EPOCH) / 1000
        return datetime.datetime.utcfromtimestamp(timestamp).replace(tzinfo=datetime.timezone.utc)         
                        
    def __repr__(self) -> str:
        fmt = f" id={self.id!r} name={self.name!r}"
        return "<Guild{}>".format(fmt)