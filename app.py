from flask import Flask
from flask_restful import Resource, Api

# Instancing Flask + API
app = Flask(__name__)
api = Api(app)


fakeDatabase = {
    1:{'name':'Clean car'},
    2:{'name':'Write blog'},
    3:{'name':'Start stream'},
}

class Stats(Resource):
    def get(self):
        return fakeDatabase
class Stat(Resource):
    def get(self, data):
        return fakeDatabase[data]

api.add_resource(Stats, '/')
api.add_resource(Stat, '/<int:data>')

if __name__ == '__main__':
    app.run(debug=True)