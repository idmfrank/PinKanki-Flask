from flask import Flask, jsonify
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


# Load config
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Get an auth token

# Build request body
auth_body = {}
auth_body['InstanceName'] = os.environ['ARCH_INSTANCE']
auth_body['Username'] = os.environ['ARCH_USER']
auth_body['UserDomain'] = str(os.environ.get('ARCH_DOMAIN') or '') # UserDomain should be empty string not 'None'
auth_body['Password'] = os.environ['ARCH_PWD']


@app.route('/login', methods=['GET'])
def login():
    login_url = os.environ['ARCH_HOST'] + config['Resources']['Login']

    r = requests.post(login_url, json=auth_body)

    # print(r.status_code)
    # print(r.json())

    SessionToken = r.json()['RequestedObject']['SessionToken']
    json_text = jsonify(r.json())

    # and then you can return it to the front end in the response body like this
    return json_text

@app.route('/users', methods=['GET'])
def users():
    login_url = os.environ['ARCH_HOST'] + config['Resources']['Login']

    r = requests.post(login_url, json=auth_body)

    #print(u.json())
    SessionToken = r.json()['RequestedObject']['SessionToken']

    # print(r.status_code)
    # print(r.json())
    user_url = os.environ['ARCH_HOST'] + config['Resources']['User']
    u = requests.get(user_url, headers={"Authorization": "Archer session-id=" + SessionToken})

    json_text = jsonify(u.json())

    # and then you can return it to the front end in the response body like this
    return json_text




# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)