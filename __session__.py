import socks 
import logging
import colorama

from telethon.sync import TelegramClient

from Accest.log import Log

from config.config import Config

from colorama import Fore

logging.basicConfig(level = logging.INFO)

colorama.init(autoreset = True)

while True:
    name: str = input("Введите имя: ")

    proxy_ = None
    try:
        proxy_ = (
            socks.SOCKS5, 
            Config.proxy['host'], 
            Config.proxy['port'], 
            Config.proxy['username'], 
            Config.proxy['password']
        )

        client = TelegramClient(
            name, 
            Config.API_ID, 
            Config.API_HASH, 
            proxy = proxy_, 
            system_version = Config.system_version, 
            device_model   = Config.device_model
        )
        client.start()
        logging.info("successfull")
    except Exception as ex:
        logging.error(Fore.RED + f"{ex.__class__.__name__}: {ex}")