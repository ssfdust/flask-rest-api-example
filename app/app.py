from flask import Flask
from config import DevConfig
from extensions import api
from modules import auth  # NOQA
from modules import users  # NOQA

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

    return app
