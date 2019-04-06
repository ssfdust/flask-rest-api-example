from extensions import api
from functools import wraps
from flask_jwt_extended import jwt_required

auth_blp = api.blueprint("auth", "auth",
                     url_prefix="/api/v1/auth",
                     description="Auth Module")

def doc_login_required(func):
    # 'Decorate' the function with the real authentication decorator

    # Create the wrapped function.  This just calls the 'decorated' function
    @wraps(func)
    def wrapper(*args, **kwargs):
        return jwt_required(*args, **kwargs)

    # Update the api docs on the wrapped function and return it to be
    # further decorated by other decorators
    parameters = {
        'name': 'Authorization',
        'in': 'header',
        'description': 'Authorization: Bearer <access_token>',
        'required': 'true'
    }

    wrapper._apidoc = getattr(func, '_apidoc', {})
    wrapper._apidoc.setdefault('parameters', []).append(parameters)
    wrapper._apidoc.setdefault('security', [{'api_key': []}])

    return wrapper

from . import resources # NOQA
