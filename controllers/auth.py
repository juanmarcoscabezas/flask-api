from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import create_access_token, create_refresh_token

PARSER = reqparse.RequestParser()
PARSER.add_argument('email', help='This field cannot be blank', required=True)
PARSER.add_argument('password', help='This field cannot be blank', required=True)

class UserLogin(Resource):
    def post(self):
        data = PARSER.parse_args()
        user = UserModel(data.email, data.password)
        res = user.check_password()
        if not res['error']:
            res['message']['access_token'] = create_access_token(identity=user.email)
            res['message']['refresh_token'] = create_refresh_token(identity=user.email)
            return {'message': res['message']}
        return {'message': res['message']}

class UserSignup(Resource):
    def post(self):
        data = PARSER.parse_args()
        user = UserModel(data.email, data.password)
        res = user.insert()
        if not res['error']:
            res['message']['access_token'] = create_access_token(identity=user.email)
            res['message']['refresh_token'] = create_refresh_token(identity=user.email)
            return {'message': res['message']}
        return {'message': res['message']}