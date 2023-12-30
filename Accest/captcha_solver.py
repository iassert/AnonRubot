from twocaptcha import TwoCaptcha

from .log import Log

class CaptchaSolver:
    def __init__(self, 
        api_key: str
    ):
        self.api_key: str = api_key
        self.solver: TwoCaptcha = TwoCaptcha(api_key)

    def solve_captcha(self, 
        image_path: str
    ):
        try:
            return self.solver.normal(image_path)['code']
        except Exception as ex:
            Log().error(ex, "Ошибка при решение капчи")
            return
