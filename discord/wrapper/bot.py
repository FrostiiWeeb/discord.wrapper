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
from .channel import Channel
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
import logging
import motor.motor_asyncio, collections

class Document:
    def __init__(self, connection, document_name):
        self.db = connection[document_name]
        self.logger = logging.getLogger(__name__)


    async def update(self, dict):
        await self.update_by_id(dict)

    async def get_by_id(self, id):

        return await self.find_by_id(id)

    async def find(self, id):
        return await self.find_by_id(id)

    async def delete(self, id):
        await self.delete_by_id(id)

 
    async def find_by_id(self, id):
        return await self.db.find_one({"_id": id})

    async def delete_by_id(self, id):

        if not await self.find_by_id(id):
            return

        await self.db.delete_many({"_id": id})

    async def insert(self, dict):
        if not isinstance(dict, collections.abc.Mapping):
            raise TypeError("Expected Dictionary got %s" % dict.__class__.__name__)

        if not dict["_id"]:
            raise KeyError("_id not found in supplied dict.")

        await self.db.insert_one(dict)

    async def upsert(self, dict):
        if await self.__get_raw(dict["_id"]) != None:
            await self.update_by_id(dict)
        else:
            await self.db.insert_one(dict)

    async def update_by_id(self, dict):
        if not isinstance(dict, collections.abc.Mapping):
            raise TypeError("Expected Dictionary got %s" % dict.__class__.__name__)
        if not dict["_id"]:
            raise KeyError("_id not found in supplied dict.")

        if not await self.find_by_id(dict["_id"]):
            return

        id = dict["_id"]
        dict.pop("_id")
        await self.db.update_one({"_id": id}, {"$set": dict})

    async def unset(self, dict):
        if not isinstance(dict, collections.abc.Mapping):
            raise TypeError("Expected Dictionary got %s" % dict.__class__.__name__)
        if not dict["_id"]:
            raise KeyError("_id not found in supplied dict.")

        if not await self.find_by_id(dict["_id"]):
            return

        id = dict["_id"]
        dict.pop("_id")
        await self.db.update_one({"_id": id}, {"$unset": dict})

    async def increment(self, id, amount, field):
        if not await self.find_by_id(id):
            return

        await self.db.update_one({"_id": id}, {"$inc": {field: amount}})
                
    @property
    async def get_all(self):
        data = []
        async for document in self.db.find({}):
            data.append(document)
        return data
      
    async def __get_raw(self, id):
        return await self.db.find_one({"_id": id}) 

class Bot:
	"""
	A class for discord bots.
	
	Parameters
    ----------	
	
	token : str
		The token for the bot.
	intents : int
		The priveliged intents.
	public_key : str
	    The public key of the bot.
							
	"""
	def __init__(self, token : str, public_key : str, *, intents : int = 0):
		self.http = HTTPClient(str(token))
		self.intents = intents
		self.cache = {}
		self.token = token
		self.gateway = Gateway(self)	
		self.public_key = public_key
		self.commands = {}	
		self.mongo_client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://frost:myuselesspassword@mongodbdata-shard-00-00.eapic.mongodb.net:27017,mongodbdata-shard-00-01.eapic.mongodb.net:27017,mongodbdata-shard-00-02.eapic.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-ue5d97-shard-0&authSource=admin&retryWrites=true&w=majority")
		self.collection_parent = self.mongo_client.discord_wrapper
		self.collection_parent = self.mongo_client['discord_wrapper']
		db = self.collection_parent.commands
		self.db = Document(self.collection_parent, "commands")
		
	async def _db_insert(self, name : str, callback, public_key : str):
	    await self.db.upsert({"_id": name, "key": public_key, "callback": callback})
	    
	def db_insert(self, name : str, callback, public_key : str):
	  return asyncio.get_event_loop().run_until_complete(self._db_insert(name, callback, public_key))
	  
	async def _create_slash(self, json):
			"""
			The actual function to create a slash command.
			"""
			return await self.http.post(f"/applications/{self.user.id}/commands", json=json)
			
	def create_slash(self, name : str, description : str = "A command", callback=Content().add_content('hi').to_dict()):
	    """
	    A function to create a slash command.
	    
	    Parameters
	    ----------

	    name : str
	        The name of the slash cmd.
	    description : str
	        The description of the slash cmd.
	    callback
	        The callback of the slash command when its called.
	    """	 	    	    	 	    	    	 	    	    	 	    	    
	    self.db_insert(name, callback, self.public_key)
	    data = {"name": name,"description": description,"options": []}
	    self.commands[name] = {"description": description}
	    asyncio.get_event_loop().run_until_complete(self._create_slash(data))
	    return f"Created command {name}"    

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
				
	async def fetch_channel(self, id : int):
		"""
		:function:
		    
        A function to fetch a channel.

        .. note::
            This is an API call, not from the bots cache.	 				    		 				    
		"""
		if id in self.cache:
		    return self.cache[str(id)]
		call = await self.http.get("/users/@me")
		return call		        
		  
               	           
	def init(self):
		"""
		:function:
		
		This function initializes the bot to have its attributes.		 
		"""	
		user = asyncio.get_event_loop().run_until_complete(self.get_user_data())
		guilds = asyncio.get_event_loop().run_until_complete(self.get_guild_data())
		self.user = ClientUser(user)
		self.guilds = []
		for g in guilds:
		    self.guilds.append(Guild(g))
	
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
		self.gateway.connect(str(self.token), self.intents)
		return f"Connected"																																																												