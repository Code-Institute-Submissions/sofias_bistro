from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo
import re
from bson.objectid import ObjectId 

#Retrieving the database environment variables
MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = 'restaurant_reviews'
RESTAURANT = 'restaurant'
MENU = 'menu'
REVIEWS = 'reviews'

# Creating database connection
conn = pymongo.MongoClient(MONGO_URI)


app = Flask(__name__)

# Flask Routes Begin Here

#Routing Index (Home) Page
@app.route('/')
def index():
    
    return render_template('index.html')


#Routing About Page
@app.route('/about')
def about():
    
    return render_template('about.html')


#Routing Menu Page
@app.route('/menu')
def menu():
    """#Fetch all menu items by categories and display them in alphabetical order"""
    appetisers = conn[DATABASE_NAME][MENU].find({'item_category': 'Appetiser'}).sort('item_name', pymongo.ASCENDING)
    pastas = conn[DATABASE_NAME][MENU].find({'item_category': 'Pasta'}).sort('item_name', pymongo.ASCENDING)
    pizzas = conn[DATABASE_NAME][MENU].find({'item_category': 'Pizza'}).sort('item_name', pymongo.ASCENDING)
    entrees = conn[DATABASE_NAME][MENU].find({'item_category': 'Entree'}).sort('item_name', pymongo.ASCENDING)    
    desserts = conn[DATABASE_NAME][MENU].find({'item_category': 'Dessert'}).sort('item_name', pymongo.ASCENDING)  
    
    return render_template('menu.html', appetisers=appetisers, pastas=pastas, pizzas=pizzas, entrees=entrees, desserts=desserts)

@app.route('/reviews/new')
def add_review():
    
    rating = request.args.get('rating')
    dish = request.args.get('menu_item')
    
    all_ratings = ["1", "2", "3", "4", "5"]
    all_menu_items = ["Tomato Bruschetta", "Sofia's Caprese Salad", "House Salad", "Ravioli Ai Funghi", "Spaghetti Ai Frutti di Marre", "Margherita", "Diavola", "Salmone Al Griglia", "Veal Buon Appetito", "Tiramisu", "Chocolate Coffee Cake"]

    cursor = conn[DATABASE_NAME][MENU].find()
    
    return render_template('add_review.html', all_ratings=all_ratings, all_menu_items=all_menu_items, result=cursor)

#Routing Contact Page
@app.route('/contact')
def contact():
    
    return render_template('contact.html')

    
#Routing to process newly created review
@app.route('/reviews/new', methods=["POST"])
def process_added_review():
        
    visit_date = request.form.get('visit_date')
    reviewer_name = request.form.get('reviewer_name')
    comment = request.form.get('comment')

    return render_template("index.html")

#Routing page of reviews for each menu item
@app.route('/menu/<menu_item_id>/reviews')
def see_reviews(menu_item_id):
    results = conn[DATABASE_NAME][MENU].find_one({
        '_id': ObjectId(menu_item_id)
    })
    
    results2 = conn[DATABASE_NAME][REVIEWS].aggregate([{
        "$match": { 'menu_item_id': ObjectId(menu_item_id) }
    }])
    
    return render_template('reviews.html', item_results=results, reviews=results2)





# "magic code" -- boilerplate
if __name__ == '__main__':
   app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)
           
           