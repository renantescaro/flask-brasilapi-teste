from flaskr.api.brasilapi.ddd_api import DddApi


class DddSv:
    def cidades_por_ddd(self, ddd:int):
        response = DddApi().por_ddd(ddd)
        if response.status_code == 200:
            cidades = response.json()['cities']
            estado  = response.json()['state']

            dados = []
            for cidade in cidades:
                dados.append({
                    'cidade' : cidade,
                    'estado' : estado })
            return dados
        return None