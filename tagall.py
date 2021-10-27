# updated - t.me/adianish
import logging
import requests
import asyncio
from .. import loader, utils

logger = logging.getLogger(__name__)

def register(cb):
    cb(TagAllMod())

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

class TagAllMod(loader.Module):

    strings = {"name":"TagAll"}

    def __init__(self):
        self.config = loader.ModuleConfig("DEFAULT_MENTION_MESSAGE", 'KYS Token so... Ahh..', "Default message of mentions")
        self.name = self.strings["name"]

    async def client_ready(self, client, db):
        self.client = client

    async def tagallcmd(self, message):
        arg = utils.get_args_raw(message)

        logger.error(message)
        notifies = []
        async for user in self.client.iter_participants(message.to_id):
            notifies.append("<a href=\"tg://user?id="+ str(user.id) +"\">\u206c\u206f</a>")
        chunkss = list(chunks(notifies, 5))
        logger.error(chunkss)
        await message.delete()
        try:
            loop = asyncio.get_event_loop()
        except Exception as e:
            loop = asyncio.get_running_loop()
        chunkss = [i for i in chunkss]
        chunkss = chunks(chunkss, 10)
        for i in chunkss:
            loop.create_task(self.test(message, i, arg))

    async def test(self, message, chunks, arg):
        while True:
            for chunk in chunks:
                await self.client.send_message(message.to_id, (self.config["DEFAULT_MENTION_MESSAGE"] if not arg else arg) + '\u206c\u206f'.join(chunk))

