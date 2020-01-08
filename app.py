import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity

from resources.user import UserRegister
from resources.item import ItemResource, ItemList
from resources.store import StoreResource, StoreListResource

# from db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'cesar'

api = Api(app) # Allows to add Resources. Every Resource must be a class.

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(ItemResource, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(StoreResource, '/store/<string:name>')
api.add_resource(StoreListResource, '/stores')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000)