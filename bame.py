import pyrebase
from flask import *

config = {
    "apiKey": "AIzaSyDKrW_cr5X6QRF_E4vA1phbQcP9urHMbdk",
    "authDomain": "bame-c5ecc.firebaseapp.com",
    "databaseURL": "https://bame-c5ecc.firebaseio.com",
    "projectId": "bame-c5ecc",
    "storageBucket": "bame-c5ecc.appspot.com",
    "messagingSenderId": "87535704965",
    "appId": "1:87535704965:web:5a2aaa61776041199242ec",
    "measurementId": "G-TCKXXBR3F8"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def test():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
