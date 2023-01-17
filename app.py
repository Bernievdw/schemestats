from flask import Flask, request
from flask_restful import Resource, Api

# Instancing Flask + API
app = Flask(__name__)
api = Api(app)


fakeDatabase = {
    1:{'name':'Clean car'},
    2:{'name':'Write blog'},
    3:{'name':'Start stream'},
}

class Items(Resource):
    def get(self):
        return fakeDatabase

    def post(self):
        data = request.json
        item_id = len(fakeDatabase.keys()) + 1
        fakeDatabase[item_id] = {'name':data['name']}
        return fakeDatabase

class Item(Resource):
    def get(self, pk):
        return fakeDatabase[pk]

    def put(self, pk):
        data = request.json
        fakeDatabase[pk]['name'] = data['name']
        return fakeDatabase

api.add_resource(Items, '/')
api.add_resource(Item, '/<int:data>')

if __name__ == '__main__':
    app.run(debug=True)