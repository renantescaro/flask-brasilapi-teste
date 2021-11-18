from flaskr.api.brasilapi.feriado_api import FeriadoApi


class FeriadoSv:
    def por_ano(self, ano:int):
        response = FeriadoApi().por_ano(ano)
        if response.status_code == 200:
            return response.json()
        return None