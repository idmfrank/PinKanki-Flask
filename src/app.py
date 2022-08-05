from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    # suppose you have your data in the variable name_data
    name_data = { "firstName": "Frank", "lastName": "Wray" }

    # you can convert that variable into a json string like this
    json_text = jsonify(name_data)

    # and then you can return it to the front end in the response body like this
    return json_text


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)