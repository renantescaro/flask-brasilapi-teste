import requests
from flaskr.utils.config import Config


class DddApi:
    def __init__(self) -> None:
        self.url = Config.get('URL_BRASILAPI') + str('/ddd/v1/')


    def por_ddd(self, ddd:int):
        return requests.get(url=self.url+str(ddd))