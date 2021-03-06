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
    return render_template("home.html")

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
        return render_template('searchDirectory.html')
    else:
        selectCategory = request.form.get("selectCategory")
        search = request.form.get("search")
        err = "Sorry, couldn't find what you were looking for. Please try again or scroll through the directory to find what you are looking for."
        if selectCategory == "arts":
            artCategory = db.child("Bame_Business").child("business").child("arts_Media_Tech").get()
            artCat = [x.val() for x in artCategory.each()]
            art_category = len(artCat)
            art_category = range(art_category)
            search = search.split(", ")
            s = len(search)
            s = range(s)
            for x in s:
                for y in art_category:
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

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        email = request.form.get("email")
        confirmEmail = request.form.get("confirmEmail")
        password = request.form.get("pass")
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        businessName = request.form.get("businessName")
        startYear = request.form.get("startYear")
        selectCategory = request.form.get("selectCategory")
        businessDescription = request.form.get("businessDescription")
        keyWords = request.form.get("keyWords")
        businessEmail = request.form.get("businessEmail")
        businessNumber = request.form.get("businessNumber")
        businessAddress = request.form.get("businessAddress")
        businessTown = request.form.get("businessTown")
        businessCity = request.form.get("businessCity")
        businessPostcode = request.form.get("businessPostcode")
        web = request.form.get("web")
        insta = request.form.get("insta")
        tweet = request.form.get("tweet")
        bameRegister = dict(
            firstName = firstName,
            lastName = lastName,
            confirmEmail = confirmEmail,
            businessName = businessName,
            businessStartYear = startYear,
            businessCategory = selectCategory,
            businessDescription = businessDescription,
            keyWords = keyWords,
            businessEmail = businessEmail,
            businessNumber = businessNumber,
            businessAddress = [businessAddress, businessTown, businessCity, businessPostcode],
            businessURL = web,
            Instagram = insta,
            Twitter = tweet,
        )
        if selectCategory == "arts":
            # # pswrd = password
            # # if len(str(pswrd)) <= 5:
            # if not password:
            #     err = "Please provde a valid password. Your password must contain at LEAST 6 characters."
            #     return render_template('home.html', passwordERROR=err)
            # else:
            keyWords = keyWords.split(", ")
            keyWords = len(keyWords)
            if keyWords <= 14:
                err = "Please provide 15 or more keywords for your business"
                return render_template('home.html', err=err)
            elif keyWords >= 15:
                try:
                    user = auth.create_user_with_email_and_password(email, password)
                    auth.send_email_verification(user['idToken'])
                    user = auth.refresh(user['refreshToken'])
                    db.child("Bame_Business").child("business").child("arts_Media_Tech").push(bameRegister, user['idToken'])
                    signed_in_user = auth.get_account_info(user['idToken'])

                    artCategory = db.child("Bame_Business").child("business").child("arts_Media_Tech").get(user['idToken'])
                    artCat = [x.val() for x in artCategory.each()]
                    if signed_in_user['users'][0]['email'] == artCat[0]['confirmEmail']:
                        return render_template(
                        'arts.html',
                        business = artCat[0]['businessName'],
                        founder = artCat[0]['firstName'],
                        surname = artCat[0]['lastName'],
                        year = artCat[0]['businessStartYear'],
                        category = artCat[0]['businessCategory'],
                        description = artCat[0]['businessDescription'],
                        address = artCat[0]['businessAddress'],
                        email = artCat[0]['businessEmail'], # brings up keyError if nothing entered
                        phone = artCat[0]['businessNumber'],
                        web = artCat[0]['businessURL'],
                        tweet = artCat[0]['Twitter'],
                        insta = artCat[0]['Instagram'])
                except:
                    err = "Something went wrong, your registration was not complete."
                    return render_template('home.html', err=err)
        if selectCategory == "charity":
            keyWords = keyWords.split(", ")
            keyWords = len(keyWords)
            if keyWords <= 14:
                err = "Please provide 15 or more keywords for your business"
                return render_template('home.html', err=err)
            elif keyWords >= 15:
                try:
                    user = auth.create_user_with_email_and_password(email, password)
                    auth.send_email_verification(user['idToken'])
                    user = auth.refresh(user['refreshToken'])
                    db.child("Bame_Business").child("business").child("charities_SupportGroups").push(bameRegister, user['idToken'])
                    signed_in_user = auth.get_account_info(user['idToken'])

                    charityCategory = db.child("Bame_Business").child("business").child("charities_SupportGroups").get(user['idToken'])
                    charityCat = [x.val() for x in charityCategory.each()]
                    if signed_in_user['users'][0]['email'] == charityCat[0]['confirmEmail']:
                        return render_template(
                        'charity.html',
                        business = charityCat[0]['businessName'],
                        founder = charityCat[0]['firstName'],
                        surname = charityCat[0]['lastName'],
                        year = charityCat[0]['businessStartYear'],
                        category = charityCat[0]['businessCategory'],
                        description = charityCat[0]['businessDescription'],
                        address = charityCat[0]['businessAddress'],
                        email = charityCat[0]['businessEmail'],
                        phone = charityCat[0]['businessNumber'],
                        web = charityCat[0]['businessURL'],
                        tweet = charityCat[0]['Twitter'],
                        insta = charityCat[0]['Instagram'])
                except:
                    err = "Something went wrong, your registration was not complete."
                    return render_template('home.html', err=err)

        elif selectCategory == "foods":
            keyWords = keyWords.split(", ")
            keyWords = len(keyWords)
            if keyWords <= 14:
                err = "Please provide 15 or more keywords for your business"
                return render_template('home.html', err=err)
            elif keyWords >= 15:
                try:
                    user = auth.create_user_with_email_and_password(email, password)
                    auth.send_email_verification(user['idToken'])
                    user = auth.refresh(user['refreshToken'])
                    db.child("Bame_Business").child("business").child("foods_Restaurants_Takeaways").push(bameRegister, user['idToken'])
                    signed_in_user = auth.get_account_info(user['idToken'])

                    foodCategory = db.child("Bame_Business").child("business").child("foods_Restaurants_Takeaways").get(user['idToken'])
                    foodCat = [x.val() for x in foodCategory.each()]
                    if signed_in_user['users'][0]['email'] == foodCat[0]['confirmEmail']:
                        return render_template(
                        'food.html',
                        business = foodCat[0]['businessName'],
                        founder = foodCat[0]['firstName'],
                        surname = foodCat[0]['lastName'],
                        year = foodCat[0]['businessStartYear'],
                        category = foodCat[0]['businessCategory'],
                        description = foodCat[0]['businessDescription'],
                        address = foodCat[0]['businessAddress'],
                        email = foodCat[0]['businessEmail'],
                        phone = foodCat[0]['businessNumber'],
                        web = foodCat[0]['businessURL'],
                        tweet = foodCat[0]['Twitter'],
                        insta = foodCat[0]['Instagram'])
                except:
                    err = "Something went wrong, your registration was not complete."
                    return render_template('home.html', err=err)
        elif selectCategory == "health":
            keyWords = keyWords.split(", ")
            keyWords = len(keyWords)
            if keyWords <= 14:
                err = "Please provide 15 or more keywords for your business"
                return render_template('home.html', err=err)
            elif keyWords >= 15:
                try:
                    user = auth.create_user_with_email_and_password(email, password)
                    auth.send_email_verification(user['idToken'])
                    user = auth.refresh(user['refreshToken'])
                    db.child("Bame_Business").child("business").child("health_Lifestyle_Sports").push(bameRegister, user['idToken'])
                    signed_in_user = auth.get_account_info(user['idToken'])

                    healthCategory = db.child("Bame_Business").child("business").child("health_Lifestyle_Sports").get(user['idToken'])
                    healthCat = [x.val() for x in healthCategory.each()]
                    if signed_in_user['users'][0]['email'] == healthCat[0]['confirmEmail']:
                        return render_template(
                        'health.html',
                        business = healthCat[0]['businessName'],
                        founder = healthCat[0]['firstName'],
                        surname = healthCat[0]['lastName'],
                        year = healthCat[0]['businessStartYear'],
                        category = healthCat[0]['businessCategory'],
                        description = healthCat[0]['businessDescription'],
                        address = healthCat[0]['businessAddress'],
                        email = healthCat[0]['businessEmail'],
                        phone = healthCat[0]['businessNumber'],
                        web = healthCat[0]['businessURL'],
                        tweet = healthCat[0]['Twitter'],
                        insta = healthCat[0]['Instagram'])
                except:
                    err = "Something went wrong, your registration was not complete."
                    return render_template('home.html', err=err)
        elif selectCategory == "house":
            keyWords = keyWords.split(", ")
            keyWords = len(keyWords)
            if keyWords <= 14:
                err = "Please provide 15 or more keywords for your business"
                return render_template('home.html', err=err)
            elif keyWords >= 15:
                try:
                    user = auth.create_user_with_email_and_password(email, password)
                    auth.send_email_verification(user['idToken'])
                    user = auth.refresh(user['refreshToken'])
                    db.child("Bame_Business").child("business").child("housing_Property_ConstructionServices").push(bameRegister, user['idToken'])
                    signed_in_user = auth.get_account_info(user['idToken'])

                    houseCategory = db.child("Bame_Business").child("business").child("housing_Property_ConstructionServices").get(user['idToken'])
                    houseCat = [x.val() for x in houseCategory.each()]
                    if signed_in_user['users'][0]['email'] == houseCat[0]['confirmEmail']:
                        return render_template(
                        'house.html',
                        business = houseCat[0]['businessName'],
                        founder = houseCat[0]['firstName'],
                        surname = houseCat[0]['lastName'],
                        year = houseCat[0]['businessStartYear'],
                        category = houseCat[0]['businessCategory'],
                        description = houseCat[0]['businessDescription'],
                        address = houseCat[0]['businessAddress'],
                        email = houseCat[0]['businessEmail'],
                        phone = houseCat[0]['businessNumber'],
                        web = houseCat[0]['businessURL'],
                        tweet = houseCat[0]['Twitter'],
                        insta = houseCat[0]['Instagram'])
                except:
                    err = "Something went wrong, your registration was not complete."
                    return render_template('home.html', err=err)
        elif selectCategory == "legal":
            keyWords = keyWords.split(", ")
            keyWords = len(keyWords)
            if keyWords <= 14:
                err = "Please provide 15 or more keywords for your business"
                return render_template('home.html', err=err)
            elif keyWords >= 15:
                try:
                    user = auth.create_user_with_email_and_password(email, password)
                    auth.send_email_verification(user['idToken'])
                    user = auth.refresh(user['refreshToken'])
                    db.child("Bame_Business").child("business").child("legal_Financial").push(bameRegister, user['idToken'])
                    signed_in_user = auth.get_account_info(user['idToken'])

                    legalCategory = db.child("Bame_Business").child("business").child("legal_Financial").get(user['idToken'])
                    legalCat = [x.val() for x in legalCategory.each()]
                    if signed_in_user['users'][0]['email'] == legalCat[0]['confirmEmail']:
                        return render_template(
                        'legal.html',
                        business = legalCat[0]['businessName'],
                        founder = legalCat[0]['firstName'],
                        surname = legalCat[0]['lastName'],
                        year = legalCat[0]['businessStartYear'],
                        category = legalCat[0]['businessCategory'],
                        description = legalCat[0]['businessDescription'],
                        address = legalCat[0]['businessAddress'],
                        email = legalCat[0]['businessEmail'],
                        phone = legalCat[0]['businessNumber'],
                        web = legalCat[0]['businessURL'],
                        tweet = legalCat[0]['Twitter'],
                        insta = legalCat[0]['Instagram'])
                except:
                    err = "Something went wrong, your registration was not complete."
                    return render_template('home.html', err=err)
        elif selectCategory == "retail":
            keyWords = keyWords.split(", ")
            keyWords = len(keyWords)
            if keyWords <= 14:
                err = "Please provide 15 or more keywords for your business"
                return render_template('home.html', err=err)
            elif keyWords >= 15:
                try:
                    user = auth.create_user_with_email_and_password(email, password)
                    auth.send_email_verification(user['idToken'])
                    user = auth.refresh(user['refreshToken'])
                    db.child("Bame_Business").child("business").child("retail_Fashion_Jewellery").push(bameRegister, user['idToken'])
                    signed_in_user = auth.get_account_info(user['idToken'])

                    retailCategory = db.child("Bame_Business").child("business").child("retail_Fashion_Jewellery").get(user['idToken'])
                    retailCat = [x.val() for x in retailCategory.each()]
                    if signed_in_user['users'][0]['email'] == retailCat[0]['confirmEmail']:
                        return render_template(
                        'retail.html',
                        business = retailCat[0]['businessName'],
                        founder = retailCat[0]['firstName'],
                        surname = retailCat[0]['lastName'],
                        year = retailCat[0]['businessStartYear'],
                        category = retailCat[0]['businessCategory'],
                        description = retailCat[0]['businessDescription'],
                        address = retailCat[0]['businessAddress'],
                        email = retailCat[0]['businessEmail'],
                        phone = retailCat[0]['businessNumber'],
                        web = retailCat[0]['businessURL'],
                        tweet = retailCat[0]['Twitter'],
                        insta = retailCat[0]['Instagram'])
                except:
                    err = "Something went wrong, your registration was not complete."
                    return render_template('home.html', err=err)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        email = request.form.get("login")
        password = request.form.get("pass")

        user = auth.sign_in_with_email_and_password(email, password)
        user = auth.refresh(user['refreshToken'])
        signed_in_user = auth.get_account_info(user['idToken'])

        artCategory = db.child("Bame_Business").child("business").child("arts_Media_Tech").get(user['idToken'])
        foodCategory = db.child("Bame_Business").child("business").child("foods_Restaurants_Takeaways").get(user['idToken'])
        healthCategory = db.child("Bame_Business").child("business").child("health_Lifestyle_Sports").get(user['idToken'])
        housingCategory = db.child("Bame_Business").child("business").child("housing_Property_ConstructionServices").get(user['idToken'])
        retailCategory = db.child("Bame_Business").child("business").child("retail_Fashion_Jewellery").get(user['idToken'])
        charityCategory = db.child("Bame_Business").child("business").child("charities_SupportGroups").get(user['idToken'])
        legalCategory = db.child("Bame_Business").child("business").child("legal_Financial").get(user['idToken'])

        if artCategory:
            artCat = [x.val() for x in artCategory.each()]
            art_category = len(artCat)
            art_category = range(art_category)
            for x in art_category:
                # return render_template('profile.html', artCategory=artCategory, artCat=artCat[0])
                return render_template(
                'profile.html',
                business = artCat[0]['businessName'],
                founder = artCat[0]['firstName'],
                surname = artCat[0]['lastName'],
                year = artCat[0]['businessStartYear'],
                category = artCat[0]['businessCategory'],
                description = artCat[0]['businessDescription'],
                address = artCat[0]['businessAddress'],
                email = artCat[0]['businessEmail'], # brings up keyError if nothing entered
                phone = artCat[0]['businessNumber'],
                web = artCat[0]['businessURL'],
                tweet = artCat[0]['Twitter'],
                insta = artCat[0]['Instagram'],
                artCategory = art_category, artCat=artCat)

@app.route('/addNewBusiness', methods=['GET', 'POST'])
def addNewBusiness():
    return render_template('profile.html')

@app.route('/businessList', methods=['GET', 'POST'])
def businessList():
    if request.method == 'GET':
        email = request.form.get("login")
        password = request.form.get("pass")
        artCategory = db.child("Bame_Business").child("business").child("arts_Media_Tech").get(user['idToken'])
        art_category = len(artCat)
        art_category = range(art_category)
        for x in art_category:
            return render_template(
            'profile.html',
            business = artCat[0]['businessName'],
            founder = artCat[0]['firstName'],
            surname = artCat[0]['lastName'],
            year = artCat[0]['businessStartYear'],
            category = artCat[0]['businessCategory'],
            description = artCat[0]['businessDescription'],
            address = artCat[0]['businessAddress'],
            email = artCat[0]['businessEmail'], # brings up keyError if nothing entered
            phone = artCat[0]['businessNumber'],
            web = artCat[0]['businessURL'],
            tweet = artCat[0]['Twitter'],
            insta = artCat[0]['Instagram'],
            artCategory = art_category, artCat=artCat)

if __name__ == '__main__':
    app.run(debug=True)
