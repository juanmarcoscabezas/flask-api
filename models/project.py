"""ProjectModel Module"""
from bson.objectid import ObjectId
from db import MONGO

class ProjectModel:
    """This class handles Projects"""
    _id = ''
    title = ''
    description = ''
    owner = ''

    def __init__(self, title, description, owner):
        self.title = title
        self.description = description
        self.owner = owner

    @classmethod
    def find_all(cls, owner):
        """this method finds all Projects asigned to an user"""
        message = {}
        projects = []
        for project in MONGO.db.projects.find({'owner': owner}):
            if project['_id']:
                project['_id'] = str(project['_id'])
            projects.append(project)
        message = {'projects': projects}
        return {'error': False, 'message': message}

    @classmethod
    def find_one(cls, _id):
        """This method finds a Project by id"""
        try:
            project = MONGO.db.projects.find_one_or_404({'_id': ObjectId(_id)})
            print(project)
            project['_id'] = str(project['_id'])
            return {'error': False, 'message': {'project': project}}
        except:
            return {'error': False, 'message': {'project': {}}}

    def insert(self):
        """This method creates a Project"""
        message = {}
        project_exist = MONGO.db.projects.find_one({'title': self.title, 'owner': self.owner})
        if project_exist:
            message = {'error': 'project already exists'}
            return {'error': True, 'message': message}
        project_created = MONGO.db.projects.insert({
            'title': self.title,
            'description': self.description,
            'owner': self.owner
        })
        if project_created:
            return {'error': False, 'message': {'success': 'project created'}}
        return {'error': True, 'message': {'error': 'project not created'}}
