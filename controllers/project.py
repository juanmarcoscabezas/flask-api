"""ProjectController module"""
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.project import ProjectModel

PARSER = reqparse.RequestParser()
PARSER.add_argument('title', help='This field cannot be blank', required=True)
PARSER.add_argument('description', help='This field cannot be blank', required=True)

class Projects(Resource):
    """This class handles Projects requests"""
    @jwt_required
    def get(self):
        """this method gets all Projects"""
        owner = get_jwt_identity()
        res = ProjectModel.find_all(owner)
        return {'message': res['message']}

    @jwt_required
    def post(self):
        """This method handle the creation of new Projects"""
        data = PARSER.parse_args()
        owner = get_jwt_identity()
        project = ProjectModel(data.title, data.description, owner)
        res = project.insert()
        return {'message': res['message']}

class Project(Resource):
    """This class handles specific Projects requests"""
    @jwt_required
    def get(self, _id):
        """this method gets a Project by id"""
        res = ProjectModel.find_one(_id)
        return {'message': res['message']}

    @jwt_required
    def put(self, _id):
        """this method updates a Project by id"""

    @jwt_required
    def delete(self, _id):
        """this method delete a Project by id"""
