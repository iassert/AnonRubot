import os
import colorama

from Accest.tr import tr

colorama.init(autoreset = True)

class Config:
    sessions_path: str = f"./{tr.sessions}/"

    path_photo: str = f"./photo.jpg"
    spam_text_AnonRubot: list[str] = []
    age_AnonRubot: int = 17

    timeout: int = 10
    delay:   int = 1

    captcha_api: str
    
    proxy: dict[str, str | int] = {
        'host': "",
        'port': 0,
        'username': "",
        'password': "",
    }

    system_version: str
    device_model:   str
    
    API_ID: int
    API_HASH: str
    