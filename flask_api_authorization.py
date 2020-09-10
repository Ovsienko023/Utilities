@app.route('/test', methods=['POST', 'DELETE', 'GET'])
def test_func():
    data = request.authorization
    print(data)
    return {"status": True}


# --------- Client

import requests

url = r'http://127.0.0.1:5000/test'
a = requests.post(url, auth=('Bob', 'asd123'))
print(a)