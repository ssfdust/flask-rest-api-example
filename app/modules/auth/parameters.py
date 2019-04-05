from marshmallow import Schema, fields
from . import auth_blp

@auth_blp.definition('login_info')
class LoginInfo(Schema):
    username = fields.String()
    password = fields.String()
