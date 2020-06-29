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
def basic():
    if request.method == 'POST':
        if request.form.get('submit') == 'add':
            name = request.form.get('nameVal')
            # this creates a collection called todo in DB
            # it also adds the 'name' variable value in the collection
            db.child("todo").push(name)
            # line 30 & 31 is to set up the read / get db method
            todo = db.child("todo").get() # set name of collection a variable
            to = todo.val() # encase the collection variable with a new variable, this allows you to put data back into web with jinja
            return render_template('index.html', t=to.values()) # .values() will print all the values in the 'to' object (t in jinja)
        elif request.form.get('submit') == 'delete':
            # db.child("todo").equal_to("foodie").remove()
        # return render_template('index.html', t=to.values())
            db.child("todo").remove() # this removes ALL database values
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
