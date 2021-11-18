from flaskr.api.brasilapi.banco_api import BancoApi


class BancoSv:
    def todos(self):
        response = BancoApi().todos()
        if response.status_code == 200:
            return response.json()
        return None


    def por_codigo(self, codigo:int):
        response = BancoApi().por_codigo(codigo)
        if response.status_code == 200:
            return response.json()
        return None