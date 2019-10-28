from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo

#Retrieving the database environment variables
MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = 'sofias_bistro'

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
    
    return render_template('menu.html')


#Routing Menu Page
@app.route('/contact')
def contact():
    
    return render_template('contact.html')
    

# "magic code" -- boilerplate
if __name__ == '__main__':
   app.run(host=os.environ.get('IP'),
           port=int(os.environ.get('PORT')),
           debug=True)
           
           