from flask_restful import Resource, reqparse
from models.project import ProjectModel
from flask_jwt_extended import jwt_required, get_jwt_identity

PARSER = reqparse.RequestParser()
PARSER.add_argument('title', help='This field cannot be blank', required=True)
PARSER.add_argument('description', help='This field cannot be blank', required=True)

class Projects(Resource):
    @jwt_required
    def get(self):
        owner = get_jwt_identity()
        res = ProjectModel.findAll(owner)
        return {'message': res['message']}

    @jwt_required
    def post(self):
        data = PARSER.parse_args()
        owner = get_jwt_identity()
        print(owner)
        project = ProjectModel(data.title, data.description, owner)
        res = project.insert()
        return {'message': res['message']}

class Project(Resource):
    def get(self):
        pass

