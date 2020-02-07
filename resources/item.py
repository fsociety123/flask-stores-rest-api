from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item_model import ItemModel
#The first resource
class Item(Resource):

    #Request parsing is done to extract only the needed parameters and leave the rest
    parser= reqparse.RequestParser()

    parser.add_argument("price", type= float, required= True, help= "This field cannot be blank")
    parser.add_argument("store_id", type= int, required= True, help= "A store id is required")

    #This method overrides the parent class method
    @jwt_required()
    def get(self, name):
        
        result= ItemModel.get_item(name)

        if result: 
            return result.json(), 200

        return {"message": "Item not found."}, 404

    
    #This method overrides the parent class method
    def post(self, name):

        #Let's check if the item already exists
        if ItemModel.get_item(name):
            return {'message': f"An item with the name {name} already exists"}, 400
        
        #Getting the json passed when the api is called
        #Gives error when content-type is not set to json
        #Has arg silent to not give an error but return None
        data= Item.parser.parse_args()

        item= ItemModel(name,data['price'], data['store_id'])
        
        try:
            item.save_to_db()

        except:
            return {"message": "Error while inserting the item"}, 500 #Internal server error

        return item.json(), 201


    def delete(self, name):

        item= ItemModel.get_item(name)
        if item:
            item.delete_from_db()
            return {"message": "Item deleted"}

        else:
            return {"message": "Item not found"}

        


    def put(self, name):

        #Get the data
        data= Item.parser.parse_args()

        #Returns item if it already exists else None
        item= ItemModel.get_item(name)

        #If the item doesn't exist
        if item is None:
            item= ItemModel(name, data['price'], data['store_id'])
        else:
            item.price= data['price']
            item.store_id= data['store_id']
        
        item.save_to_db()
        
        return item.json()

#Adding the item list resource
class ItemList(Resource):

    def get(self):

        return {"Items": [item.json() for item in ItemModel.query.all()]}