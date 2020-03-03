"""Start of app"""
from flask import Flask, make_response
from flask_restful import Api
from flask_jwt_extended import JWTManager

from db import MONGO
from controllers.auth import UserLogin, UserSignup, UserRefreshToken
from controllers.project import Project, Projects


APP = Flask(__name__)
API = Api(APP)

APP.config['MONGO_URI'] = 'mongodb://localhost:27017/projectllo'
APP.config['JWT_SECRET_KEY'] = 'secret-key'

MONGO.init_app(APP)
JWT = JWTManager(APP)

def unauthorized(message):
    """Mesage error when the user doesn't have token"""
    message = 'missing authorization header'
    return make_response({'message': {'error': message}}, 401)
JWT.unauthorized_loader(unauthorized)

def expired(message):
    """Mesage error when the token has expired"""
    message = 'token has expired'
    return make_response({'message': {'error': message}}, 401)
JWT.expired_token_loader(expired)

def invalid(message):
    """Mesage error when the token is invalid"""
    message = 'signature verification failed'
    return make_response({'message': {'error': message}}, 422)
JWT.invalid_token_loader(invalid)


API.add_resource(UserLogin, '/auth/login')
API.add_resource(UserSignup, '/auth/signup')
API.add_resource(UserRefreshToken, '/auth/refresh-token')
API.add_resource(Projects, '/projects')
API.add_resource(Project, '/projects/<string:_id>')

if __name__ == '__main__':
    APP.run(debug=True)
