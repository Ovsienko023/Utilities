from flask import Flask, request, render_template
from flask_cors import CORS
from flask import abort
from functools import wraps

app = Flask(__name__)
CORS(app)

def decor(func):
    @wraps(func)
    def wrapper():
        a = func()
        data = request.authorization
        print(data)
        if data['username'] == 'Bob':
            return a
        return {"status": "error"}
    return wrapper


@app.route('/test', methods=['POST', 'DELETE', 'GET'])
@decor
def test_func():
    data = request.authorization
    print(data)
    return {"status": True} # render_template('index.html')
    # return abort(404)


app.run(debug=True)

# ---------------Client----------------

import requests

url = r'http://127.0.0.1:5000/test'
# data = {"login": "Bob", "messages": "I'm the best!"}
# a = requests.post(url, json=data)
a = requests.post(url, auth=('Bob', 'asd123'))
print(a.json())
