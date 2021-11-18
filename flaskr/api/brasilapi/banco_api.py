import requests
from flaskr.utils.config import Config


class BancoApi:
    def __init__(self) -> None:
        self.url = Config.get('URL_BRASILAPI') + str('/banks/v1/')


    def todos(self):
        return requests.get(url=self.url)