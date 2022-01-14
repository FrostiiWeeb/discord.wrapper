import typing, sys
from .channel import *


class Author:
    def __init__(self, data: dict, data_member: dict = None) -> None:
        if not data_member:
            author = data["author"]
            self.embeds = []
            if data["embeds"] == []:
                self.embeds = None
            else:
                for embed in data["embeds"]:
                    self.embeds.append(embed)
            self.channel = TextChannel(
                data["channel_id"],
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
            )
            self.name = author["username"]
            self.id = int(author["id"])
            self.discriminator = author["discriminator"]
            self.avatar = author["avatar"]
        else:
            author = data["author"]
            self.joined_at = data_member["joined_at"]
            self.roles = data_member["roles"]
            self.hoisted_role = data_member["hoisted_role"]
            self.embeds = []
            if data["embeds"] == []:
                self.embeds = None
            else:
                for embed in data["embeds"]:
                    self.embeds.append(embed)
            self.channel = TextChannel(
                data["channel_id"],
                data["guild_id"],
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
            )
            self.name = author["username"]
            self.id = int(author["id"])
            self.discriminator = author["discriminator"]
            self.avatar = author["avatar"]
