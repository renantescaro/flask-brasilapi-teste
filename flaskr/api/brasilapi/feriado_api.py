import requests
from flaskr.utils.config import Config


class FeriadoApi:
    def __init__(self) -> None:
        self.url = Config.get('URL_BRASILAPI') + str('/feriados/v1/')


    def por_ano(self, ano:int):
        return requests.get(url=self.url+str(ano))