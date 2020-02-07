import sqlite3
from db import db

class UserModel(db.Model):

    #Letting sqlalchemy know about the table and columns
    __tablename__= "users"
    id= db.Column(db.Integer, primary_key= True)
    username= db.Column(db.String)
    password= db.Column(db.String)

    def __init__(self, username, password):
        self.username= username
        self.password= password

    def sav_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_user_username(cls, username):
       return cls.query.filter_by(username= username).first()

    @classmethod
    def get_user_id(cls, _id):
        return cls.query.filter_by(id= _id).first()