import asyncio

from telethon.sync import events, TelegramClient

from Accest.log            import Log
from Accest.tr             import tr
from Accest.client         import Client_
from Accest.captcha_solver import CaptchaSolver

from config.config import Config



class AnonRubot:
    name: str = tr.AnonRubotName
    log: Log = Log(tr.AnonRubotLog)
    count: int = 0

    captcha_solver: CaptchaSolver = CaptchaSolver(Config.captcha_api)



async def start_dialog_AnonRubot(
    client: TelegramClient, 
    flag_AnonRubot: dict[str, bool]
):
    client_: Client_ = Client_(client)

    @client_.on(events.NewMessage(from_users = AnonRubot.name))
    async def handle_new_message(event: events.NewMessage.Event):
        if tr.t1 in event.raw_text:
            msg = await client_.send_file(AnonRubot.name, Config.path_photo)
            if msg is not None:
                AnonRubot.count += 1
                AnonRubot.log.info(f"отправил сообщение (ФОТО) > {AnonRubot.count}")

                await asyncio.sleep(Config.delay)

            for i in Config.spam_text_AnonRubot:
                msg = await client_.send_message(AnonRubot.name, i)

                if msg is not None:
                    AnonRubot.count += 1
                    AnonRubot.log.info(f"отправил сообщение (ТЕКСТ) > {AnonRubot.count}")

                    await asyncio.sleep(Config.delay)

            await asyncio.sleep(Config.timeout)
            await client_.send_message(AnonRubot.name, tr.next_)

        elif tr.t2 in event.raw_text:
            await client_.send_message(AnonRubot.name, tr.search)
            
            AnonRubot.log.warning(f"со мной закончили связь, ищу следующего")

        elif tr.t3 in event.raw_text:
            msg = await client_.send_message(AnonRubot.name, str(Config.age_AnonRubot))
            if msg is not None:
                await client_.send_message(AnonRubot.name, tr.search)

                AnonRubot.log.warning(f"указал возраст {Config.age_AnonRubot}")
        
        elif tr.t4 in event.raw_text:
            AnonRubot.log.warning(f"собеседник уже есть, ищу следующего")
        
            await asyncio.sleep(Config.timeout)
            await client_.send_message(AnonRubot.name, tr.next_)

        elif tr.t5 in event.raw_text or tr.t6 in event.raw_text or tr.t10 in event.raw_text:
            if event.media and event.media.photo:
                _ = await event.download_media(file = "./downloaded_image.jpg")
                result = AnonRubot.captcha_solver.solve_captcha("downloaded_image.jpg")

                await client_.send_message(AnonRubot.name, f"{result}")

                AnonRubot.log.warning(f"решил капчу {result}")

        elif tr.t7 in event.raw_text:
            await client_.send_message(AnonRubot.name, tr.restartcaptcha)

            AnonRubot.log.warning("рестартанул капчу")

        elif tr.t8 in event.raw_text or tr.t9 in event.raw_text or tr.t11 in event.raw_text:
            AnonRubot.log.error("аккаунт будет работать потом, щас блок")

            flag_AnonRubot["AnonRubot_flag"] = False
    
        else:
            AnonRubot.log.error(f"Не обработанное сообщение от бота: {event.raw_text}")
