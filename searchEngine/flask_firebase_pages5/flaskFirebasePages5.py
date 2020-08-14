import pyrebase
from flask import *
from searchEngine import *
# from functools import wraps
from random import randint

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
    return render_template('new.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        selectCategory = request.form.get("selectCategory")
        search = request.form.get("search")
        search_btn = request.form.get("search_btn")
        search_all = request.form.get("search_all")

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
                # if the seach keyword matches with the entry keyword then release data
                    if search[x] in artCat[y]['keyWords']:
                        return render_template(
                        'new.html',
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
                        insta=artCat[y]['Instagram'])
    
        return "sorry couldn't find what you were looking for!"

    else:
        pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    unsuccessful = 'Please check your credentials'
    successful = 'Login successful'
    if request.method == 'POST':
        email = request.form.get('name')
        password = request.form.get('pass')
        # try:
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
            num = len(artCat)
            artCat = artCat[num - 1]

            if email == artCat['confirmationEmail']:
                business = artCat['businessName']
                founder = artCat['userName']
                year = artCat['businessStartYear']
                category = artCat['businessCategory']
                description = artCat['businessDescription']
                address = artCat['businessAddress']
                email = artCat['businessEmail']
                phone = artCat['businessNumber']
                web = artCat['businessURL']
                tweet = artCat['Twitter']
                insta = artCat['Instagram']
                return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
            elif foodCategory:
                foodCat = [x.val() for x in foodCategory.each()]
                num = len(foodCat)
                foodCat = foodCat[num - 1]
                if email == foodCat['confirmationEmail']:
                    business = foodCat['businessName']
                    founder = foodCat['userName']
                    year = foodCat['businessStartYear']
                    category = foodCat['businessCategory']
                    description = foodCat['businessDescription']
                    address = foodCat['businessAddress']
                    email = foodCat['businessEmail']
                    phone = foodCat['businessNumber']
                    web = foodCat['businessURL']
                    tweet = foodCat['Twitter']
                    insta = foodCat['Instagram']
                    return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
                elif charityCategory:
                    charityCat = [x.val() for x in charityCategory.each()]
                    num = len(charityCat)
                    charityCat = charityCat[num - 1]
                    if email == charityCat['confirmationEmail']:
                        business = charityCat['businessName']
                        founder = charityCat['userName']
                        year = charityCat['businessStartYear']
                        category = charityCat['businessCategory']
                        description = charityCat['businessDescription']
                        address = charityCat['businessAddress']
                        email = charityCat['businessEmail']
                        phone = charityCat['businessNumber']
                        web = charityCat['businessURL']
                        tweet = charityCat['Twitter']
                        insta = charityCat['Instagram']
                        return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
                    elif healthCategory:
                        healthCat = [x.val() for x in healthCategory.each()]
                        num = len(healthCat)
                        healthCat = healthCat[num - 1]
                        if email == healthCat['confirmationEmail']:
                            business = healthCat['businessName']
                            founder = healthCat['userName']
                            year = healthCat['businessStartYear']
                            category = healthCat['businessCategory']
                            description = healthCat['businessDescription']
                            address = healthCat['businessAddress']
                            email = healthCat['businessEmail']
                            phone = healthCat['businessNumber']
                            web = healthCat['businessURL']
                            tweet = healthCat['Twitter']
                            insta = healthCat['Instagram']
                            return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
                        elif housingCategory:
                            houseCat = [x.val() for x in housingCategory.each()]
                            num = len(houseCat)
                            houseCat = houseCat[num - 1]
                            if email == houseCat['confirmationEmail']:
                                business = houseCat['businessName']
                                founder = houseCat['userName']
                                year = houseCat['businessStartYear']
                                category = houseCat['businessCategory']
                                description = houseCat['businessDescription']
                                address = houseCat['businessAddress']
                                email = houseCat['businessEmail']
                                phone = houseCat['businessNumber']
                                web = houseCat['businessURL']
                                tweet = houseCat['Twitter']
                                insta = houseCat['Instagram']
                                return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
                            elif retailCategory:
                                retailCat = [x.val() for x in retailCategory.each()]
                                num = len(retailCat)
                                retailCat = retailCat[num - 1]
                                if email == retailCat['confirmationEmail']:
                                    business = retailCat['businessName']
                                    founder = retailCat['userName']
                                    year = retailCat['businessStartYear']
                                    category = retailCat['businessCategory']
                                    description = retailCat['businessDescription']
                                    address = retailCat['businessAddress']
                                    email = retailCat['businessEmail']
                                    phone = retailCat['businessNumber']
                                    web = retailCat['businessURL']
                                    tweet = retailCat['Twitter']
                                    insta = retailCat['Instagram']
                                    return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
                                elif legalCategory:
                                    legalCat = [x.val() for x in legalCategory.each()]
                                    num = len(legalCat)
                                    legalCat = legalCat[num - 1]
                                    if email == legalCat['confirmationEmail']:
                                        business = legalCat['businessName']
                                        founder = legalCat['userName']
                                        year = legalCat['businessStartYear']
                                        category = legalCat['businessCategory']
                                        description = legalCat['businessDescription']
                                        address = legalCat['businessAddress']
                                        email = legalCat['businessEmail']
                                        phone = legalCat['businessNumber']
                                        web = legalCat['businessURL']
                                        tweet = legalCat['Twitter']
                                        insta = legalCat['Instagram']
                                        return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)

        #     return render_template('new.html', us=unsuccessful)

    return render_template('new.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        confirmEmail = request.form.get('confirmEmail')
        password = request.form.get('pass')
        userName = request.form.get('inputName')
        businessName = request.form.get('businessName')
        startYear = request.form.get('startYear')
        selectCategory = request.form.get('selectCategory')
        businessDescription = request.form.get('businessDescription')
        keyWords = request.form.get('keyWords')
        web = request.form.get('web')
        insta = request.form.get('insta')
        tweet = request.form.get('tweet')
        businessNumber = request.form.get('businessNumber')
        businessAddress = request.form.get('businessAddress')
        businessTown = request.form.get('businessTown')
        businessCity = request.form.get('businessCity')
        businessPostcode = request.form.get('businessPostcode')
        businessEmail = request.form.get('businessEmail')
        bameRegister = dict(
            userName = userName,
            confirmationEmail = confirmEmail,
            businessName = businessName,
            businessStartYear = startYear,
            businessCategory = selectCategory,
            businessDescription = businessDescription,
            keyWords = keyWords,
            businessURL = web,
            Instagram = insta,
            Twitter = tweet,
            businessNumber = businessNumber,
            businessAddress = [businessAddress, businessTown, businessCity, businessPostcode],
            businessEmail = businessEmail,
        )
        if selectCategory == "arts":
            try:
                user = auth.create_user_with_email_and_password(email, password)
                auth.send_email_verification(user['idToken'])
                user = auth.refresh(user['refreshToken'])
                db.child("Bame_Business").child("business").child("arts_Media_Tech").push(bameRegister, user['idToken'])
                signed_in_user = auth.get_account_info(user['idToken'])

                artCategory = db.child("Bame_Business").child("business").child("arts_Media_Tech").get(user['idToken'])
                artCat = [x.val() for x in artCategory.each()]
                num = len(artCat)
                artCat = artCat[num - 1]
                if signed_in_user['users'][0]['email'] == artCat['confirmationEmail']:
                    business = artCat['businessName']
                    founder = artCat['userName']
                    year = artCat['businessStartYear']
                    category = artCat['businessCategory']
                    description = artCat['businessDescription']
                    address = artCat['businessAddress']
                    email = artCat['businessEmail']
                    phone = artCat['businessNumber']
                    web = artCat['businessURL']
                    tweet = artCat['Twitter']
                    insta = artCat['Instagram']
                    return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
            except:
                return render_template('new.html')
        elif selectCategory == "foods":
            try:
                user = auth.create_user_with_email_and_password(email, password)
                auth.send_email_verification(user['idToken'])
                user = auth.refresh(user['refreshToken'])
                db.child("Bame_Business").child("business").child("foods_Restaurants_Takeaways").push(bameRegister, user['idToken'])
                signed_in_user = auth.get_account_info(user['idToken'])

                foodCategory = db.child("Bame_Business").child("business").child("foods_Restaurants_Takeaways").get(user['idToken'])
                foodCat = [x.val() for x in foodCategory.each()]
                num = len(foodCat)
                foodCat = foodCat[num - 1]
                if signed_in_user['users'][0]['email'] == foodCat['confirmationEmail']:
                    business = foodCat['businessName']
                    founder = foodCat['userName']
                    year = foodCat['businessStartYear']
                    category = foodCat['businessCategory']
                    description = foodCat['businessDescription']
                    address = foodCat['businessAddress']
                    email = foodCat['businessEmail']
                    phone = foodCat['businessNumber']
                    web = foodCat['businessURL']
                    tweet = foodCat['Twitter']
                    insta = foodCat['Instagram']
                    return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
            except:
                return render_template('new.html')
        elif selectCategory == "health":
            try:
                user = auth.create_user_with_email_and_password(email, password)
                auth.send_email_verification(user['idToken'])
                user = auth.refresh(user['refreshToken'])
                db.child("Bame_Business").child("business").child("health_Lifestyle_Sports").push(bameRegister, user['idToken'])
                signed_in_user = auth.get_account_info(user['idToken'])

                healthCategory = db.child("Bame_Business").child("business").child("health_Lifestyle_Sports").get(user['idToken'])
                healthCat = [x.val() for x in healthCategory.each()]
                num = len(healthCat)
                healthCat = healthCat[num - 1]
                if signed_in_user['users'][0]['email'] == healthCat['confirmationEmail']:
                    business = healthCat['businessName']
                    founder = healthCat['userName']
                    year = healthCat['businessStartYear']
                    category = healthCat['businessCategory']
                    description = healthCat['businessDescription']
                    address = healthCat['businessAddress']
                    email = healthCat['businessEmail']
                    phone = healthCat['businessNumber']
                    web = healthCat['businessURL']
                    tweet = healthCat['Twitter']
                    insta = healthCat['Instagram']
                    return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
            except:
                return render_template('new.html')
        elif selectCategory == "house":
            try:
                user = auth.create_user_with_email_and_password(email, password)
                auth.send_email_verification(user['idToken'])
                user = auth.refresh(user['refreshToken'])
                db.child("Bame_Business").child("business").child("housing_Property_ConstructionServices").push(bameRegister, user['idToken'])
                signed_in_user = auth.get_account_info(user['idToken'])

                housingCategory = db.child("Bame_Business").child("business").child("housing_Property_ConstructionServices").get(user['idToken'])
                houseCat = [x.val() for x in housingCategory.each()]
                num = len(houseCat)
                houseCat = houseCat[num - 1]
                if signed_in_user['users'][0]['email'] == houseCat['confirmationEmail']:
                    business = houseCat['businessName']
                    founder = houseCat['userName']
                    year = houseCat['businessStartYear']
                    category = houseCat['businessCategory']
                    description = houseCat['businessDescription']
                    address = houseCat['businessAddress']
                    email = houseCat['businessEmail']
                    phone = houseCat['businessNumber']
                    web = houseCat['businessURL']
                    tweet = houseCat['Twitter']
                    insta = houseCat['Instagram']
                    return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
            except:
                return render_template('new.html')
        elif selectCategory == "retail":
            try:
                user = auth.create_user_with_email_and_password(email, password)
                auth.send_email_verification(user['idToken'])
                user = auth.refresh(user['refreshToken'])
                db.child("Bame_Business").child("business").child("retail_Fashion_Jewellery").push(bameRegister, user['idToken'])
                signed_in_user = auth.get_account_info(user['idToken'])

                retailCategory = db.child("Bame_Business").child("business").child("retail_Fashion_Jewellery").get(user['idToken'])
                retailCat = [x.val() for x in retailCategory.each()]
                num = len(retailCat)
                retailCat = retailCat[num - 1]
                if signed_in_user['users'][0]['email'] == retailCat['confirmationEmail']:
                    business = retailCat['businessName']
                    founder = retailCat['userName']
                    year = retailCat['businessStartYear']
                    category = retailCat['businessCategory']
                    description = retailCat['businessDescription']
                    address = retailCat['businessAddress']
                    email = retailCat['businessEmail']
                    phone = retailCat['businessNumber']
                    web = retailCat['businessURL']
                    tweet = retailCat['Twitter']
                    insta = retailCat['Instagram']
                    return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
            except:
                return render_template('new.html')
        elif selectCategory == "legal":
            try:
                user = auth.create_user_with_email_and_password(email, password)
                auth.send_email_verification(user['idToken'])
                user = auth.refresh(user['refreshToken'])
                db.child("Bame_Business").child("business").child("legal_Financial").push(bameRegister, user['idToken'])
                signed_in_user = auth.get_account_info(user['idToken'])

                legalCategory = db.child("Bame_Business").child("business").child("legal_Financial").get(user['idToken'])
                legalCat = [x.val() for x in legalCategory.each()]
                num = len(legalCat)
                legalCat = legalCat[num - 1]
                if signed_in_user['users'][0]['email'] == legalCat['confirmationEmail']:
                    business = legalCat['businessName']
                    founder = legalCat['userName']
                    year = legalCat['businessStartYear']
                    category = legalCat['businessCategory']
                    description = legalCat['businessDescription']
                    address = legalCat['businessAddress']
                    email = legalCat['businessEmail']
                    phone = legalCat['businessNumber']
                    web = legalCat['businessURL']
                    tweet = legalCat['Twitter']
                    insta = legalCat['Instagram']
                    return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
            except:
                return render_template('new.html')
        elif selectCategory == "charity":
            try:
                user = auth.create_user_with_email_and_password(email, password)
                auth.send_email_verification(user['idToken'])
                user = auth.refresh(user['refreshToken'])
                db.child("Bame_Business").child("business").child("charities_SupportGroups").push(bameRegister, user['idToken'])
                signed_in_user = auth.get_account_info(user['idToken'])

                charityCategory = db.child("Bame_Business").child("business").child("charities_SupportGroups").get(user['idToken'])
                charityCat = [x.val() for x in charityCategory.each()]
                num = len(charityCat)
                charityCat = charityCat[num - 1]
                if signed_in_user['users'][0]['email'] == charityCat['confirmationEmail']:
                    business = charityCat['businessName']
                    founder = charityCat['userName']
                    year = charityCat['businessStartYear']
                    category = charityCat['businessCategory']
                    description = charityCat['businessDescription']
                    address = charityCat['businessAddress']
                    email = charityCat['businessEmail']
                    phone = charityCat['businessNumber']
                    web = charityCat['businessURL']
                    tweet = charityCat['Twitter']
                    insta = charityCat['Instagram']
                    return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
            except:
                return render_template('new.html')
        #     try:
        #
        #     except:
                # return render_template('new.html')
    return render_template('new.html')


@app.route('/newBusiness', methods=['GET', 'POST'])
# @login_required
def newBusiness():
    if request.method == 'POST':
        email = request.form.get('email')
        confirmEmail = request.form.get('confirmEmail')
        password = request.form.get('pass')
        userName = request.form.get('inputName')
        businessName = request.form.get('businessName')
        startYear = request.form.get('startYear')
        selectCategory = request.form.get('selectCategory')
        businessDescription = request.form.get('businessDescription')
        keyWords = request.form.get('keyWords')
        web = request.form.get('web')
        insta = request.form.get('insta')
        tweet = request.form.get('tweet')
        businessNumber = request.form.get('businessNumber')
        businessAddress = request.form.get('businessAddress')
        businessTown = request.form.get('businessTown')
        businessCity = request.form.get('businessCity')
        businessPostcode = request.form.get('businessPostcode')
        businessEmail = request.form.get('businessEmail')
        bameRegister = dict(
            userName = userName,
            confirmationEmail = confirmEmail,
            businessName = businessName,
            businessStartYear = startYear,
            businessCategory = selectCategory,
            businessDescription = businessDescription,
            keyWords = keyWords,
            businessURL = web,
            Instagram = insta,
            Twitter = tweet,
            businessNumber = businessNumber,
            businessAddress = [businessAddress, businessTown, businessCity, businessPostcode],
            businessEmail = businessEmail,
        )
        if selectCategory == "arts":
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                user = auth.refresh(user['refreshToken'])
                db.child("Bame_Business").child("business").child("arts_Media_Tech").push(bameRegister, user['idToken'])
                signed_in_user = auth.get_account_info(user['idToken'])

                artCategory = db.child("Bame_Business").child("business").child("arts_Media_Tech").get(user['idToken'])
                artCat = [x.val() for x in artCategory.each()]
                num = len(artCat)
                artCat = artCat[num - 1]
                if signed_in_user['users'][0]['email'] == artCat['confirmationEmail']:
                    business = artCat['businessName']
                    founder = artCat['userName']
                    year = artCat['businessStartYear']
                    category = artCat['businessCategory']
                    description = artCat['businessDescription']
                    address = artCat['businessAddress']
                    email = artCat['businessEmail']
                    phone = artCat['businessNumber']
                    web = artCat['businessURL']
                    tweet = artCat['Twitter']
                    insta = artCat['Instagram']
                    return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
            except:
                return render_template('new.html')
        elif selectCategory == "foods":
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                user = auth.refresh(user['refreshToken'])
                db.child("Bame_Business").child("business").child("foods_Restaurants_Takeaways").push(bameRegister, user['idToken'])
                signed_in_user = auth.get_account_info(user['idToken'])

                foodCategory = db.child("Bame_Business").child("business").child("foods_Restaurants_Takeaways").get(user['idToken'])
                foodCat = [x.val() for x in foodCategory.each()]
                num = len(foodCat)
                foodCat = foodCat[num - 1]
                if signed_in_user['users'][0]['email'] == foodCat['confirmationEmail']:
                    business = foodCat['businessName']
                    founder = foodCat['userName']
                    year = foodCat['businessStartYear']
                    category = foodCat['businessCategory']
                    description = foodCat['businessDescription']
                    address = foodCat['businessAddress']
                    email = foodCat['businessEmail']
                    phone = foodCat['businessNumber']
                    web = foodCat['businessURL']
                    tweet = foodCat['Twitter']
                    insta = foodCat['Instagram']
                    return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
            except:
                return render_template('new.html')
        elif selectCategory == "health":
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                user = auth.refresh(user['refreshToken'])
                db.child("Bame_Business").child("business").child("health_Lifestyle_Sports").push(bameRegister, user['idToken'])
                signed_in_user = auth.get_account_info(user['idToken'])

                healthCategory = db.child("Bame_Business").child("business").child("foods_Restaurants_Takeaways").get(user['idToken'])
                healthCat = [x.val() for x in healthCategory.each()]
                num = len(healthCat)
                healthCat = healthCat[num - 1]
                if signed_in_user['users'][0]['email'] == healthCat['confirmationEmail']:
                    business = healthCat['businessName']
                    founder = healthCat['userName']
                    year = healthCat['businessStartYear']
                    category = healthCat['businessCategory']
                    description = healthCat['businessDescription']
                    address = healthCat['businessAddress']
                    email = healthCat['businessEmail']
                    phone = healthCat['businessNumber']
                    web = healthCat['businessURL']
                    tweet = healthCat['Twitter']
                    insta = healthCat['Instagram']
                    return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
            except:
                return render_template('new.html')
        elif selectCategory == "house":
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                user = auth.refresh(user['refreshToken'])
                db.child("Bame_Business").child("business").child("housing_Property_ConstructionServices").push(bameRegister, user['idToken'])
                signed_in_user = auth.get_account_info(user['idToken'])

                housingCategory = db.child("Bame_Business").child("business").child("housing_Property_ConstructionServices").get(user['idToken'])
                houseCat = [x.val() for x in housingCategory.each()]
                num = len(houseCat)
                houseCat = houseCat[num - 1]
                if signed_in_user['users'][0]['email'] == houseCat['confirmationEmail']:
                    business = houseCat['businessName']
                    founder = houseCat['userName']
                    year = houseCat['businessStartYear']
                    category = houseCat['businessCategory']
                    description = houseCat['businessDescription']
                    address = houseCat['businessAddress']
                    email = houseCat['businessEmail']
                    phone = houseCat['businessNumber']
                    web = houseCat['businessURL']
                    tweet = houseCat['Twitter']
                    insta = houseCat['Instagram']
                    return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
            except:
                return render_template('new.html')
        elif selectCategory == "legal":
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                user = auth.refresh(user['refreshToken'])
                db.child("Bame_Business").child("business").child("legal_Financial").push(bameRegister, user['idToken'])
                signed_in_user = auth.get_account_info(user['idToken'])

                legal_Financial = db.child("Bame_Business").child("business").child("legal_Financial").get(user['idToken'])
                legalCat = [x.val() for x in legalCategory.each()]
                num = len(legalCat)
                legalCat = legalCat[num - 1]
                if signed_in_user['users'][0]['email'] == legalCat['confirmationEmail']:
                    business = legalCat['businessName']
                    founder = legalCat['userName']
                    year = legalCat['businessStartYear']
                    category = legalCat['businessCategory']
                    description = legalCat['businessDescription']
                    address = legalCat['businessAddress']
                    email = legalCat['businessEmail']
                    phone = legalCat['businessNumber']
                    web = legalCat['businessURL']
                    tweet = legalCat['Twitter']
                    insta = legalCat['Instagram']
                    return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
            except:
                return render_template('new.html')
        elif selectCategory == "charity":
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                user = auth.refresh(user['refreshToken'])
                db.child("Bame_Business").child("business").child("charities_SupportGroups").push(bameRegister, user['idToken'])
                signed_in_user = auth.get_account_info(user['idToken'])

                charityCategory = db.child("Bame_Business").child("business").child("charities_SupportGroups").get(user['idToken'])
                charityCat = [x.val() for x in charityCategory.each()]
                num = len(charityCat)
                charityCat = charityCat[num - 1]
                if signed_in_user['users'][0]['email'] == charityCat['confirmationEmail']:
                    business = charityCat['businessName']
                    founder = charityCat['userName']
                    year = charityCat['businessStartYear']
                    category = charityCat['businessCategory']
                    description = charityCat['businessDescription']
                    address = charityCat['businessAddress']
                    email = charityCat['businessEmail']
                    phone = charityCat['businessNumber']
                    web = charityCat['businessURL']
                    tweet = charityCat['Twitter']
                    insta = charityCat['Instagram']
                    return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
            except:
                return render_template('new.html')
        elif selectCategory == "retail":
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                user = auth.refresh(user['refreshToken'])
                db.child("Bame_Business").child("business").child("charities_SupportGroups").push(bameRegister, user['idToken'])
                signed_in_user = auth.get_account_info(user['idToken'])

                charityCategory = db.child("Bame_Business").child("business").child("charities_SupportGroups").get(user['idToken'])
                charityCat = [x.val() for x in charityCategory.each()]
                num = len(charityCat)
                charityCat = charityCat[num - 1]
                if signed_in_user['users'][0]['email'] == charityCat['confirmationEmail']:
                    business = charityCat['businessName']
                    founder = charityCat['userName']
                    year = charityCat['businessStartYear']
                    category = charityCat['businessCategory']
                    description = charityCat['businessDescription']
                    address = charityCat['businessAddress']
                    email = charityCat['businessEmail']
                    phone = charityCat['businessNumber']
                    web = charityCat['businessURL']
                    tweet = charityCat['Twitter']
                    insta = charityCat['Instagram']
                    return render_template('profile.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
            except:
                return render_template('new.html')
    return render_template('newBusiness.html')

@app.route('/update', methods=['GET', 'POST'])
def update():
    # make a post request instead
    if request.method == 'POST':
        email = request.form.get('name')
        confirmEmail = request.form.get('confirmEmail')
        password = request.form.get('pass')
        try:
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
                num = len(artCat)
                artCat = artCat[num - 1]

                if email == artCat['confirmationEmail']:
                    business = artCat['businessName']
                    founder = artCat['userName']
                    year = artCat['businessStartYear']
                    category = artCat['businessCategory']
                    description = artCat['businessDescription']
                    address = artCat['businessAddress']
                    email = artCat['businessEmail']
                    phone = artCat['businessNumber']
                    web = artCat['businessURL']
                    tweet = artCat['Twitter']
                    insta = artCat['Instagram']
                    return render_template('update.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
                elif charityCategory:
                    charityCat = [x.val() for x in charityCategory.each()]
                    num = len(charityCat)
                    charityCat = charityCat[num - 1]
                    if email == charityCat['confirmationEmail']:
                        business = charityCat['businessName']
                        founder = charityCat['userName']
                        year = charityCat['businessStartYear']
                        category = charityCat['businessCategory']
                        description = charityCat['businessDescription']
                        address = charityCat['businessAddress']
                        email = charityCat['businessEmail']
                        phone = charityCat['businessNumber']
                        web = charityCat['businessURL']
                        tweet = charityCat['Twitter']
                        insta = charityCat['Instagram']
                        return render_template('update.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
                    elif healthCategory:
                        healthCat = [x.val() for x in healthCategory.each()]
                        num = len(healthCat)
                        healthCat = healthCat[num - 1]
                        if email == healthCat['confirmationEmail']:
                            business = healthCat['businessName']
                            founder = healthCat['userName']
                            year = healthCat['businessStartYear']
                            category = healthCat['businessCategory']
                            description = healthCat['businessDescription']
                            address = healthCat['businessAddress']
                            email = healthCat['businessEmail']
                            phone = healthCat['businessNumber']
                            web = healthCat['businessURL']
                            tweet = healthCat['Twitter']
                            insta = healthCat['Instagram']
                            return render_template('update.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
                        elif housingCategory:
                            houseCat = [x.val() for x in housingCategory.each()]
                            num = len(houseCat)
                            houseCat = houseCat[num - 1]
                            if email == houseCat['confirmationEmail']:
                                business = houseCat['businessName']
                                founder = houseCat['userName']
                                year = houseCat['businessStartYear']
                                category = houseCat['businessCategory']
                                description = houseCat['businessDescription']
                                address = houseCat['businessAddress']
                                email = houseCat['businessEmail']
                                phone = houseCat['businessNumber']
                                web = houseCat['businessURL']
                                tweet = houseCat['Twitter']
                                insta = houseCat['Instagram']
                                return render_template('update.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
                            elif retailCategory:
                                retailCat = [x.val() for x in retailCategory.each()]
                                num = len(retailCat)
                                retailCat = retailCat[num - 1]
                                if email == retailCat['confirmationEmail']:
                                    business = retailCat['businessName']
                                    founder = retailCat['userName']
                                    year = retailCat['businessStartYear']
                                    category = retailCat['businessCategory']
                                    description = retailCat['businessDescription']
                                    address = retailCat['businessAddress']
                                    email = retailCat['businessEmail']
                                    phone = retailCat['businessNumber']
                                    web = retailCat['businessURL']
                                    tweet = retailCat['Twitter']
                                    insta = retailCat['Instagram']
                                    return render_template('update.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
                                elif legalCategory:
                                    legalCat = [x.val() for x in legalCategory.each()]
                                    num = len(legalCat)
                                    legalCat = legalCat[num - 1]
                                    if email == legalCat['confirmationEmail']:
                                        business = legalCat['businessName']
                                        founder = legalCat['userName']
                                        year = legalCat['businessStartYear']
                                        category = legalCat['businessCategory']
                                        description = legalCat['businessDescription']
                                        address = legalCat['businessAddress']
                                        email = legalCat['businessEmail']
                                        phone = legalCat['businessNumber']
                                        web = legalCat['businessURL']
                                        tweet = legalCat['Twitter']
                                        insta = legalCat['Instagram']
                                        return render_template('update.html', business=business, founder=founder, year=year, category=category, description=description, address=address, email=email, phone=phone, web=web, tweet=tweet, insta=insta)
            # return render_template('update.html')
        except:
            return render_template('profile.html')
    else:
        pass

@app.route('/updateProfile', methods=['POST'])
def updateProfile():
    if request.method == 'POST':
        return render_template('updateProfile.html')

if __name__ == '__main__':
    app.run(debug=True)
