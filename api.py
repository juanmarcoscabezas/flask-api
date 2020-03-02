"""Start of app"""
from flask import Flask, make_response
from flask_restful import Api
from flask_jwt_extended import JWTManager

from db import MONGO
from controllers.auth import UserLogin, UserSignup
from controllers.project import Project, Projects


APP = Flask(__name__)
API = Api(APP)

APP.config['MONGO_URI'] = 'mongodb://localhost:27017/projectllo'
APP.config['JWT_SECRET_KEY'] = 'secret-key'

MONGO.init_app(APP)
JWT = JWTManager(APP)

def unauthorized(err):
    return make_response({'message': 'missing authorization header'}, 401)

JWT.unauthorized_loader(unauthorized)


API.add_resource(UserLogin, '/login')
API.add_resource(UserSignup, '/signup')
API.add_resource(Project, '/projects')

if __name__ == '__main__':
    APP.run(debug=True)
