import aiohttp, asyncio, sys, datetime


# https://discord.com/developers/docs/resources/user

# https://github.com/kyb3r/pycord/blob/dev/pycord/api/http.py

# https://cdn.discordapp.com/avatars/746807014658801704/ed8582aa1e1e0f9b873d06951d3a37fc.webp?size=1024


class User:
    id: str
    username: str
    discriminator: int
    avatar: str
    verified: bool
    email: str
    flags: int
    banner: str
    accent_color: int
    premium_type: int
    public_flags: int

    def __init__(
        self,
        id: str,
        username: str,
        discriminator: int,
        avatar: str,
        verified: bool,
        email: str,
        flags: int,
        banner: str,
        accent_color: int,
        premium_type: int,
        public_flags: int,
    ) -> None:
        self.id = id
        self.name = username
        self.discriminator = discriminator
        self.tag = discriminator
        self.avatar = avatar
        self.verified = verified
        self.email = email
        self.flags = flags
        self.banner = banner
        self.accent_color = accent_color
        self.premium_type = premium_type
        self.public_flags = public_flags
        self.DISCORD_EPOCH = 1420070400000
        self.created_at = self.snowflake_time(self.id)

    def snowflake_time(self, id: int) -> datetime.datetime:
        timestamp = ((id >> 22) + self.DISCORD_EPOCH) / 1000
        return datetime.datetime.utcfromtimestamp(timestamp).replace(
            tzinfo=datetime.timezone.utc
        )

    def __repr__(self) -> str:
        fmt = f"id={self.id!r} name={self.name!r} discriminator={self.discriminator!r} bot={self.bot!r}"
        return "<User {}>".format(fmt)


class ClientUser:
    id: str
    username: str
    discriminator: int
    avatar: str
    verified: bool
    email: str
    flags: int
    banner: str
    accent_color: int
    premium_type: int
    public_flags: int

    def __init__(
        self,
        id: str,
        username: str,
        discriminator: int,
        avatar: str,
        verified: bool,
        email: str,
        flags: int,
        banner: str,
        accent_color: int,
        premium_type: int,
        public_flags: int,
    ) -> None:
        self.id = id
        self.username = username
        self.tag = discriminator
        self.discriminator = discriminator
        self.avatar = avatar
        self.verified = verified
        self.email = email
        self.flags = flags
        self.banner = banner
        self.name = username
        self.accent_color = accent_color
        self.premium_type = premium_type
        self.public_flags = public_flags
        self.DISCORD_EPOCH = 1420070400000
        self.bot = True
        self.created_at = self.snowflake_time(self.id)

    def snowflake_time(self, id: int) -> datetime.datetime:
        timestamp = ((id >> 22) + self.DISCORD_EPOCH) / 1000
        return datetime.datetime.utcfromtimestamp(timestamp).replace(
            tzinfo=datetime.timezone.utc
        )

    def __repr__(self) -> str:
        fmt = f"id={self.id!r} name={self.name!r} discriminator={self.discriminator!r} bot={self.bot!r}"
        return "<ClientUser {}>".format(fmt)
