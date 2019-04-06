from flask import Flask
from config import DevConfig
from extensions import api

def create_app(config=''):
    app = Flask("Authorization")
    app.config.from_object(DevConfig)

    spec_kwargs = {
        'components': {
            'securitySchemes': {
                'api_key': {
                    'type': 'http',
                    'scheme': 'bearer',
                    'bearerFormat': 'JWT'
                }
            }
        }
    }
    api.init_app(app, spec_kwargs=spec_kwargs)
    register_blp(api)

    return app

def register_blp(api):
    from modules.auth import auth_blp
    from modules.users import usr_blp

    api.register_blueprint(auth_blp)
    api.register_blueprint(usr_blp)
