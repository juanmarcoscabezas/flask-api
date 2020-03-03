"""UserModel Module"""
from werkzeug.security import generate_password_hash, check_password_hash
from db import MONGO

class UserModel:
    """This class handle Users"""
    _id = ''
    email = ''
    password = ''

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def insert(self):
        """This method inserts an user to DB"""
        message = {}
        user_exist = MONGO.db.users.find_one({'email': self.email})
        if user_exist:
            message = {'error': 'user already exists'}
            return {'error': True, 'message': message}
        _hash = generate_password_hash(self.password)
        user_created = MONGO.db.users.insert({'email': self.email, 'password': _hash})
        if user_created:
            message = {'success': 'user created'}
            return {'error': False, 'message': message}
        message = {'error': 'user not created'}
        return {'error': True, 'message': message}

    def check_password(self):
        """This method checks if the given password is correct"""
        message = {}
        user_exist = MONGO.db.users.find_one({'email': self.email})
        if user_exist:
            if check_password_hash(user_exist['password'], self.password):
                message = {'success': 'Loged in as {}'.format(user_exist['email'])}
                return {'error': False, 'message': message}
            message = {'error': 'wrong email or password'}
            return {'error': True, 'message': message}
        message = {'error': 'wrong email or password'}
        return {'error': True, 'message': message}
