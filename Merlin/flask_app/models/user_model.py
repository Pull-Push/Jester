from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'[a-zA-Z\'.+_-]')


class User:
    def __init__(self,data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.dateCreated = data['dateCreated']
        self.dateUpdated = data['dateUpdated']
        
    #< ALL METHODS FOR THE INDIVIDUAL CLASSES GO IN THE APPROPRIATE MODELS FILE
    @classmethod
    def save_user(cls,data):
        query = '''INSERT INTO users
        (username, email, password)
        VALUES(%(username)s,%(email)s,%(password)s);
        '''
        results = connectToMySQL('merlin_db').query_db(query,data)
        return results

    @classmethod
    def check_user(cls,data):
        print(data['email'])
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('merlin_db').query_db(query,data)
        if len(results)< 1:
            return False
        return cls(results[0])
    

    @classmethod
    def getby_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('merlin_db').query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validate(data):
        is_valid = True
        if not NAME_REGEX.match(data['first_name']):
            flash("First name must be letters only",'regerr')
            is_valid = False
        elif not NAME_REGEX.match(data['last_name']):
            flash("Last name must be letters only",'regerr')
            is_valid = False
        elif len(data['first_name']) < 3:
            flash("First Name Field Must Be At Least 3 Characters",'regerr')
            is_valid = False
        elif len(data['last_name']) < 3:
            flash("Last Name Field Must Be At Least 3 Characters",'regerr')
            is_valid = False            
        elif not EMAIL_REGEX.match(data['email']):
            flash("Please Enter a Valid Email",'regerr')
            is_valid = False
        elif User.check_user(data):
            flash("Email Already Exists",'regerr')
            is_valid = False
        elif len(data['password'])<8:
            flash('Passwords Must be 8 Characters','regerr')
            is_valid = False
        elif data['password'] != data['conf_pass']:
            flash("Passwords must match",'regerr')
            is_valid = False
        return is_valid