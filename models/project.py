from db import MONGO
from bson.objectid import ObjectId

class ProjectModel:

    _id = ''
    title = ''
    description = ''
    owner = ''

    def __init__(self, title, description, owner):
        self.title = title
        self.description = description
        self.owner = owner

    @classmethod
    def findAll(self, owner):
        projects = []
        for project in MONGO.db.projects.find({'owner': owner}):
            if project['_id']:
                project['_id'] = str(project['_id'])
            projects.append(project)
        return {'error': False, 'message': {'projects': projects}}
    
    @classmethod
    def findOne(self, _id):
        try:
            project = MONGO.db.projects.find_one_or_404({'_id': ObjectId(_id)})
            print(project)
            project['_id'] = str(project['_id'])
            return {'error': False, 'message': {'project': project}}
        except:
            return {'error': False, 'message': {'project': {}}}

    def insert(self):
        project_exist = MONGO.db.projects.find_one({'title': self.title, 'owner': self.owner})
        if project_exist:
            return {'error': True, 'message': {'error': 'project already exists'}}
        project_created = MONGO.db.projects.insert({'title': self.title, 'description': self.description, 'owner': self.owner})
        if project_created:
            return {'error': False, 'message': {'success': 'project created'}}
        return {'error': True, 'message': {'error': 'project not created'}}
