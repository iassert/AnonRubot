import typing

from telethon      import hints
from telethon.sync import TelegramClient
from telethon.tl.types      import Message
from telethon.events.common import EventBuilder

from .tr  import tr
from .log import Log


class Client_:
    __log: Log = Log(tr.clientLog)

    def __init__(self, client: TelegramClient) -> None:
        self.__client: TelegramClient = client

    def on(self, event: EventBuilder):
        try:
            return self.__client.on(event)
        except Exception as ex:
            self.__log.error(ex, "Ошибка при создании обработчика")

            def decorator(f):
                return f

            return decorator

    async def send_message(self, entity: hints.EntityLike, text: str) -> Message | None:
        try:
            return await self.__client.send_message(entity, text)
        except Exception as ex:
            self.__log.error(ex, "Ошибка при отправке сообщения")
            await self.disconnect()

    async def send_file(self, entity: hints.EntityLike, file: typing.Union[hints.FileLike, typing.Sequence[hints.FileLike]]) -> Message | None:
        try:
            return await self.__client.send_file(entity, file)
        except Exception as ex:
            self.__log.error(ex, "Ошибка при отправке фото")

    async def disconnect(self):
        try:
            await self.__client.disconnect()
            self.__log.error("Отключение")
        except Exception as ex:
            self.__log.error(ex, "Ошибка при отключении")