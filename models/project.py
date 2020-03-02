from db import MONGO

class ProjectModel:

    _id = ''
    title = ''
    description = ''

    def __init__(self, title, description):
        self.title = title
        self.description = description

    @classmethod
    def findAll(self):
        projects = []
        for project in MONGO.db.projects.find():
            if project['_id']:
                project['_id'] = str(project['_id'])
            projects.append(project)
        print(projects)
        return {'error': False, 'message': {'projects': projects}}

    def insert(self):
        project_exist = MONGO.db.projects.find_one({'title': self.title})
        if project_exist:
            return {'error': True, 'message': {'error': 'project already exists'}}
        project_created = MONGO.db.projects.insert({'title': self.title, 'description': self.description})
        if project_created:
            return {'error': False, 'message': {'success': 'project created'}}
        return {'error': True, 'message': {'error': 'project not created'}}
