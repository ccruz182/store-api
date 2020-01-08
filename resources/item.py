from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel

class ItemResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float, 
        required=True, 
        help="This field cannot be left blank"
    )
    parser.add_argument('store_id',
        type=int, 
        required=True, 
        help="This field cannot be left blank"
    )

    @jwt_required()   
    def get(self, name):                
        item = ItemModel.find_by_name(name)
        
        if item:
            return item.json()
        
        return {'message': f'There is no item called {name} in the list.'}, 404        

    def post(self, name):        
        data = ItemResource.parser.parse_args()
        inserted_item = ItemModel(name, **data)

        try:
            inserted_item.save_to_db()
        except:
            return {"message": "An error ocurred inserting the item"}, 500
                        
        return inserted_item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            print("--", item, type(item), "--")
            item.delete_from_db()
            return {'message': f'Item {name} was deleted'}
        
        return {'message': f'No Item {name} in database'}

    def put(self, name):        
        data = ItemResource.parser.parse_args()
                
        item = ItemModel.find_by_name(name)

        if item is None: # There is an item already, just update.            
            item = ItemModel(name, **data)
        else:            
            item.price = data['price']
        
        item.save_to_db()
        
        return item.json(), 200


class ItemList(Resource):
    def get(self):
        items = ItemModel.find_all()

        _items = []

        for item in items:
            _items.append(item.json())

        return {'items': _items}