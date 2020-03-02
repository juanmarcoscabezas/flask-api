from flask_restful import Resource, reqparse
from models.project import ProjectModel
from flask_jwt_extended import jwt_required

PARSER = reqparse.RequestParser()
PARSER.add_argument('title', help='This field cannot be blank', required=True)
PARSER.add_argument('description', help='This field cannot be blank', required=True)

class Project(Resource):
    @jwt_required
    def get(self):
        res = ProjectModel.findAll()
        return {'message': res['message']}
    def post(self):
        data = PARSER.parse_args()
        project = ProjectModel(data.title, data.description)
        res = project.insert()
        return {'message': res['message']}

class Projects(Resource):
    def get(self):
        pass

