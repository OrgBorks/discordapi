import discord

__all__ = (
    "Message",
    "make_payload"
)

class Message():
    def __init__(self, m):
        self.id = m["id"]
        self.channel_id = m["channel_id"]
        self.channel = discord.get_channel(self.channel_id)
        self.guild_id = m.get("guild_id", None)
        # self.guild = discord.get_guild(self.guild_id)
        self.webhook_id = m.get("webhook_id", None)
        self.author = m.get("author", None)
        # TODO: make a member class
        self.member = m.get("member", None)
        self.content = m["content"]
        self.timestamp = m["timestamp"]
        self.time_edited = m["edited_timestamp"]
        self.tts = m["tts"]
        self.everyone = m["mention_everyone"]
        self.mentions = m["mentions"]
        self.role_mentions = m["mention_roles"]
        self.attachments = m["attachments"]
        self.embeds = m["embeds"]
        self.reactions = m.get("reactions", None)
        self.nonce = m.get("nonce", None)
        self.pinned = m["pinned"]
        self.type = m["type"]
        self.activity = m.get("activity", None)
        self.application = m.get("aplication", None)
        self.application_id = m.get("application_id", None)
        self.message_reference = m.get("message_reference", None)
        self.flags = m.get("flags", None)
        self.referenced_message = m.get("referenced_message", None)
        self.interaction = m.get("interaction", None)
        self.thread = m.get("thread", None)
        self.components = m.get("components", None)
        self.stickers = m.get("sticker_items", None)
    
def make_payload(content=None, tts=None, file=None, embeds=None, mentions=None, reference=None, components=None, stickers=None):
    if not file:
        payload = {}
        if content:
            payload["content"] = content
        if tts:
            payload["tts"] = tts
        if embeds:
            payload["embeds"] = embeds
        if mentions:
            payload["allowed_mentions"] = mentions
        if reference:
            payload["message_reference"] = reference
        if components:
            payload["components"] = components
        if stickers:
            payload["sticker_ids"] = stickers
    return payload