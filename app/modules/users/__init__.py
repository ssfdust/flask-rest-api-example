from flask_rest_api import Api

api = Api("usr")
usr_blp = api.blueprint("users", "users",
                        url_prefix="/api/v1/users",
                        description="User Resources")

from . import resources # NOQA
