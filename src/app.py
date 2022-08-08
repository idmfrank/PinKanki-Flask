from flask import Flask, jsonify
from Archer import Archer
import yaml, requests, os

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    # suppose you have your data in the variable name_data
    name_data = { "firstName": "Frank", "lastName": "Wray" }

    # you can convert that variable into a json string like this
    json_text = jsonify(name_data)

    # and then you can return it to the front end in the response body like this
    return json_text


@app.route('/login', methods=['GET'])
def login():
    a = Archer()
    json_text = jsonify({'sessionToken': a.login()})
    a.logout()
    return json_text

@app.route('/users', methods=['GET'])
def users():
    a = Archer()
    a.login()
    users = a.getUsers()
    a.logout()
    return users

@app.route('/groups', methods=['GET'])
def groups():
    a = Archer()
    a.login()
    groups = a.getGroups()
    a.logout()
    return groups

@app.route('/roles', methods=['GET'])
def roles():
    a = Archer()
    a.login()
    roles = a.getRoles()
    a.logout()
    return roles

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)