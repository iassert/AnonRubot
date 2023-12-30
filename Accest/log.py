from .tr import tr

from colorama import Fore, Style


class Log:
    def __init__(self, name: str = "") -> None:
        self.__name: str = name

    def info(self, text: str):
        print(Fore.GREEN + Style.BRIGHT + self.__name + text)

    def warning(self, text: str) -> None:
        print(Fore.YELLOW + Style.BRIGHT + self.__name + text)

    def error(self, text: str | Exception, caption: str = "") -> None:
        if isinstance(text, str):
            print(Fore.RED + tr.error + self.__name + text)
        elif isinstance(text, Exception):
            ex = text
    
            print(Fore.RED + tr.error + self.__name + caption + f":{ex.__class__.__name__}:{ex}")
