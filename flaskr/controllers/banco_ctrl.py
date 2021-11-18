import json
from flask import Blueprint, render_template, redirect, url_for
from flaskr.services.brasilapi.banco_sv import BancoSv

bp = Blueprint(
    'banco',
    __name__,
    template_folder='templates' )


class BancosCtrl:
    @bp.route('/bancos', methods=['GET'])
    def bancos():
        return render_template(
            'bancos/listagem.html',
            titulo = 'Listagem de Bancos',
            dados  = json.dumps(BancoSv().todos() ) )


    @bp.route('/bancos/<codigo>', methods=['GET'])
    def banco_por_codigo(codigo):
        ano = 2021
        return redirect(
            url_for('banco.bancos',
            ano = ano ))