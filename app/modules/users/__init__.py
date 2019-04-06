from extensions import api

usr_blp = api.blueprint("users", "users",
                        url_prefix="/api/v1/users",
                        description="User Resources")

from . import resources # NOQA
