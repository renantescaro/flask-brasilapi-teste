import json
from flask import Blueprint, render_template, redirect, url_for
from flaskr.services.brasilapi.feriado_sv import FeriadoSv

bp = Blueprint(
    'feriado',
    __name__,
    template_folder='templates' )


class FeriadoCtrl:
    @bp.route('/feriados', methods=['GET'])
    def feriados():
        ano = 2021
        return redirect(
            url_for('feriado.feriados_por_ano',
            ano = ano ))


    @bp.route('/feriados/<ano>', methods=['GET'])
    def feriados_por_ano(ano):
        return render_template(
            'feriados/listagem.html',
            titulo = 'Listagem de Feriados',
            dados  = json.dumps(FeriadoSv().por_ano(ano)) )