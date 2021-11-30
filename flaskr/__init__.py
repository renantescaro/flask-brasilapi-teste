from flask import Flask
from flaskr.controllers.inicial_ctrl import bp as bp_inicial
from flaskr.controllers.feriado_ctrl import bp as bp_feriado
from flaskr.controllers.banco_ctrl import bp as bp_banco
from flaskr.controllers.ddds_ctrl import bp as bp_ddds


def create_app(test_config=None):
    app = Flask(
        __name__,
        static_url_path = '/static',
        static_folder   = 'static',
        instance_relative_config = True )

    app.config.from_mapping(
        SECRET_KEY   = 'super secret key',
        SESSION_TYPE = 'filesystem',
        JSONIFY_PRETTYPRINT_REGULAR = False )


    # adicionar rotas
    app.register_blueprint(bp_inicial)
    app.register_blueprint(bp_feriado)
    app.register_blueprint(bp_banco)
    app.register_blueprint(bp_ddds)
    return app