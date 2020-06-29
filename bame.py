import pyrebase
from flask import *

config = {
    "apiKey": "AIzaSyDzGHV_bWTwsZbdAGkiNj11sLZ9khKf43E",
    "authDomain": "flaskfirebase-869f6.firebaseapp.com",
    "databaseURL": "https://flaskfirebase-869f6.firebaseio.com",
    "projectId": "flaskfirebase-869f6",
    "storageBucket": "flaskfirebase-869f6.appspot.com",
    "messagingSenderId": "716659971362",
    "appId": "1:716659971362:web:258c468b0a8434467e817b",
    "measurementId": "G-D0K2VY1HVT"
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
            return render_template('layout.html', t=to.values()) # .values() will print all the values in the 'to' object (t in jinja)
        elif request.form.get('submit') == 'delete':
            # db.child("todo").equal_to("foodie").remove()
        # return render_template('index.html', t=to.values())
            db.child("todo").remove() # this removes ALL database values
        return render_template('layout.html')
    return render_template('layout.html')

# @app.route('/')
# def home():
#     return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug=True)
