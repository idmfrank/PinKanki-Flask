# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from extract import json_extract

import requests
  
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Main(Resource):
  
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
  
        return jsonify({'message': 'Welcome to the PinKanki Flask REST App'})
  
    # Corresponds to POST request
    def post(self):
          
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201
  
  
# another resource to calculate the square of a number
class User(Resource):
    
    def get(self, userName):
      
        api_url = "https://randomuser.me/api/"
        response = requests.get(api_url)
        data = response.json()
        retValue = json_extract(data, 'username')
        return retValue

class UserData(Resource):
    
    def get(self):
      
        api_url = "https://randomuser.me/api/"
        response = requests.get(api_url)
        data = response.json()
        return data

  
# adding the defined resources along with their corresponding urls
api.add_resource(Main, '/')
api.add_resource(User, '/user/<userName>')
api.add_resource(UserData, '/userdata')
  
  
# driver function
if __name__ == '__main__':
  
    app.run(host='0.0.0.0', port=3245, debug = True)