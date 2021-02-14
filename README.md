# [MS3 - Pig in a Ginnel](http://pigginnel.herokuapp.com)

- [Introduction](#introduction)
- [UX](#ux)
  - [The Design](#the-design)
  - [Wireframes](#wireframes)
  - [User-stories](#user-stories)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [MongoDB](#mongodb)
  - [Okta](#okta)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Inspiration](#inspiration)
  - [Acknowledgements](#acknowledgements)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Introduction
 
The live website can be found here at [http://pigginnel.herokuapp.com](http://pigginnel.herokuapp.com)

# UX

When people go to restaurants, there are three features people want when researching where to eat; 
1. The Menu. What food, or, what style of food, is on offer. 
2. What did other people make of the restaurant, how did they review it?
3. The ability to book a reservation. 

This usually relies on three different websites; The restaurant's own, TripAdvisor/Yelp, OpenTable/DesignMyNight. The fact that there are several options for both the reviews and bookings can be annoying. The idea behind my project is to bring all three of those features into one website. This website has the standard information about this fictional restaurant (who the chef is, what style the food is, where to find it...), as well as the ability for users to leave reviews, and to see other users' reviews, and to make reservations. In addition to that, the ability for users to edit and delete their own reviews and reservations.

## The Design

In the wireframes, it is clear that originally the plan was to separate all the individuals sections over separate pages. However, after contemplating using [this template](https://bootstrapmade.com/restaurantly-restaurant-template/), I decided to streamline the content onto as few pages as possible. The template was not implemented due to wanting to showcase my ability to implement my own designs. However, I certainly took inspiration from that template. 

One way I wanted to differ from that template, was I wanted to have a much more minimalist website. I also wanted to use more white colours than black. On top of all that, I wanted to showcase my ability to learn to use a new framework beyond Bootstrap. After considering Materialize, and realising it was not what I personally was after, I opted to use [UiKit](https://getuikit.com). UiKit is focused around minimalism, and a clean appearance, colours are basic too - these I felt are appropriate for a website orientated around a restaurant. The logic behind that statement being that the restaurant is focused around its food, not on its design. Whilst having good UI and UX is still important, I did not want the create the impression that more effort would have been put into the marketing and website of this fictional restaurant, than on the produce of the restaurant itself.

The fonts were taken from [Google Fonts](https://fonts.google.com), and the ones that have been used as: 

- [Permanent Marker](fonts.google.com/specimen/Permanent+Marker), for the site logo.

- [Indie Flower](fonts.google.com/specimen/Indie+Flower), for the navbar and footer.

- [Raleway](fonts.google.com/specimen/Raleway), for all other text on the site.

## [Wireframes](/wireframes/)

[Adobe XD](https://www.adobe.com/uk/products/xd.html) was used to create the initial wireframes, the pdf file with all the wireframes can be viewed in [Wireframes](/wireframes/ms3_restaurant.pdf).

## User-stories

- As a user, I want to see the sample menus for the restaurant, so I know the style of food on offer.

  - [On the index page, either through clicking the menu in navbar, or scrolling down](/readme/img/features/express.PNG)
  - [At the same point, but having selected Sample Tasting Menu](/readme/img/features/tasting.PNG)

- As a user, I want to have anchors to different parts of the page, so that I do not have to keep scrolling.

  - [In the header, there is the navbar which jumps to all appropriate anchors](/readme/img/features/navbar.PNG)
  - [Or on mobile, having selected the three bars icon](/readme/img/features/navbar_mobile.PNG)

- As a user, I want to see information on the chef, so I know if it is a chef I am interested in.

  - [On the index page, either selected "about" in the navbar, or having scrolled](/readme/img/features/about.PNG)

- As a user, I want to see reviews of the restaurant, so that others' experiences may influence my decision.

  - [On the index page, either selected "Reviews" in the navbar, or having scrolled](/readme/img/features/index_reviews.PNG)

- As a user, I want to see contact information for the restaurant, so that I may call with a special request.

  - [On any page, at the bottom in the footer, or in the Maps section](/readme/img/features/footer.PNG)

- As a user, I wish to see an address and a map, so I can ensure I am heading to the right place.

  - [On the index page, either selected "Find Us" in the navbar, or having scrolled](/readme/img/features/map.PNG)

- As a user, I want to be able to create an account, so that I may manage my bookings and reviews.

  - [Having selected Login, the user will be presented with the Okta login screen](/readme/img/features/okta.PNG)

- As a user, I want to be able to make a reservation, so that I may visit the restaurant for a meal.

  - [Once logged in, the user may create a reservation from the dashboard after pressing the make a reservation button](/readme/img/features/reservation.PNG)

- As a user, I want to be able to leave a review, so that I may let other people know my opinion of my meal.

  - [Once logged in, the user may create a review from the dashboard after pressing the leave a review button](/readme/img/features/review.PNG)

- As a user, I want to be able to edit my reservation, in case circumstances change.

  - [Once logged in, the user may edit a reservation from the dashboard after pressing the Edit this Booking button on the appropriate card.](/readme/img/features/reservation_edit.PNG)

- As a user, I want to be able to cancel my reservation, in case I am no longer able to, or wanting, to attend.

  - [Once logged in, the user may cancel a reservation from the dashboard after pressing the Cancel this Booking button on the appropriate card. A modal will appear to ensure they want to do this.](/readme/img/features/reservation_cancel.PNG)

- As a user, I want to be able to edit my review, in case I have changed my opinion of the restaurant.

  - [Once logged in, the user may edit a reservation from the dashboard after pressing the Edit this Booking button on the appropriate card.](/readme/img/features/review_edit.PNG)

- As a user, I want to be able to cancel my review, in case I have changed my opinion of the restaurant.

  - [Once logged in, the user may delete a review from the dashboard after pressing the Delete this Review button on the appropriate card. A modal will appear to ensure they want to do this.](/readme/img/features/review_delete.PNG)

- As a site owner, I wish to see all the reservations that have been made, so that I know which bookings to prepare for.

  - [Once logged in, on the admin account, the admin may see all the reservations that have been made.](/readme/img/features/dashboard_admin.PNG)

- As a site owner, I wish to see all the reviews that have been made, so that I know what people think of my restaurant.

  - [Once logged in, on the admin account, the admin may see all the reviews that have been made.](/readme/img/features/dashboard_admin.PNG)

- As a site owner, I want the reservations that would have occurred deleted, so that I do not have clutter from expired reservations.

  - [Whenever the index page is called, the mongodb collection checks today's date versus the date of each reservation, and if it is less than today, it is deleted from the collection.](/readme/img/features/reservation_expired.PNG)

# Features

## **Existing Features**

- [The ability to see information on the chef](/readme/img/features/about.PNG)

- [Toggle to view the express menu](/readme/img/features/express.PNG)

- [Toggle to view the tasting menu](/readme/img/features/tasting.PNG)

- [Three randomly selected reviews from the mongodb collection](/readme/img/features/index_reviews.PNG)

- [Google Maps Api with the restaurant's location](/readme/img/features/map.PNG)

- [Navbar with anchors to all sections, and a link to login](/readme/img/features/navbar.PNG)

- [A navbar for mobile resolutions](/readme/img/features/navbar_mobile.PNG)

- [Footer with contact info and social media links](/readme/img/features/footer.PNG)

- [User Dashboard appearance](/readme/img/features/dashboard.PNG)

- [Admin Dashboard appearance](/readme/img/features/dashboard_admin.PNG)

- [Okta Login Screen](/readme/img/features/okta.PNG)

- [Ability to create a reservation](/readme/img/features/reservation.PNG)

- [Ability to edit a reservation](/readme/img/features/reservation_edit.PNG)

- [Ability to cancel a reservation](/readme/img/features/reservation_cancel.PNG)

- [Ability to create a review](/readme/img/features/review.PNG)

- [Ability to edit a review](/readme/img/features/review_edit.PNG)

- [Ability to delete a review](/readme/img/features/review_delete.PNG)

## MongoDB

My [MongoDB Cluster](/readme/img/mongodb/mongo_cluster.png) is titled pigGinnel, and is composed of the database ginnelPig. Within that, there are two collections. 

[Reservations](/readme/img/mongodb/mongo_reservation.png) is the first of these. The user info is all taken from g.user, from Okta. All information provided during account creation. The Email is used to identify the users' reservations, so only their own are displayed, and also, when trying to edit a reservation a user must be logged in. If that is the case, the signed in users' email must match the email of the reservation being editted, otherwise the user is taken to an empty page with a button to return the user to the homepage. There are two dates, though the user only submits one. When the user selects a date for the reservation, it is submitted as dd/mmm/yyyy. This is assigned to shown_date, and is then also displayed in this format when the user views their reservations. Slices are taken from this, and moved around to submit a second date in the format YYYYmmdd. The reason for this is to make it easier to sort by reservation date, rather than creation date. Further to this, whenever the index page is called, by any user, any reservation that would already have occurred (ie, < today's date), is deleted from the collection to avoid cluttering and manual deletion. When a user attempts to submit a reservation, the application first checks how many covers (expected guests) already exist for that specific date and specific time slot. With that integer, the application adds the integer entered by the user. If the existing covers, and the new covers < 30 (the max capacity for this fictional restaurant), then the reservation is added to the collection. If it would exceed 30, it is not added, and the user is displayed with a message saying that slot only has "x" amount of spaces left. 

[Reviews](/readme/img/mongodb/mongo_reviews.png) is the second of these. As before, user info is all taken from g.user, and the email is used to match the displayed reviews to the right user, as well as used to ensure only the creator of the review is able to edit the review. There is no extra work required by the application in terms of submitting the reviews. 
## Okta

Through Okta, I have used OpenID Connect for User management for this app. The reason for this is that overtime, and as requirements change, libraries like flask-login can be difficult to maintain. Through the use of Okta, I myself am not in charge of collecting and storing the users' information, but it is all secured by Okta, and in turn, the security of this system is better than that of a management system created by myself. 

If I had implemented my own database for user management, users would be expected to remember another set of passwords, whereas with Okta, users can use the same login details on any other application that uses Okta. Whilst Okta is not a universely used system, it still has the potential to reduce how many usernames and passwords a user has to keep track of. 

One feature that has not been included into my application, is the ability for the admin to send emails to the user. This is because if this application were to be public, and for a real business, then it would be expected that the site owner would also be paying to use Okta professionally (which I currently am not). With the premium features, the site owner can send emails to either select users, or to all users, and can create templates for different purposes, such as when a reservation is made. 

Other benefits to using Okta is that, from the Okta Application Dashboard, the Site Owner, can see [data](/readme/img/okta/okta_stats.png), including total users, failed login attempts, authentications, etc. They can also see which specific users have logged in, as shown [in the logins tab](/readme/img/okta/okta_logins.png). The site owner also has the ability to edit information about the [users themselves](/readme/img/okta/okta_users.png), and can assign them to different groups or provide different priviledges. 

### Known Bug 
One of the known bugs with Okta is that if the user clicks the login/make reservation button, it takes the user to the [Okta Sign in widget](/readme/img/okta/okta_widget.png), from this point, if the user were to to intend to return to the previous screen without logging in, they must quickly press the return button several times, otherwise they can become stuck on the page. If they don't do this, they must enter a url themselves. 

The way to fix this would be, if this site were published professionally, the site owner would have a custom url with the rights to that url. If a site owner has the rights to a url, through the Okta dashboard, they can [customise sign in](/readme/img/okta/okta_signin.png), however at this stage, that cannot be rectified. 

# Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

  - Semantic markup language as the shell of the site.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

  - Cascading Style Sheets as the design of the site.

- [JS](https://en.wikipedia.org/wiki/JavaScripts)

  - JavaScript used to enable interactivity of the webpages.

- [jQuery-ui](https://jqueryui.com)

  - Used for the datepicker function.

- [Font Awesome 5](https://fontawesome.com)

  - Used for all the social media icons, and the three bars for the navbar on mobile resolutions.

- [UIKit](https://getuikit.com)

  - Lightweight modular framework used for the clean design of the website.

- [Google Fonts](https://fonts.google.com)

  - Fonts used; "Permanent Marker", "Indie Flower", "Raleway"

- [Visual Studio Code](https://code.visualstudio.com)

  - All code for this project was written in VS Code.

- [Git](https://git-scm.com)

  - Git was used for version-control and for pushing through to my Github Repo.

- [Heroku](https://www.heroku.com/)

  - Heroku was used for deployment of my live website.

- [MongoDB](https://www.mongodb.com)

  - NoSQL database management used for management of reservations and reviews.

- [Photoshop](https://www.adobe.com/uk/products/photoshop.html)
  - Used to edit the images.

# Testing

Further information on all the steps taken for testing this website can be found in the [testing.md file](testing.md).

# Deployment

This project is currently deployed to [Heroku](https://www.heroku.com/) and is available to view [here](http://pigginnel.herokuapp.com)

To run the project locally:

- Click the green Clone or Download button on the [Github Repository](https://github.com/P0shJosh/pigginnel)

- Using the Clone with HTTPS option, copy the link displayed.

- Open your IDE, and ensure the Git Terminal is open.

- Change the working directory to the location where the cloned directory is to go.

- Use the "git clone" command and paste the url copied in the second step.

- You will need to create an env.py, which should be added to your .gitignore, with the following: 

```
import os

os.environ.setdefault("IP", "127.0.0.1")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "{string}"")
os.environ.setdefault("MONGO_URI", "{string}"") 
os.environ.setdefault("MONGO_DBNAME", "{string}"")
os.environ.setdefault("AUTH_TOKEN",
                      "{string}"")
os.environ.setdefault("ADMIN", "the email address of your admin")
```
In order to connect to [MongoDB](https://www.mongodb.com): 

- Create a free account on [MongoDB](https://www.mongodb.com)

- Create a database titled "ginnelPig"

- Within that, you need to create the collection "reservations" 

```
_id: <ObjectId>
firstName: <string>
lastName: <string>
email: <string>
date: <integer>
shown_date: <string>
slot: <string>
covers: <string>
requirements: <string>
```
- You also need to create the collection "reviews" 
```
_id: <ObjectId>
firstName: <string>
lastName: <string>
email: <string>
date: <string>
stars: <string>
review: <string>
```

To use Okta for user management, you will need to follow the instructions outlined in this guide by [Randall Degges](https://developer.okta.com/blog/2018/07/12/flask-tutorial-simple-user-registration-and-login). However, any time it mentions "localhost:5000", replace with "127.0.0.1:5000", and also, add a second link each time, with your deployed heroku app link created in the next steps. Importantly, you will need to create the OpenID Connect Config File, titled client_secrets.json. 

In order to deploy to [Heroku](https://www.heroku.com/):
 
- In your terminal, type ```pip freeze > requirements.txt```

- In your Procfile, add ```web: gunicorn app:app```

- On [Heroku](https://www.heroku.com/), create an account, and then create a new app. 

- In the settings, you will need to set the follow [Config Vars](/readme/img/features/okta.PNG)
  - Some of these details will be found on your Okta Dev Console. 

- If you have pushed to github, remove env.py from your gitignore to allow heroku to use the variables.

- Finally, after creating some commits, you can type the following in your terminal: 
  - ```heroku login```
  - ```heroku git:remote -a {your-project-name}```
  - ```git push heroku master:master```

In run.py, you will need to find and edit the following to your own details: 
```
okta_client = UsersClient("{your Okta base_url}",
                          os.environ.get("AUTH_TOKEN"))
```
```
logout_request = ("{your Okta base_url}/oauth2/default/v1/"
                      f"logout?id_token_hint={id_token}&post_logout_redirect_"
                      "uri={your heroku link}") 
```
# Credits

## Content
- [Okta](https://developer.okta.com/blog/2018/07/12/flask-tutorial-simple-user-registration-and-login), for the tutorial on integrating Okta into my flask application.

- [Roots](https://www.rootsyork.com), all the text for the menu, and even the menu itself (with the exception of a few of the drinks choices).

- [James Martin Chef](https://www.jamesmartinchef.co.uk), provided the content used for the "About" section, with the wording on Pig in a Ginnel being created by myself.

## Media
- [British GQ](https://media.gq-magazine.co.uk/photos/5d13a7ef3bedf23a51db7b61/16:9/w_1920,c_limit/james-martin-hp-gq-28feb19_b.jpg), for the image of James Martin used in the "About" section. 

- [Fenchurch Restaurant, Sky Garden London](https://skygarden.london/wp-content/uploads/2019/10/untitled-23-of-47-e1579528528296-3840x2160.jpg), for the image used as the hero image. 

- [Black Star PNG](https://icon2.cleanpng.com/20171220/ofw/star-png-image-5a3a7e9651e390.02167008151378293433541614.jpg), then editted in photoshop to multiply the stars. 

## Inspiration

- [Frog by Adam Handling](https://www.frogbyadamhandling.com), the real world inspiration for the location of this fictional restaurant.

- [Origin Coffee](https://www.origincoffee.co.uk/)

- [Kanishka Restaurant](https://kanishkarestaurant.co.uk)

- [James Martin Chef](https://www.jamesmartinchef.co.uk)

## Acknowledgements

- To [Austin](https://github.com/Austin-Ray), thanks for all your answers and explanations, and guiding me towards best practice.

- To [Tim](https://github.com/TravelTimN), for your support on getting my date system to work, and explaining RegEx to me.

- To [Precious](https://github.com/precious-ijege), my mentor for this. As always, your advice really helped, and you made sure I made the right calls.
