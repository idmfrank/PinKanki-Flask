# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from extract import json_extract

import requests
  
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

api_url = "https://random-data-api.com/api/users/random_user"

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
class UserField(Resource):
    
    def get(self, fieldName):
      
        response = requests.get(api_url)
        data = response.json()
        retValue = json_extract(data, fieldName)
        return retValue

class UserData(Resource):
    
    def get(self):
      
        response = requests.get(api_url)
        data = response.json()
        fieldList = []
        for key in data:
          fieldList.append(key)
        return fieldList
  
# adding the defined resources along with their corresponding urls
api.add_resource(Main, '/')
api.add_resource(UserField, '/userdata/<fieldName>')
api.add_resource(UserData, '/userdata')
  
# driver function
if __name__ == '__main__':
  
    app.run(host='0.0.0.0', port=3245, debug = True)