from . import auth_blp as blp, doc_login_required
from flask.views import MethodView
from .parameters import LoginInfo
from .schemas import MsgRetSchema

@blp.route("/login")
class Login(MethodView):
    @blp.doc(summary='Login API',
             description='login user with username or code<br>'
                            'return token, abilities'
             )
    @blp.arguments(LoginInfo)
    @blp.response(MsgRetSchema, description='login ret')
    def post(self, login_info):
        print(login_info)
        return {'code': 0, 'msg': 'login successfully'}
