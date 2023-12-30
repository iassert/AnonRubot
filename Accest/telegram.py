import socks

from telethon.sync import TelegramClient

from config.config import Config

from .log import Log


async def connect_to_telegram(
    session_path: str, 
    api_id: int   = Config.API_ID, 
    api_hash: str = Config.API_HASH
):
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
            session_path, 
            api_id, 
            api_hash, 
            proxy = proxy_, 
            system_version = Config.system_version, 
            device_model   = Config.device_model
        )
        await client.connect()

        if not await client.is_user_authorized():
            Log().error(f'{session_path} - невалидный')
            return

        Log().info(f'Взял сессию в работу - {session_path}')
        return client
    except Exception as ex:
        Log().error(ex)
