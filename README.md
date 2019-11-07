# Sofia's Bistro


Sofia's Bistro is a fictional bistro. The ideology behind the bistro's existence is that it is a small business owned by a (fictional) family, who are running the business with just one outlet. They have set up the establishment to serve a selection of Italian dishes for which the recipes have been passed down within the family through generations. The family operates the bistro in Singapore with the hopes to create awareness to the community via an online medium: a website called "Sofia's Bistro". Eventually the business owners are hoping to develop a niche in the community of Singapore by by featuring the homestyle Italian food. Being family oriented, they would like open a connection with their past and existing customers to give them a voice on to share with the community of Singapore about their dining experience at the bistro. Moreover, the website will open an opportunity to allow any website visitors to become potential customers for the restaurant, and ultimately for the business owners to understand what is popular amongst their customers for future business growth of the bistro.

The link to the project may be found [here.](https://msp-restaurant.herokuapp.com/ "Sofia's Bistro")


---


## UX


A copy of the project wireframe may be found [here.](https://github.com/amcali/sofias_bistro/issues/2/ "Sofia's Bistro - Project Wireframe")

The website is for essentially for three types of target audiences:

i) Customers - For any individuals who had and regularly visit the bistro, the website's contents and UX intends to provide an feature to allow customers to share their dining experience.

ii) Website Visitors - this defines any individuals who visit the website, and do not know about the bistro.

iii) Business Owners - The owners of the bistro would be able to view the reviews from its customers and use the website to display what its business has to offer.

The following scenarios illustrate how the website's existing features to serves its target audiences.



#### 1) Customers

As a user who has visited the restaurant, click the 'Review' navigation dropdown tab, and then click on the 'Add Review' so to be able to complete the review form to provide my dining experience.

As a website visitor who has submitted a review and wishes to make amendments to it, click on the 'Review' navigation dropdown tab, and click on the 'Edit' button for the respective review to be amended. This will display the stored contents of the review in the format of the form. After making the necessary amendments, click on the 'Edit' button. The website site will then redirect to the 'All Reviews' page and display a notification that the review was successfully updated, which will be visible on that page.

As a website visitor who wishes to delete a review, click on the 'Review' navigation dropdown tab, and click on the 'Delete' button. The page will direct to a notification page to ask the user if they wish to delete the review. Click on 'Yes' button will have the review deleted. The site will redirect to the 'All Reviews' page and display a notification that states the review was successfully deleted.



#### 2) Website Visitors

As a website visitor, I will access the website url, which will take me to the homepage. I will be able to comprehend business nature of the website owner from the website name and the visual presentation.

As a website visitor, I will click the 'About' navigation tab so as to get an understanding of the business nature of the website owner, and also access the website owner's contact details.

As a website visitor, click the 'Menu' navigation tab which will show me the type of food the bistro sells. This will serve the purpose of me to make the decision if the menu is what I would like to consider if I am choosing an eating establishment to visit.

As a website visitor, I will click the 'Review' navigation dropdown tab, and then click on the 'All Reviews' to have an understanding of how customers have found the bistro to be. This will give me further insight to making a decision on whether to consider visitng the bistro.



#### 3) Business Owners

As the website's business owner, I will click the 'Review' navigation dropdown tab, and then click on the 'All Reviews' to have an understanding of how customers have found the bistro to be. This will give me insight from customers' inputs to factor in ideas for future implementaion plans to expand the business.


---


## Features


The website has four sections which are accessble via the navigation menu:

__1. Home__ - This is the first page displayed to the site visitor, it gives a visual image of the bistro.

__2. About__ - This is where the site visitor is able to retrieve information about the bistro's contact details and location.

__3. Menu__ - This features the menu which the bistro serves.

__4. Reviews__ - This tab leads to two sections: 

  __i) All Reviews__ - This is where the site visitor is able to view all reviews posted by customers. Each posted review provides the user the option to amend or delete the posted review.

  __i) Add Review__ - This opens to a form whereby the site visitor is able to provide their review and rate their visit to the bistro.


 
### Existing Features

The main features of the project are as follows:

__Menu Page and Contact Page__ - This displays the menu of items which the bistro serves, and the bistro location respectively. The information and pictures are rendered from a database.

__Reviews section__ - This allows the user to review existing reviews, and also add, edit or delete a review. All reviews stored, recalled, updated and deleted are done so via the website, and stored in a database.

The features that are considered for future implementation are as follows:
- To have a form of authentication to control user ability to amend and delete reviews.
- To have review ratings to be tabulated and produce data statistics to the business owner to understand the feedback from customers.
- To have notification stated if no reviews are available for display.



### Features Left to Implement

- To implement user login account for visitors to register and login for review sharing purposes. This in turn will control the accessibility of each user to amend and delete the review(s) which they created.
- To have notification messages to appear when the user successfully adds, edits or delete
- Admin account access for the business owner to be able to provide updates on the website with regards to their bistro. Such updates would be any menu changes, or promotional features.


---


## Technologies Used


In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [HTML](https://html.com/)
    - The project uses **HTML** for the markup language of all HTML pages.

- [CSS](https://www.w3.org/Style/CSS/Overview.en.html/)
    - The project uses **CSS** to for basic styling of the web pages.

- [Bootstrap](https://getbootstrap.com/)
    - The project uses **Boostrap** to implement the UI framework to the webpages.
 
 - [Python Flask](https://www.fullstackpython.com/flask.html)
    - The project uses **Python Flask** to implement Python coded functionality to the webpages.

- [Jinja](https://www.palletsprojects.com/p/jinja/)
    - The project uses **Jinja** to implement Flask functionality to the HTML files.

- [MongoDB](https://www.mongodb.com/)
    - The project uses **MongoDB** to hold the database in which some of the web page contents are stored.

- [GitHub](https://github.com/)
    - The project uses **GitHub** to document the development and coding.

- [Heroku](https://heroku.com/)
    - The project uses **Heroku** to deploy the website.

- [W3 Schools](https://www.w3schools.com/)
    - The project uses **W3 Schools** resources to create the HTML, CSS and Bootstrap features implemented.

- [Python](https://www.python.org/)
    - The project uses **Python** website resources to develop the coding used.


---


## Testing


For this project, manual testing was done as follows:


#### 1. Navigation Menu:

  i) Open the website at the Home Page.
  
  ii) Try to click on each of the following navigation tabs to view that they direct to the appropriate pages:
  
   a) 'About' will link to the 'About' page
    
   b) 'Menu' will link to the 'Menu' page
    
   c) 'Reviews - All Reviews' will link to 'All Reviews' page
    
   d) 'Reviews - Add Review' will link to the 'Add Review' page


#### 2. Review Form - Add Review:

    i) Go to the "Reviews - Add Review" page.
    
    ii) Try to submit the form with the visit date field left empty and verify that a message will appear to prompt the user to fill up those required fields.
    
    iii) Try to submit the form with the name field left empty and verify that a message will appear to prompt the user to fill up those required fields.
    
    iv) Try to submit the form with the rating left unselected for any number and verify that a message will appear to prompt the user to fill up those required fields.
    
    v) Try to submit the form with all inputs completed except for the comment field and verify that the review entry is successfully added upon completion of clicking the 'Add' button.
    
    vi) Try to submit the form with all inputs completed and verify that the review entry is successfully added upon completion of clicking the 'Add' button.


#### 3. Review Form - Edit Review:

    i) Go to the "Reviews - All Reviews" page.
    
    ii) Click the 'Edit' button for selected review to edit and verify that the page with the review form will show with all fields displaying the existing content.
    
    iii) Make amendments to the content with the visit date field left empty and verify that a message will appear to prompt the user to fill up the visit date field.
    
    iv) Make amendments to the content with the name field left empty and verify that a message will appear to prompt the user to fill up the name field.
    
    v) Make amendments to the content with the rating field left unselected for a number and verify that a message will appear to prompt the user to select the rating.
    
    vi) Try to submit the form with all inputs amended and completed except for the comment field and verify that the review entry is successfully updated upong clicking the 'Update' button.
    
    vii) Try to submit the form with all inputs amended and completed and verify that the review entry is successfully updated upon clicking the 'Update' button. The page will redirect to the 'All Reviews' page, and the updated review will appear on the 'All Reviews' page.
    
    viii) Click the 'Cancel' button and verify that the 'All Reviews' page will be returned. 


#### 4. Review Form - Delete Review:

    i) Go to the "Reviews - All Reviews" page.
    
    ii) Click the 'Delete' button for selected review to be deleted and verify that the page will be directed to a 'Deletion Confirmation' page that states the details of the review that is intended for deletion.
    
    iii) Click on the 'No' button and verify that the page will be directed to the 'All Reviews' page.
    
    iv) Click on the 'Yes' button and verify that the review is successfully deleted. The page will direct to the'All Reviews' page, and the deleted review will not appear on the 'All Reviews' page.
    
    
#### 5. Mobile Responsive:

All pages have been checked on smaller devices to ensure that they are presentably displayed as mobile responsive.


#### 6. Bugs Encountered: 

Upon deployment to heroku, the page would not display itself upon adding, editing and deleting a review due to an "Internal Server Error 500" issue. The issue was rectified by removing the Flask Flash Message function initially implemented for notification messages, but which only worked during testing on Cloud9.


---


## Deployment

The project was developed on [AWS Cloud9.] (https://aws.amazon.com/education/awseducate/)
The project had been deployed on [Heroku.] (https://msp-restaurant.herokuapp.com/)
The coding and documentation may be found on [GitHub.] (https://github.com/amcali/sofias_bistro)


---


## Credits

The following resources have been used for this project:

#### 1. Pictures: 
All pictures in this project are from Pexels:
https://www.pexels.com/photo/clear-wine-glass-on-table-67468/
https://www.pexels.com/photo/bread-cooking-cuisine-delicious-299410/
https://www.pexels.com/photo/appetizer-avocado-bacon-cuisine-551997/
https://www.pexels.com/photo/appetizer-basil-caprese-cheese-416510/
https://www.pexels.com/photo/cooked-food-on-black-bowl-688804/
https://www.pexels.com/photo/seashell-dish-921374/
https://www.pexels.com/photo/pizza-with-red-pepper-and-cheese-1049620/
https://www.pexels.com/photo/pizza-on-brown-wooden-board-825661/
https://www.pexels.com/photo/close-up-of-meal-served-in-plate-323682/
https://www.pexels.com/photo/brown-fish-fillet-on-white-ceramic-plate-46239/
https://www.pexels.com/photo/restaurant-coffee-chocolate-dessert-2230/
https://www.pexels.com/photo/cake-chocolate-chocolate-cake-cocoa-373066/


#### 4. Mongo Documentation
https://docs.mongodb.com/manual/reference/operator/query/eq/

#### 5. Pymongo documentation
https://api.mongodb.com/python/current/examples/aggregation.html

#### 6. Bootstrap template
https://colorlib.com/wp/template/feliciano/

#### 7. Jumbotron positioning on home page
https://stackoverflow.com/questions/42252443/vertical-align-center-in-bootstrap-4


### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from [Pexels.](https://www.pexels.com/)

Home Page: 
https://www.pexels.com/photo/clear-wine-glass-on-table-67468/

Menu Page:
https://www.pexels.com/photo/bread-cooking-cuisine-delicious-299410/
https://www.pexels.com/photo/appetizer-avocado-bacon-cuisine-551997/
https://www.pexels.com/photo/appetizer-basil-caprese-cheese-416510/
https://www.pexels.com/photo/cooked-food-on-black-bowl-688804/
https://www.pexels.com/photo/seashell-dish-921374/
https://www.pexels.com/photo/pizza-with-red-pepper-and-cheese-1049620/
https://www.pexels.com/photo/pizza-on-brown-wooden-board-825661/
https://www.pexels.com/photo/close-up-of-meal-served-in-plate-323682/
https://www.pexels.com/photo/brown-fish-fillet-on-white-ceramic-plate-46239/
https://www.pexels.com/photo/restaurant-coffee-chocolate-dessert-2230/
https://www.pexels.com/photo/cake-chocolate-chocolate-cake-cocoa-373066/

All written content on all the webpages are self created. The menu names were generated from research via [Google](https://www.google.com/). The contact details on the [About](https://msp-restaurant.herokuapp.com/about) page is fictional.


### Acknowledgements

I received inspiration for this project from the following:
[Buon Appetito Italian Restaurant & Delicatessens](https://buonappetitoitalian.com/menus/lunch-menu)
[Zomato](https://www.zomato.com/)

**All content used and deployed in this project is solely used for educational purposes.
