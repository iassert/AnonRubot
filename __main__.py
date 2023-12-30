import os
import asyncio

from Accest.log      import Log
from Accest.telegram import connect_to_telegram
from Accest.tr       import tr

from config.config import Config

from Handlers.AnonRubot import start_dialog_AnonRubot, AnonRubot

from colorama import Fore
from datetime import datetime

async def slow_print(text: str) -> None:
    for i in text:
        print(Fore.RED + i, end = '', flush = True)
        await asyncio.sleep(1e-10)

async def start_spam(
    session_path: str, 
    chat_acces_state: dict[str, bool]
):  
    client = await connect_to_telegram(session_path)
    if client is None:
        return

    await start_dialog_AnonRubot(
        client, 
        chat_acces_state, 
    )

    async with client:
        try:
            await client.send_message(AnonRubot.name, tr.start)

            await client.run_until_disconnected()
        except Exception as ex:
            Log().error(ex)

    Log().info(f'Сессия {session_path} завершена')

    if not chat_acces_state['AnonRubot_flag']:
        await client.disconnect()

async def check_flags(
    chat_acces_state: dict[str, bool], 
    event: asyncio.Event
):
    while True:
        if not chat_acces_state['AnonRubot_flag']:
            event.set()
            return
        await asyncio.sleep(1)

async def main():
    await slow_print(f"""
Author - https://t.me/static_assert
    _            _     ____   ____   _____  ____   _____ 
    \ \         / \   / ___| / ___| | ____||  _ \ |_   _|
  /\ \ \       / _ \  \___ \ \___ \ |  _|  | |_) |  | | 
 / /  \ \     / ___ \  ___) | ___) || |___ |  _ <   | | 
/_/    \_\   /_/   \_\|____/ |____/ |_____||_| \_\  |_|

{datetime.now().strftime("%d.%m.%Y %H:%M")}
""")
    
    if not os.path.exists(Config.sessions_path):
        os.mkdir(Config.sessions_path)

    sessions = os.listdir(Config.sessions_path)
    if sessions == []:
        return

    while True:
        for session in sessions:
            session_path = Config.sessions_path + session
            chat_access_state = {
                'AnonRubot_flag': True
            }
            event = asyncio.Event()

            asyncio.create_task(check_flags(chat_access_state, event))
            await start_spam(
                session_path, 
                chat_access_state
            )

if __name__ == '__main__':
    asyncio.run(main())
input()