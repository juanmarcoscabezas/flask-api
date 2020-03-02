from db import MONGO
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel:

    _id = ''
    email = ''
    password = ''

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def insert(self):
        user_exist = MONGO.db.users.find_one({'email': self.email})
        if user_exist:
            return {'error': True, 'message': {'error': 'user already exists'}}
        _hash = generate_password_hash(self.password)
        user_created = MONGO.db.users.insert({'email': self.email, 'password': _hash})
        if user_created:
            return {'error': False, 'message': {'success': 'user created'}}
        return {'error': True, 'message': {'error': 'user not created'}}
    
    def check_password(self):
        user_exist = MONGO.db.users.find_one({'email': self.email})
        if user_exist:
            if check_password_hash(user_exist['password'], self.password):
                return {'error': False, 'message': {'success': 'Loged in as {}'.format(user_exist['email'])}}
            return {'error': True, 'message': {'error': 'wrong email or password'}}
        return {'error': True, 'message': {'error': 'wrong email or password'}}