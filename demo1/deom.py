import pyrebase
from flask import *
from random import randint
import requests

app = Flask(__name__)
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

auth = firebase.auth()
db = firebase.database()

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("layout.html")

@app.route("/search", methods=['GET','POST'])
def search():
    if request.method == 'POST':
        selectCategory = request.form.get("selectCategory")
        search = request.form.get("search")
        # search = search.split(", ")
        if selectCategory == "arts":
            # select the art category in the Firebase database
            artCategory = db.child("Bame_Business").child("business").child("arts_Media_Tech").get()
            # list comprehension to list every item within the category - this is now in a list
            artCat = [x.val() for x in artCategory.each()]
            # calculate the amount of items (entries) in the category
            art_category = len(artCat)
            # we now put this into a range so its readable in a list format
            art_category = range(art_category)
            # split seperate keywords into a list
            search = search.split(", ")
            # calculate how many words in the search list
            s = len(search)
            # put the number into a range so its readable in a list format
            s = range(s)


            for x in s: # for each keyword selected..
                for y in art_category: # for every entry in the category..
                # if the search keyword matches with the entry keyword then release data
                    if search[x] in artCat[y]['keyWords']:
                        return render_template(
                        'arts.html',
                        business=artCat[y]['businessName'],
                        founder=artCat[y]['userName'],
                        year=artCat[y]['businessStartYear'],
                        category=artCat[y]['businessCategory'],
                        description=artCat[y]['businessDescription'],
                        address=artCat[y]['businessAddress'],
                        email=artCat[y]['businessEmail'],
                        phone=artCat[y]['businessNumber'],
                        web=artCat[y]['businessURL'],
                        tweet=artCat[y]['Twitter'],
                        insta=artCat[y]['Instagram'],
                        art_category=art_category, artCat=artCat)
                    else:
                        err = "Sorry, couldn't find what you were looking for. Please try again."
                        return render_template('home.html', err=err)
        elif selectCategory == "charity":
            charityCategory = db.child("Bame_Business").child("business").child("charities_SupportGroups").get()
            charityCat = [x.val() for x in charityCategory.each()]
            charity_category = len(charityCat)
            charity_category = range(charity_category)
            search = search.split(", ")
            s = len(search)
            s = range(s)
            for x in s:
                for x in charity_category:
                    if search[x] in charityCat[x]['keyWords']:
                        return render_template(
                        'charity.html',
                        business=charityCat[x]['businessName'],
                        founder=charityCat[x]['userName'],
                        year=charityCat[x]['businessStartYear'],
                        category=charityCat[x]['businessCategory'],
                        description=charityCat[x]['businessDescription'],
                        address=charityCat[x]['businessAddress'],
                        email=charityCat[x]['businessEmail'],
                        phone=charityCat[x]['businessNumber'],
                        web=charityCat[x]['businessURL'],
                        tweet=charityCat[x]['Twitter'],
                        insta=charityCat[x]['Instagram'],
                        charity_category=charity_category, charityCat=charityCat)
                    else:
                        err = "Sorry, couldn't find what you were looking for. Please try again."
                        return render_template('home.html', err=err)

# @app.route("/Arts-Media-Tech-Category", methods=['GET', 'POST']) # this is for post (when searching through the category)
# def artsCategory():
#     if request.form == 'GET':
#         artCategory = db.child("Bame_Business").child("business").child("arts_Media_Tech").get()
#         artCat = [x.val() for x in artCategory.each()]
#         art_category = len(artCat)
#         art_category = range(art_category)
#         return render_template('arts.html', art_category=art_category, artCat=artCat)

if __name__ == '__main__':
    app.run(debug=True)
