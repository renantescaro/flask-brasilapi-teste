import json
from flask import Blueprint, render_template
from flaskr.services.brasilapi.ddd_sv import DddSv

bp = Blueprint(
    'ddds',
    __name__,
    template_folder='ddds' )


class DddsCtrl:
    @bp.route('/ddds', methods=['GET'])
    def consulta():
        return render_template(
            'ddds/consulta.html' )


    @bp.route('/ddds/<ddd>', methods=['GET'])
    def consultar(ddd):
        return json.dumps(DddSv().cidades_por_ddd(ddd))