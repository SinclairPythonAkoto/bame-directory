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
        err = "Sorry, couldn't find what you were looking for. Please try again or scroll through the directory to find what you are looking for."
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
                        return render_template('arts.html', err=err, art_category=art_category, artCat=artCat)
        elif selectCategory == "charity":
            charityCategory = db.child("Bame_Business").child("business").child("charities_SupportGroups").get()
            charityCat = [x.val() for x in charityCategory.each()]
            charity_category = len(charityCat)
            charity_category = range(charity_category)
            search = search.split(", ")
            s = len(search)
            s = range(s)
            for x in s:
                for y in charity_category:
                    if search[x] in charityCat[y]['keyWords']:
                        return render_template(
                        'charity.html',
                        business=charityCat[y]['businessName'],
                        founder=charityCat[y]['userName'],
                        year=charityCat[y]['businessStartYear'],
                        category=charityCat[y]['businessCategory'],
                        description=charityCat[y]['businessDescription'],
                        address=charityCat[y]['businessAddress'],
                        email=charityCat[y]['businessEmail'],
                        phone=charityCat[y]['businessNumber'],
                        web=charityCat[y]['businessURL'],
                        tweet=charityCat[y]['Twitter'],
                        insta=charityCat[y]['Instagram'],
                        charity_category=charity_category, charityCat=charityCat)
                    else:
                        return render_template('charity.html', err=err, charity_category=charity_category, charityCat=charityCat)
        elif selectCategory == "foods":
            foodCategory = db.child("Bame_Business").child("business").child("foods_Restaurants_Takeaways").get()
            foodCat = [x.val() for x in foodCategory.each()]
            food_category = len(foodCat)
            food_category = range(food_category)
            search = search.split(", ")
            s = len(search)
            s = range(s)
            for x in s:
                for y in food_category:
                    if search[x] in foodCat[y]['keyWords']:
                        return render_template(
                        'food.html',
                        business=foodCat[y]['businessName'],
                        founder=foodCat[y]['userName'],
                        year=foodCat[y]['businessStartYear'],
                        category=foodCat[y]['businessCategory'],
                        description=foodCat[y]['businessDescription'],
                        address=foodCat[y]['businessAddress'],
                        email=foodCat[y]['businessEmail'],
                        phone=foodCat[y]['businessNumber'],
                        web=foodCat[y]['businessURL'],
                        tweet=foodCat[y]['Twitter'],
                        insta=foodCat[y]['Instagram'],
                        food_category=food_category, foodCat=foodCat)
                    else:
                        return render_template('food.html', err=err, food_category=food_category, foodCat=foodCat)
        elif selectCategory == "health":
            healthCategory = db.child("Bame_Business").child("business").child("health_Lifestyle_Sports").get()
            healthCat = [x.val() for x in healthCategory.each()]
            health_category = len(healthCat)
            health_category = range(health_category)
            search = search.split(", ")
            s = len(search)
            s = range(s)
            for x in s:
                for y in health_category:
                    if search[x] in healthCat[y]['keyWords']:
                        return render_template(
                        'health.html',
                        business=healthCat[y]['businessName'],
                        founder=healthCat[y]['userName'],
                        year=healthCat[y]['businessStartYear'],
                        category=healthCat[y]['businessCategory'],
                        description=healthCat[y]['businessDescription'],
                        address=healthCat[y]['businessAddress'],
                        email=healthCat[y]['businessEmail'],
                        phone=healthCat[y]['businessNumber'],
                        web=healthCat[y]['businessURL'],
                        tweet=healthCat[y]['Twitter'],
                        insta=healthCat[y]['Instagram'],
                        health_category=health_category, healthCat=healthCat)
                    else:
                        return render_template('health.html', err=err, health_category=health_category, healthCat=healthCat)
        elif selectCategory == "house":
            houseCategory = db.child("Bame_Business").child("business").child("housing_Property_ConstructionServices").get()
            houseCat = [x.val() for x in houseCategory.each()]
            house_category = len(houseCat)
            house_category = range(house_category)
            search = search.split(", ")
            s = len(search)
            s = range(s)
            for x in s:
                for y in house_category:
                    if search[x] in houseCat[y]['keyWords']:
                        return render_template(
                        'house.html',
                        business=houseCat[y]['businessName'],
                        founder=houseCat[y]['userName'],
                        year=houseCat[y]['businessStartYear'],
                        category=houseCat[y]['businessCategory'],
                        description=houseCat[y]['businessDescription'],
                        address=houseCat[y]['businessAddress'],
                        email=houseCat[y]['businessEmail'],
                        phone=houseCat[y]['businessNumber'],
                        web=houseCat[y]['businessURL'],
                        tweet=houseCat[y]['Twitter'],
                        insta=houseCat[y]['Instagram'],
                        house_category=house_category, houseCat=houseCat)
                    else:
                        return render_template('house.html', err=err, house_category=house_category, houseCat=houseCat)
        elif selectCategory == "legal":
            legalCategory = db.child("Bame_Business").child("business").child("legal_Financial").get()
            legalCat = [x.val() for x in legalCategory.each()]
            legal_category = len(legalCat)
            legal_category = range(legal_category)
            search = search.split(", ")
            s = len(search)
            s = range(s)
            for x in s:
                for y in legal_category:
                    if search[x] in legalCat[y]['keyWords']:
                        return render_template(
                        'legal.html',
                        business=legalCat[y]['businessName'],
                        founder=legalCat[y]['userName'],
                        year=legalCat[y]['businessStartYear'],
                        category=legalCat[y]['businessCategory'],
                        description=legalCat[y]['businessDescription'],
                        address=legalCat[y]['businessAddress'],
                        email=legalCat[y]['businessEmail'],
                        phone=legalCat[y]['businessNumber'],
                        web=legalCat[y]['businessURL'],
                        tweet=legalCat[y]['Twitter'],
                        insta=legalCat[y]['Instagram'],
                        legal_category=legal_category, legalCat=legalCat)
                    else:
                        return render_template('legal.html', err=err, legal_category=legal_category, legalCat=legalCat)
        elif selectCategory == "retail":
            retailCategory = db.child("Bame_Business").child("business").child("retail_Fashion_Jewellery").get()
            retailCat = [x.val() for x in retailCategory.each()]
            retail_category = len(retailCat)
            retail_category = range(retail_category)
            search = search.split(", ")
            s = len(search)
            s = range(s)
            for x in s:
                for y in retail_category:
                    if search[x] in retailCat[y]['keyWords']:
                        return render_template(
                        'retail.html',
                        business=retailCat[y]['businessName'],
                        founder=retailCat[y]['userName'],
                        year=retailCat[y]['businessStartYear'],
                        category=retailCat[y]['businessCategory'],
                        description=retailCat[y]['businessDescription'],
                        address=retailCat[y]['businessAddress'],
                        email=retailCat[y]['businessEmail'],
                        phone=retailCat[y]['businessNumber'],
                        web=retailCat[y]['businessURL'],
                        tweet=retailCat[y]['Twitter'],
                        insta=retailCat[y]['Instagram'],
                        retail_category=retail_category, retailCat=retailCat)
                    else:
                        return render_template('retail.html', err=err, retail_category=retail_category, retailCat=retailCat)

@app.route("/Arts-Media-Tech")
# this will take you to arts category html page
def artsCategory():
    artCategory = db.child("Bame_Business").child("business").child("arts_Media_Tech").get()
    artCat = [x.val() for x in artCategory.each()]
    art_category = len(artCat)
    art_category = range(art_category)
    return render_template('arts.html', art_category=art_category, artCat=artCat)

@app.route("/Charities-SupportGroups")
def charityCategory():
    charityCategory = db.child("Bame_Business").child("business").child("charities_SupportGroups").get()
    charityCat = [x.val() for x in charityCategory.each()]
    charity_category = len(charityCat)
    charity_category = range(charity_category)
    return render_template('charity.html', charity_category=charity_category, charityCat=charityCat)

@app.route("/Foods-Restaurants-Takeaways")
def foodCategory():
    foodCategory = db.child("Bame_Business").child("business").child("foods_Restaurants_Takeaways").get()
    foodCat = [x.val() for x in foodCategory.each()]
    food_category = len(foodCat)
    food_category = range(food_category)
    return render_template('food.html', food_category=food_category, foodCat=foodCat)

@app.route("/Health-Lifestyle-Sports")
def healthCategory():
    healthCategory = db.child("Bame_Business").child("business").child("health_Lifestyle_Sports").get()
    healthCat = [x.val() for x in healthCategory.each()]
    health_category = len(healthCat)
    health_category = range(health_category)
    return render_template('health.html', health_category=health_category, healthCat=healthCat)

@app.route("/Housing-Property-ConstructionServices")
def houseCategory():
    houseCategory = db.child("Bame_Business").child("business").child("housing_Property_ConstructionServices").get()
    houseCat = [x.val() for x in houseCategory.each()]
    house_category = len(houseCat)
    house_category = range(house_category)
    return render_template('house.html', house_category=house_category, houseCat=houseCat)

@app.route("/Legal-Financial")
def legalCategory():
    legalCategory = db.child("Bame_Business").child("business").child("legal_Financial").get()
    legalCat = [x.val() for x in legalCategory.each()]
    legal_category = len(legalCat)
    legal_category = range(legal_category)
    return render_template('legal.html', legal_category=legal_category, legalCat=legalCat)

@app.route("/Retail-Fashion-Jewellery-Beauty&Cosmetics")
def retailCategory():
    retailCategory = db.child("Bame_Business").child("business").child("retail_Fashion_Jewellery").get()
    retailCat = [x.val() for x in retailCategory.each()]
    retail_category = len(retailCat)
    retail_category = range(retail_category)
    return render_template('retail.html', retail_category=retail_category, retailCat=retailCat)
#
@app.route("/searchDeirectory", methods=['GET', 'POST'])
def searchDirectory():
    if request.method == 'GET':
        # now duplicate the same function as the search route
        return render_template('searchDirectory.html')

if __name__ == '__main__':
    app.run(debug=True)
