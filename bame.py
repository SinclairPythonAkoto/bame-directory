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

# redirect to login
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to sign in first')
            return redirect(url_for('login'))
    return wrap

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

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('usernme')
        userPassword = request.form.get('password')
        # users = dict(username=user, password=userPassword)
        db.child("BAMEusers").push([user, userPassword])
        bameUsers = db.child("BAMEusers").get()
        userList = bameUsers.val()
        return render_template('layout.html', bameList=userList.values())

    # return print(userList.values())
    # return render_template('layout.html', userList=userList.values())
    # return f"hello {userList}!"

# @app.route('/')
# def home():
#     return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug=True)
