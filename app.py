from flask import Flask, request, send_file
from flask_restful import Api
from security import authenticate, identity
from flask_jwt import JWT
from resources.item import Item, ItemList
from resources.user import UserRegister
from resources.store import Store, StoreList
from db import db

#Standard step to geve the app a unique name
app= Flask(__name__)

#creating a secret key
app.secret_key= 'flask'

#Tell sqlalchemy to use the database created by sqlite
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///data.db'

#Flask-sqlalchemy won't track the changes made to the objects but sqlalchemy will do it
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

#Creating the api
api= Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

#This will create a jwt object which will create an endpoint /auth for authentication and return a token
jwt= JWT(app, authenticate, identity)

api.add_resource(Store, "/store/<string:name>")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(StoreList, "/stores")

#This condition will only be true when this file is executed. If this file is imported then it will be false
if __name__ == "__main__":
    db.init_app(app)
    app.run(port= 5000, debug= True)
