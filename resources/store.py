from flask_restful import Resource

from models.store import StoreModel

class StoreResource(Resource):

    def get(self, name):                
        store = StoreModel.find_by_name(name)
        
        if store:
            return store.json()
        
        return {'message': f'There is no store called {store} in the list.'}, 404        

    def post(self, name):                    
        if StoreModel.find_by_name(name):
            return {"message": "A store with the name '{}' is already in the database".format(name)}, 400
        
        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {"message": "An error ocurred while creating the store"}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()
        
        return {'message': 'Store deleted'}

class StoreListResource(Resource):
    def get(self):        
        return {"stores": [store.json() for store in StoreModel.find_all()]}
