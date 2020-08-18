import pyrebase

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

artCategory = db.child("Bame_Business").child("business").child("arts_Media_Tech").get()
foodCategory = db.child("Bame_Business").child("business").child("foods_Restaurants_Takeaways").get()
healthCategory = db.child("Bame_Business").child("business").child("health_Lifestyle_Sports").get()
housingCategory = db.child("Bame_Business").child("business").child("housing_Property_ConstructionServices").get()
retailCategory = db.child("Bame_Business").child("business").child("retail_Fashion_Jewellery").get()
charityCategory = db.child("Bame_Business").child("business").child("charities_SupportGroups").get()
legalCategory = db.child("Bame_Business").child("business").child("legal_Financial").get()

def art_search(find):
    artCategory = db.child("Bame_Business").child("business").child("arts_Media_Tech").get()
    artCat = [x.val() for x in artCategory.each()]
    art_category = len(artCat)
    art_category = range(art_category)
    find = find.split(", ")
    f = len(find)
    f = range(f)
    for x in f:
        for y in art_category:
            if find[x] in artCat[y]['keyWords']:
                return artCat[y]['businessName']
                # return artCat[y]['']

def legal_search(find):
	legalCategory = db.child("Bame_Business").child("business").child("legal_Financial").get()
	legalCat = [x.val() for x in legalCategory.each()]
	legal_category = len(legalCat)
	legal_category = range(legal_category)
	find = find.split(", ")
	f = len(find)
	f = range(f)
	for x in f:
		for y in legal_category:
			if find[x] in legalCat[y]['keyWords']:
				print(legalCat[y]['businessName'])
				print(legalCat[y]['userName'])
				print(legalCat[y]['businessStartYear'])
				print(legalCat[y]['businessDescription'])
				print(f"Your keyword >>>{find[x]}<<< was matched with: {legalCat[y]['keyWords']}")
				print(" ")
			else:
				pass
