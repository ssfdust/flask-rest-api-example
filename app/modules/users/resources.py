from flask.views import MethodView
from . import usr_blp as blp
from modules.auth import doc_login_required

@blp.route('/user')
class User(MethodView):
    @doc_login_required
    def get(self):
        return {'code': 0}
