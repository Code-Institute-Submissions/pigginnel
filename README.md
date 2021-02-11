# [MS3 - Pig in a Ginnel](http://pigginnel.herokuapp.com)

- [Introduction](#introduction)
- [UX](#ux)
  - [The Design](#the-design)
  - [Wireframes](#wireframes)
  - [User-stories](#user-stories)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
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

## The Design

[UiKit](https://getuikit.com)


## [Wireframes](/wireframes/)

[Adobe XD](https://www.adobe.com/uk/products/xd.html) was used to create the initial wireframes, the pdf file with all the wireframes can be viewed in []().


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

- [Photoshop](https://www.adobe.com/uk/products/photoshop.html)
  - Used to edit all images related to Dice and the results for the Star Wars rolls, as well as the DiceRoll logo from red to purple.

# Testing

Further information on all the steps taken for testing this website can be found in the [testing.md file](testing.md).

# Deployment

This project is currently deployed to [Heroku](https://www.heroku.com/) and is available to view [here](http://pigginnel.herokuapp.com)

In order to deploy to [Heroku](https://www.heroku.com/):

- 

To run the project locally:

- Click the green Clone or Download button on the [Github Repository](https://github.com/P0shJosh/pigginnel)

- Using the Clone with HTTPS option, copy the link displayed.

- Open your IDE, and ensure the Git Terminal is open.

- Change the working directory to the location where the cloned directory is to go.

- Use the "git clone" command and paste the url copied in the second step.

# Credits

## Content

- [Roots](https://www.rootsyork.com), all the text for the menu, and even the menu itself (with the exception of a few of the drinks choices).

- [James Martin Chef](https://www.jamesmartinchef.co.uk), provided the content used for the "About" section, with the wording on Pig in a Ginnel being created by myself.

## Media


## Inspiration

- [Frog by Adam Handling](https://www.frogbyadamhandling.com), the real world inspiration for the location of this fictional restaurant.

- [Origin Coffee](https://www.origincoffee.co.uk/)

- [Kanishka Restaurant](https://kanishkarestaurant.co.uk)

- [James Martin Chef](https://www.jamesmartinchef.co.uk)

## Acknowledgements

- To [Austin](https://github.com/Austin-Ray), thanks for all your answers and explanations, and guiding me towards best practice.

- To [Tim](https://github.com/TravelTimN), for your support on getting my date system to work, and explaining RegEx to me.

- To [Precious](https://github.com/precious-ijege), my mentor for this. As always, your advice really helped, and you made sure I made the right calls.
