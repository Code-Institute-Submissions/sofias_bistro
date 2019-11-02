from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo
import re
from bson.objectid import ObjectId 
from datetime import datetime

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
    """Fetch all menu items by categories and display them in alphabetical order"""
    appetisers = conn[DATABASE_NAME][MENU].find({'item_category': 'Appetiser'}).sort('item_name', pymongo.ASCENDING)
    pastas = conn[DATABASE_NAME][MENU].find({'item_category': 'Pasta'}).sort('item_name', pymongo.ASCENDING)
    pizzas = conn[DATABASE_NAME][MENU].find({'item_category': 'Pizza'}).sort('item_name', pymongo.ASCENDING)
    entrees = conn[DATABASE_NAME][MENU].find({'item_category': 'Entree'}).sort('item_name', pymongo.ASCENDING)    
    desserts = conn[DATABASE_NAME][MENU].find({'item_category': 'Dessert'}).sort('item_name', pymongo.ASCENDING)  
    
    return render_template('menu.html', appetisers=appetisers, pastas=pastas, pizzas=pizzas, entrees=entrees, desserts=desserts)
 
 
@app.route('/reviews')
def see_all_reviews(): 
    """Fetch all reviews and display them according to visit date"""
    all_reviews = conn[DATABASE_NAME][REVIEWS].find({}).sort('date', pymongo.DESCENDING)
    return render_template('all_reviews.html', all_reviews=all_reviews)
 
 
@app.route('/reviews/new')
def add_review():
    
    # rating = request.form.get('rating')
    # dish = request.form.get('item_name')
    
    all_ratings = ["1", "2", "3", "4", "5"]
    all_menu_items = conn[DATABASE_NAME][MENU].find()

    return render_template('add_review.html', all_ratings=all_ratings, all_menu_items=all_menu_items)



""" ORIGINAL ADD REVIEW FUNCTION PUSHES AS ARRAY IN MENU COLLECTIONS """   

# @app.route('/reviews/new', methods=['POST'])
# def process_add_review():
    
#     all_ratings = ["1", "2", "3", "4", "5"]
#     all_menu_items = conn[DATABASE_NAME][MENU].find()    
    
#     menu_item_id = request.form.get('item_name')
    
    
#     new_review = {
#         'date': request.form.get('visit_date'),
#         'reviewer_name': request.form.get('reviewer_name'),
#         'rating': request.form.get('rating'),
#         'comment': request.form.get('comment')
#     }

#     insert_review = conn[DATABASE_NAME][MENU].update({
#         '_id': ObjectId(menu_item_id)},
#         {'$push': {'reviews': new_review}})
    
#     # return new_review 
#     return render_template('index.html', new_review=new_review, insert_review=insert_review)    

""" END OF ORIGINAL ADD REVIEW FUNCTION """

@app.route('/reviews/new', methods=["POST"])
def process_add_review():

    all_ratings = ["1", "2", "3", "4", "5"]
    all_menu_items = conn[DATABASE_NAME][MENU].find()    
    
    menu_item_id = request.form.get('item_name')
    date = request.form.get('visit_date')
    reviewer_name = request.form.get('reviewer_name')
    # dish_tasted = request.form.get('item_name')
    rating = request.form.get('rating')
    comment = request.form.get('comment')


    conn[DATABASE_NAME][REVIEWS].insert({
        'menu_item_id': ObjectId(menu_item_id),
        'date': date,
        'reviewer_name': reviewer_name,
        # 'item_name': dish_tasted,
        'rating': rating,
        'comment': comment
    })
    
    
    return redirect(url_for('see_all_reviews'))





#Routing page of reviews for each menu item
@app.route('/menu/<menu_item_id>/reviews')
def see_menu_reviews(menu_item_id):

    item_results = conn[DATABASE_NAME][MENU].find_one({ '_id': ObjectId(menu_item_id)})
    reviews = conn[DATABASE_NAME][REVIEWS].aggregate([{
        "$match": { 'menu_item_id': ObjectId(menu_item_id) }
    }])

    return render_template('menu_reviews.html', item_results=item_results, reviews=reviews)




#Routing to generate form for editing review
@app.route('/reviews/<review_id>/edit')
def edit_review(review_id):

    all_ratings = ["1", "2", "3", "4", "5"]
    all_menu_items = conn[DATABASE_NAME][MENU].find()   
    
    selected_review = conn[DATABASE_NAME][REVIEWS].find_one({
        '_id': ObjectId(review_id)
    })
    
    return render_template('edit_review.html', selected_review=selected_review, all_ratings=all_ratings, all_menu_items=all_menu_items)


# "magic code" -- boilerplate
if __name__ == '__main__':
   app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)
           
           