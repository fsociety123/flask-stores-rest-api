import sqlite3
from flask_restful import Resource, reqparse
from models.user_model import UserModel

class UserRegister(Resource):

    #Defining a parser
    parser= reqparse.RequestParser()

    #Adding arguments to the parser
    parser.add_argument("username", required= True, type= str, help= "This field cannot be blank.")
    parser.add_argument("password", required= True, type= str, help= "This field cannot be blank.")

    def post(self):

        #Parsing the arguments
        data= UserRegister.parser.parse_args()

        #Check if the user already exists
        if UserModel.get_user_username(data['username']):
            return {"Message": "A user with this username already exists."}

        user= UserModel(**data)

        user.sav_to_db()

        return {"Message": "User created successfully."}, 201

