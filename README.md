# Sofia's Bistro

**One or two paragraphs providing an overview of your project.*

**Essentially, this part is your sales pitch.*

Sofia's Bistro is a fictional bistro. The ideology behind the bistro's existence is that it is a small business owned by a (fictional) family, who are running the business with just one outlet. They have set up the establishment to serve a selection of Italian dishes for which the recipes have been passed down within the family through generations. The family operates the bistro in Singapore with the hopes to create awareness to the community via an online medium: a website called "Sofia's Bistro". Eventually the business owners are hoping to develop a niche in the community of Singapore by by featuring the homestyle Italian food. Being family oriented, they would like open a connection with their past and existing customers to give them a voice on to share with the community of Singapore about their dining experience at the bistro. Moreover, the website will open an opportunity to allow any website visitors to become potential customers for the restaurant, and ultimately for the business owners to understand what is popular amongst their customers for future business growth of the bistro.

The project link may be found here:     https://msp-restaurant.herokuapp.com/ 

## UX
 
**Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

**In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

**This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

The website is meant for potential customers and existing customers to be able to know of the restaurant and what food they serve.

As a website visitor, I will access the website url, which will take me to the homepage. I will be able to comprehend business nature of the website owner from the website name and the visual presentation.

As a website visitor, I will click the 'About' navigation tab so as to get an understanding of the business nature of the website owner, and also access the website owner's contact details.

As a website visitor, click the 'Menu' navigation tab which will show me the type of food the bistro sells. This will serve the purpose of me to make the decision if the menu is what I would like to consider if I am choosing an eating establishment to visit.

As a website visitor, I will click the 'Review' navigation dropdown tab, and then click on the 'All Reviews' to have an understanding of how customers have found the bistro to be. This will give me further insight to making a decision on whether to consider visitng the bistro.

As a website visitor who has visited the restaurant, click the 'Review' navigation dropdown tab, and then click on the 'Add Review' so to be able to complete the review form to provide my dining experience.

As a website visitor who has submitted a review and wishes to make amendments to it, click on the 'Review' navigation dropdown tab, and click on the 'Edit' button for the respective review to be amended. This will display the stored contents of the review in the format of the form. After making the necessary amendments, click on the 'Edit' button. The website site will then redirect to the 'All Reviews' page and display a notification that the review was successfully updated, which will be visible on that page.

As a website visitor who wishes to delete a review, click on the 'Review' navigation dropdown tab, and click on the 'Delete' button. The page will direct to a notification page to ask the user if they wish to delete the review. Click on 'Yes' button will have the review deleted. The site will redirect to the 'All Reviews' page and display a notification that states the review was successfully deleted.

Essentially, the project has developed a section where and providing a section for individuals who visited the restaurant, the project served its purpose to use a website as a medium to in rendering views to the community about the bistro as well as a means for the bistro owner to receive feedback in an open way. Ultimately, the website aimed to serve the as a medium to the business owners to hear from their visitors/customers to receive input for future implementaion plans to expand their business.

## Features

**In this section, you should go over the different parts of your project, and describe each in a sentence or so.

The website navigation bar has four sections:

1. Home - This is the first page displayed to the site visitor, it gives a visual image of the bistro.

2. About - This is where the site visitor is able to retrieve information about the bistro's contact details and location.

3. Menu - This features the menu which the bistro serves.

4. Reviews - This tab leads to two sections: 
   (i) All Reviews - This is where the site visitor is able to view all reviews posted by customers. Each posted review provides the user the option to amend or delete the posted review.
   (ii) Add Review - This opens to a form whereby the site visitor is able to provide their review and rate their visit to the bistro.
   
 
### Existing Features
- The main features of the project are as follows:

- Menu Page - This displays the menu of items which the bistro serves. The information and pictures are rendered from the database.

- Reviews section - This allows the user to review existing reviews, and also add, edit or delete a review.

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

Features to implement in the future:
- To have a form of authentication to control user ability to amend and delete reviews.
- To have review ratings to be tabulated and produce data statistics to the business owner to understand the feedback from customers.
- To have notification stated if no reviews are available for display.

### Features Left to Implement
- To implement user login account for visitors to register and login for review sharing purposes.
- Admin account access for the business owner to be able to provide updates on the website with regards to their bistro.

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [HTML](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [CSS](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [Bootstrap](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
 
 - [Python](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [MongoDB](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [Heroku](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Navigation Menu:
  1. Open the website at the Home Page.
  2. Try to click on each of the following navigation tabs to view that they direct to the appropriate pages:
    1. 'About' will link to the 'About' page
    2. 'Menu' will link to the 'Menu' page
    3. 'Reviews - All Reviews' will link to 'All Reviews' page
    4. 'Reviews - Add Review' will link to the 'Add Review' page

1. Review Form - Add Review:
    1. Go to the "Reviews - Add Review" page
    2. Try to submit the form with the visit date field left empty and verify that a message will appear to prompt the user to fill up those required fields.
    3. Try to submit the form with the name field left empty and verify that a message will appear to prompt the user to fill up those required fields.
    4. Try to submit the form with the rating left unselected for any number and verify that a message will appear to prompt the user to fill up those required fields.
    5. Try to submit the form with all inputs completed except for the comment field and verify that the review entry is successfully added upon completion of clicking the 'Add' button.
    6. Try to submit the form with all inputs completed and verify that the review entry is successfully added upon completion of clicking the 'Add' button.

2. Review Form - Edit Review:
    1. Go to the "Reviews - All Reviews" page
    2. Click the 'Edit' button for selected review to edit and verify that the page with the review form will show with all fields displaying the existing content.
    3. Make amendments to the content with the visit date field left empty and verify that a message will appear to prompt the user to fill up the visit date field.
    4. Make amendments to the content with the name field left empty and verify that a message will appear to prompt the user to fill up the name field.
    5. Make amendments to the content with the rating field left unselected for a number and verify that a message will appear to prompt the user to select the rating.
    6. Try to submit the form with all inputs amended and completed except for the comment field and verify that the review entry is successfully updated upong clicking the 'Update' button.
    7. Try to submit the form with all inputs amended and completed and verify that the review entry is successfully updated upong clicking the 'Update' button. The page will redirect to the 'All Reviews' page and have a flash message appear stating that the review has been updated. The updated review will appear on the 'All Reviews' page.
    8. Click the 'Cancel' button and verify that the 'All Reviews' page will be returned. 

3. Review Form - Delete Review:
    1. Go to the "Reviews - All Reviews" page
    2. Click the 'Delete' button for selected review to be deleted and verify that the page will be directed to a 'Deletion Confirmation' page that states the details of the review that is intended for deletion.
    3. Click on the 'No' button and verify that the page will be directed to the 'All Reviews' page.
    4. Click on the 'Yes' button and verify that the review is successfully deleted. The page will direct to the'All Reviews' page with a flash message appear stating that the review has been deleted. Deleted review will not appear on the 'All Reviews' page.
    
    
Bugs Encountered: Upon deployment to heroku, the page would not display itself upon adding, editing and deleting a review. The issue was rectified by importing smtplib to the app.py file.

All pages have been checked on smaller devices to ensure that they are presentably displayed as mobile responsive.

**In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

**You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

**If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

The project had been deployed on Heroku.
The coding and documentation may be found on GitHub.


## Credits

1. getting a boostrap template to make the website

https://bootstrapmade.com/




3. Pictures from Pexels:

https://www.pexels.com/photo/clear-wine-glass-on-table-67468/
https://www.pexels.com/photo/close-up-of-menu-313700/

Menu items:
(appetisers):
https://www.pexels.com/photo/bread-cooking-cuisine-delicious-299410/
https://www.pexels.com/photo/appetizer-avocado-bacon-cuisine-551997/
https://www.pexels.com/photo/appetizer-basil-caprese-cheese-416510/
https://www.pexels.com/photo/spinach-chicken-pomegranate-salad-5938/

(pastas):
https://www.pexels.com/photo/pasta-dish-with-rice-on-white-ceramic-plate-8489/
https://www.pexels.com/photo/blur-close-up-cutlery-delicious-590477/
https://www.pexels.com/photo/seashell-dish-921374/

(pizzas):
https://www.pexels.com/photo/pizza-slice-842519/
https://www.pexels.com/photo/pizza-on-brown-wooden-board-825661/

(entrees):
https://www.pexels.com/photo/beef-cuisine-delicious-dinner-299347/
https://www.pexels.com/photo/selective-focus-photography-of-beef-steak-with-sauce-675951/
https://www.pexels.com/photo/seafood-dish-with-french-fries-in-white-ceramic-plate-7782/
https://www.pexels.com/photo/close-up-of-meal-served-in-plate-323682/

(desserts):
https://www.pexels.com/photo/restaurant-coffee-chocolate-dessert-2230/
https://www.pexels.com/photo/food-restaurant-summer-nuts-2424/

(beverages):
https://www.pexels.com/photo/background-blur-bread-breakfast-364109/
https://www.pexels.com/photo/shallow-focus-photography-of-cafe-late-982612/
https://www.pexels.com/photo/clear-glass-bottle-filled-with-broccoli-shake-1346347/
https://www.pexels.com/photo/shake-in-a-glass-990439/
https://www.pexels.com/photo/art-beverage-blur-caffeine-302896/
https://www.pexels.com/photo/clear-highball-glass-with-iced-tea-1484678/


4. Mongo Documentation
https://docs.mongodb.com/manual/reference/operator/query/eq/

5. Pymongo documentation
https://api.mongodb.com/python/current/examples/aggregation.html

6. Bootstrap template
https://colorlib.com/wp/template/feliciano/

7. Jumbotron positioning on home page
https://stackoverflow.com/questions/42252443/vertical-align-center-in-bootstrap-4


### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

3. Pictures from Pexels:

https://www.pexels.com/photo/clear-wine-glass-on-table-67468/
https://www.pexels.com/photo/close-up-of-menu-313700/

Menu items:
(appetisers):
https://www.pexels.com/photo/bread-cooking-cuisine-delicious-299410/
https://www.pexels.com/photo/appetizer-avocado-bacon-cuisine-551997/
https://www.pexels.com/photo/appetizer-basil-caprese-cheese-416510/
https://www.pexels.com/photo/spinach-chicken-pomegranate-salad-5938/

(pastas):
https://www.pexels.com/photo/pasta-dish-with-rice-on-white-ceramic-plate-8489/
https://www.pexels.com/photo/blur-close-up-cutlery-delicious-590477/
https://www.pexels.com/photo/seashell-dish-921374/

(pizzas):
https://www.pexels.com/photo/pizza-slice-842519/
https://www.pexels.com/photo/pizza-on-brown-wooden-board-825661/

(entrees):
https://www.pexels.com/photo/beef-cuisine-delicious-dinner-299347/
https://www.pexels.com/photo/selective-focus-photography-of-beef-steak-with-sauce-675951/
https://www.pexels.com/photo/seafood-dish-with-french-fries-in-white-ceramic-plate-7782/
https://www.pexels.com/photo/close-up-of-meal-served-in-plate-323682/

(desserts):
https://www.pexels.com/photo/restaurant-coffee-chocolate-dessert-2230/
https://www.pexels.com/photo/food-restaurant-summer-nuts-2424/

(beverages):
https://www.pexels.com/photo/background-blur-bread-breakfast-364109/
https://www.pexels.com/photo/shallow-focus-photography-of-cafe-late-982612/
https://www.pexels.com/photo/clear-glass-bottle-filled-with-broccoli-shake-1346347/
https://www.pexels.com/photo/shake-in-a-glass-990439/
https://www.pexels.com/photo/art-beverage-blur-caffeine-302896/
https://www.pexels.com/photo/clear-highball-glass-with-iced-tea-1484678/

### Acknowledgements

- I received inspiration for this project from 

2. Restaurant to get Menu ideas:
https://buonappetitoitalian.com/menus/lunch-menu

https://www.zomato.com/
