from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'app secret key'

@app.route('/<login>')
def index(login):
    if 'counter' in session:
            session['counter'] += 1
    else:
        session['counter'] = 1
    
    # session.pop('counter', None)
    
    return {"st": session['counter']}


app.run(host='192.168.16.70', port=5555)


#### Client test

def url_session():
    url = r'http://192.168.16.70:5555/vik'
    
    a = requests.get(url)
    print(a.content, '!')
    cookies = a.cookies
    
    b = requests.get(url, cookies=cookies)
    print(b.content, '!!')
    cookies = b.cookies

    c = requests.get(url, cookies=cookies)
    print(c.content, '!!!')

# url_session()