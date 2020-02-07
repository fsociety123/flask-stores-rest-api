from flask_restful import Resource
from models.store_model import StoreModel

class Store(Resource):

    def get(self, name):
        #Get the store object
        store= StoreModel.get_item(name)

        #If there was a store
        if store:
            return store.json(), 200
        
        return {"message": "Store not found"}, 404


    def post(self, name):
        #Checking if the store already exists 
        if StoreModel.get_item(name):
            return {"message": f"A store with name {name} already exists."}, 400
        
        store= StoreModel(name)

        try:
            store.save_to_db()
        
        except:
            return{"message", "An error occured while creating the store"}, 500

        return store.json(), 201


    def delete(self, name):
        #Getting the store object
        store= StoreModel.get_item(name)
        #If the store exists then delete it
        if store:
            store.delete_from_db()
            return {"message": "Store deleted successfully."}
        
        return {"message": f"There is no store with name {name}"}, 400


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}