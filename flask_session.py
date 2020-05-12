from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'app secret key'

@app.route('/')
def index():
    if 'counter' in session:
        print(session)
        session['counter'] += 1
    else:
        session['counter'] = 1
    return 'Counter: ' + str(session['counter'])


app.run(host='192.168.16.70', port=5555)


#### Client test

def url_session():
    url = r'http://192.168.16.70:5555/'
    data = {"1":"wqdw"}
    a = requests.get(url)
    print(a.content)
    cookies = a.cookies

    b = requests.get(url, cookies=cookies)
    print(b.content)

# url_session()