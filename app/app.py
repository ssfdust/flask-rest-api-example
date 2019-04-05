from flask import Flask
from config import DevConfig
from modules.auth import api as auth_api
from modules.users import api as usr_api

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
    auth_api.init_app(app)
    usr_api.init_app(app, spec_kwargs=spec_kwargs)

    return app
