import aiohttp, asyncio, sys, datetime


# https://discord.com/developers/docs/resources/user

# https://github.com/kyb3r/pycord/blob/dev/pycord/api/http.py

# https://cdn.discordapp.com/avatars/746807014658801704/ed8582aa1e1e0f9b873d06951d3a37fc.webp?size=1024

from typing import List, Any


class Guild:
    id: str
    name: str
    icon: str
    description: str
    splash: None
    discovery_splash: None
    features: List[str]
    emojis: List[Any]
    banner: str
    owner_id: str
    application_id: None
    region: None
    afk_channel_id: None
    afk_timeout: int
    system_channel_id: None
    widget_enabled: bool
    widget_channel_id: None
    verification_level: int
    roles: List[Any]
    default_message_notifications: int
    mfa_level: int
    explicit_content_filter: int
    max_presences: int
    max_members: int
    vanity_url_code: str
    premium_tier: int
    premium_subscription_count: int
    system_channel_flags: int
    preferred_locale: str
    rules_channel_id: str
    public_updates_channel_id: str

    def __init__(
        self,
        id: str,
        name: str,
        icon: str,
        description: str,
        splash: None,
        discovery_splash: None,
        features: List[str],
        emojis: List[Any],
        banner: str,
        owner_id: str,
        application_id: None,
        region: None,
        afk_channel_id: None,
        afk_timeout: int,
        system_channel_id: None,
        widget_enabled: bool,
        widget_channel_id: None,
        verification_level: int,
        roles: List[Any],
        default_message_notifications: int,
        mfa_level: int,
        explicit_content_filter: int,
        max_presences: int,
        max_members: int,
        vanity_url_code: str,
        premium_tier: int,
        premium_subscription_count: int,
        system_channel_flags: int,
        preferred_locale: str,
        rules_channel_id: str,
        public_updates_channel_id: str,
    ) -> None:
        self.id = id
        self.name = name
        self.icon = icon
        self.description = description
        self.splash = splash
        self.discovery_splash = discovery_splash
        self.features = features
        self.emojis = emojis
        self.banner = banner
        self.owner_id = owner_id
        self.application_id = application_id
        self.region = region
        self.afk_channel_id = afk_channel_id
        self.afk_timeout = afk_timeout
        self.system_channel_id = system_channel_id
        self.widget_enabled = widget_enabled
        self.widget_channel_id = widget_channel_id
        self.verification_level = verification_level
        self.roles = roles
        self.default_message_notifications = default_message_notifications
        self.mfa_level = mfa_level
        self.explicit_content_filter = explicit_content_filter
        self.max_presences = max_presences
        self.max_members = max_members
        self.vanity_url_code = vanity_url_code
        self.premium_tier = premium_tier
        self.premium_subscription_count = premium_subscription_count
        self.system_channel_flags = system_channel_flags
        self.preferred_locale = preferred_locale
        self.rules_channel_id = rules_channel_id
        self.public_updates_channel_id = public_updates_channel_id

    def __repr__(self) -> str:
        fmt = f" id={self.id!r} name={self.name!r}"
        return "<Guild{}>".format(fmt)


class UnavailableGuild:
    unavailable: bool
    id: str

    def __init__(self, unavailable: bool, id: str) -> None:
        self.unavailable = unavailable
        self.id = int(id)
