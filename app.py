from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages, jsonify 
import smtplib
import os
import pymongo
import re
from bson.objectid import ObjectId 

""" Retrieving the database environment variables """
MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = 'restaurant_reviews'
RESTAURANT = 'restaurant'
MENU = 'menu'
REVIEWS = 'reviews'

""" Creating database connection """
conn = pymongo.MongoClient(MONGO_URI)


app = Flask(__name__)



""" Globalising lists that are used by multiple routes when generating 
the select menu dropdown features on the 'Review' Form that displays for adding (creating), 
editing and deleting a review """
all_ratings = ["1", "2", "3", "4", "5"]
all_menu_items = conn[DATABASE_NAME][MENU].find()  


""" Flask Routes Begin Here """

""" Routing to display Index (Home) Page """
@app.route('/')
def index():
    
    return render_template('index.html')


""" Routing to display About Page. This section will serve to display the bistro contact details from the 'RESTAURANT' collection """
@app.route('/about')
def about():

    """Fetch restaurant details from database to display"""
    restaurant_details = conn[DATABASE_NAME][RESTAURANT].find_one({}) 
    
    return render_template('about.html', restaurant_details=restaurant_details)


""" Routing to display Menu Page. This section displays all menu items served by the bistro for which the documents are from the 'MENU' collection. """
#Image files are stored in 'static' folder, and are called by their respective file route by the 'MENU' collection.
@app.route('/menu')
def menu():
    """Fetch all menu items by categories and display them in alphabetical order"""
    appetisers = conn[DATABASE_NAME][MENU].find({'item_category': 'Appetiser'}).sort('item_name', pymongo.ASCENDING)
    pastas = conn[DATABASE_NAME][MENU].find({'item_category': 'Pasta'}).sort('item_name', pymongo.ASCENDING)
    pizzas = conn[DATABASE_NAME][MENU].find({'item_category': 'Pizza'}).sort('item_name', pymongo.ASCENDING)
    entrees = conn[DATABASE_NAME][MENU].find({'item_category': 'Entree'}).sort('item_name', pymongo.ASCENDING)    
    desserts = conn[DATABASE_NAME][MENU].find({'item_category': 'Dessert'}).sort('item_name', pymongo.ASCENDING)  
    
    return render_template('menu.html', appetisers=appetisers, pastas=pastas, pizzas=pizzas, entrees=entrees, desserts=desserts)
 

""" Routing to display the 'All Reviews' Page. All reviews are stored in documents in the 'REVIEWS' collection. """
@app.route('/reviews')
def see_all_reviews(): 
    
    """This serves to flash messages on the 'All Reviews' Page when user successfully creates(add), edits or deletes a review."""
    messages = get_flashed_messages()  

    """Fetch all reviews and display them according to visit date"""
    all_reviews = conn[DATABASE_NAME][REVIEWS].find({}).sort('date', pymongo.DESCENDING)
    return render_template('all_reviews.html', all_reviews=all_reviews)
    
    
""" Routing to display the 'Add Review' Page. 
The function under this route calls on the above globalised lists to display for the drop-down selectors for ratings and menu item names. """
@app.route('/reviews/new')
def add_review():

    return render_template('add_review.html', all_ratings=all_ratings, all_menu_items=all_menu_items, selected_review={})


""" Routing to process data in the review form to create the input from the user and store it in the 'REVIEWS' collection. """
@app.route('/reviews/new', methods=["POST"])
def process_add_review():

    date = request.form.get('visit_date')               # Reviewer's visit date
    reviewer_name = request.form.get('reviewer_name')   # Reviewer's name
    rating = request.form.get('rating')                 # Review rating
    comment = request.form.get('comment')               # Any (optional) comments

    """ Inserting the document into the 'REVIEWS' collection """
    conn[DATABASE_NAME][REVIEWS].insert({
        'date': date,
        'reviewer_name': reviewer_name,
        'rating': rating,
        'comment': comment
    })
    
    """ Message flashes upon sucessful creation of review. """
    # flash("Review successfully created")
    
    
    """ User is redirected to the 'All Reviews' Page after document is inserted into the collection """
    return redirect(url_for('see_all_reviews'))


""" Routing to generate form for user to edit review. 
Selected review for editing is called upon by the 'id' stored in the collection """
@app.route('/reviews/<review_id>/edit')
def edit_review(review_id):

    selected_review = conn[DATABASE_NAME][REVIEWS].find_one({
        '_id': ObjectId(review_id)
    })
    
    """ 'all_ratings' and 'all_menu_items' are called upon to display in the dropdown selectors of the 'review' form """
    return render_template('edit_review.html', selected_review=selected_review, all_ratings=all_ratings, all_menu_items=all_menu_items)


""" Routing to process 'review' form to make updates to the review being edited """
@app.route('/reviews/<review_id>/edit', methods=["POST"])
def process_edit_review(review_id):

    date = request.form.get('visit_date')               # Reviwer's visit date
    reviewer_name = request.form.get('reviewer_name')   # Reviewer's name
    rating = request.form.get('rating')                 # Review rating
    comment = request.form.get('comment')               # Any (optional) comments
    
    
    """ Updating amendments to selected document called from 'REVIEWS' collection """
    conn[DATABASE_NAME][REVIEWS].update({
        '_id': ObjectId(review_id)}, {
        '$set': {
        'date': date,
        'reviewer_name': reviewer_name,
        # 'item_name': dish_tasted,
        'rating': rating,
        'comment': comment
        }
    })

    """ Message flashes upon sucessful update of review. """
    # flash("Review successfully updated")

    """ User is redirected to 'All Reviews' Page """
    return redirect(url_for('see_all_reviews'))    


""" Routing to page that confirm with the if user whether or not to delete the selected review.
The review is selected by 'id'. """
@app.route('/reviews/<review_id>/confirm_delete')
def confirm_delete_review(review_id):
    
    selected_review = conn[DATABASE_NAME][REVIEWS].find_one({
        '_id': ObjectId(review_id)
    })    
    
    return render_template('confirm_delete_review.html', selected_review=selected_review)


""" Routing to process with review deletion that is confirmed by user. """
@app.route('/reviews/<review_id>/delete')
def delete_review(review_id):
    
    """" Search of selected review in collection by document 'id' """
    selected_review = conn[DATABASE_NAME][REVIEWS].find_one({
        '_id': ObjectId(review_id)
    })    
    
    """ Document deletion """
    conn[DATABASE_NAME][REVIEWS].delete_one({
        '_id': ObjectId(review_id)
    })

    """ Message notifiction of successful review deletion """
    # flash("Review has been deleted")
    
    """ User is redirected to 'All Reviews' page """
    return redirect(url_for('see_all_reviews'))


# Flask boilerplate and calling constants for message flash
if __name__ == '__main__':

    app.secret_key = os.getenv('SECRET_KEY')
    app.config['SESSION_TYPE'] = os.getenv('SESSION_TYPE')
    
    app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)
           
           