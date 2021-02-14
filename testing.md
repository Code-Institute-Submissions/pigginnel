# Testing

![Testing Excel File](/readme/testing.PNG)

## Notes on Testing 

- The [image](/readme/testing.PNG/) above of the excel file displays all my tests across different devices and browsers. 
    - Green means passed as fully intended.
    - Yellow means not entirely as intended but acceptable.
    - Red means did not render as intended.
- The steps I took to test each feature can be viewed in the [Testing each Feature](#testing-each-feature) section below.
- Chrome browser resolutions were tested with the Vivaldi browser (Chromium Based), and through the use of Chrome Developer Tools within Vivaldi. 
- Any devices listed with an asterisk were tested within Chrome Developer Tools.
- Safari was tested on a Macbook Pro 2017.

## Yellow Explained

- On internet explorer, the only issue was with the stars for the reviews. Whilst they do appear, they are slightly distorted, but still obvious as to their purpose. 

- On the galaxy fold, the reservation and review modals do appear rather small, making it hard to enter text. 

# Testing each Feature

- [Index Page](/readme/images/features/index.PNG)
    - Appeared as intended across all devices. 
    
- [About Section](/readme/img/features/about.PNG)
    - Appears beneath the hero image. On larger resolutions, two cards appear side by side, one with an image of the chef, the other with matching text/
    - On smaller resolutions, iPad Pro and below, the two cards appear stacked, with the image of the chef on top. 

- [Express Menu](/readme/img/features/express.PNG)
    - Two cards beneath the about section, side by side on larger resolutions. Left card is matching text, right card features the menu.
    - On smaller resolutions, the menu appears below the text. 
    - If the Tasting Menu had been displayed, clicking the title Express Menu will swap the visible menu to the appropriate one. 

- [Tasting Menu](/readme/img/features/tasting.PNG)
    - Two cards beneath the about section, side by side on larger resolutions. Left card is matching text, right card features the menu.
    - On smaller resolutions, the menu appears below the text. 
    - If the Express Menu had been displayed, clicking the title Tasting Menu will swap the visible menu to the appropriate one. 

- [Three Reviews](/readme/img/features/index_reviews.PNG)
    - On larger resolutions, beneath the menu, three cards appear side by side. 
    - Each contains up to 5 stars in a png, a first name, and review text.
    - On smaller resolutions, the cards stack. 

- Review Animations 
    - As the user scrolls down the page, the reviews slide in from the top. 

- [Google Maps Api](/readme/img/features/map.PNG)
    - Two cards, side by side on larger resolutions, stacked on smaller ones. 
    - One card calls the google maps api and loads a map with a location pinned, the one of the fictional restaurant. 

- [Navbar](/readme/img/features/navbar.PNG)
    - Appears at the top beneath the logo. Text should be centered. 

- [Mobile Navbar](/readme/img/features/navbar_mobile.PNG)
    - Initially hidden, when the three bars logo is pressed, the menu slides in from the right over the top of the rest of the display. 

- [Footer](/readme/img/features/footer.PNG)
    - Three sections, side by side. Link to James Martin information, contact info, and social media links. 
    - On smaller resolutions, the contact info and social media links are side by side, but beneath the James Martin Link. 

- [User Dashboard](/readme/img/features/dashboard.PNG)
    - After the user logs in, it displays Welcome User.Firstname. Beneath that a button to the external okta site to edit the user account info. 
    - Then, two columns on larger resolutions. 
    - On smaller resolutions, the two columns stack instead. 

- [Admin Dashboard](/readme/img/features/dashboard_admin.PNG)
    - After the user logs in, it displays Welcome User.Firstname.
    - Then, two columns on larger resolutions. 
    - On smaller resolutions, the two columns stack instead. 

- [Okta Login Screen](/readme/img/features/okta.PNG)
    - When the user clicks login/make a reservation, it loads an external okta widget. 
    - Widget allows the user to login, and then redirects to the dashboard. 
    - Original problem meant that when the user clicked log out, it only logged the user out of the app, but not okta itself. 
    - This was a security flaw as another user coming on could click login again and it would automatically log back in. 
    - This was solved with the extension of the logout route in run.py. 
    - Now, when the user presses logout, the user is logged out of both the app and Okta itself, allowing a fresh login when the button is pressed again. 

- [Create a Reservation](/readme/img/features/reservation.PNG)
    - Only appears on the user dashboard. 
    - Clicking the date brings up the jquery ui Datepicker. 
    - In earlier versions of the app, even with regex, the user could delete parts of the date, and cause issues for the resulting functions of run.py. 
    - This was fixed by preventing the user from editting the textbox, an unneeded feature anyway when the user just has to select the date from the datepicker ui. 
    - On the covers, users could originally add text rather than integers, changed that to improve functionality. 

- [Edit a Reservation](/readme/img/features/reservation_edit.PNG)
    - Only appears on the user dashboard.
    - Featured the same issues as create a reservation, until the same fixes were introduced.

- [Cancel a Reservation](/readme/img/features/reservation_cancel.PNG)
    - Appears on both dashboards. 
    - This is in case for some reason the admin has the need to cancel a review. 
    - This may be because the user cannot access the app themselves for some reason and so have contacted the adin. 
    - It may also be due to the fact the restaurant has closed, and so reservations need cancelling. 
    - If this does occur, it is up to the admin to inform the users that the reservations have been cancelled. This would require the use of the Okta Dashboard - functionality currently not present. 

- [Create a Review](/readme/img/features/review.PNG)
    - Appears only on the user dashboard.
    - Features a slider for the user to select how many stars they want to give the restaurant. 
    - Also a textarea which has a minimum text requirement to fill in. 

- [Edit a Review](/readme/img/features/review_edit.PNG)
    - Also only appears on the user dashboard. 
    - Same features as the create a review. 

- [Delete a Review](/readme/img/features/review_delete.PNG)
    - Features on both dashboards. 
    - The reasons for the admin having this feature are similar as to the reservations, however also in case a review is inappropriate. 
    - Regex for all things that wouldn't be allowed would be too complex to introduce, it made more sense for an admin to moderate the reviews present on the website. 


# Testing the User-stories

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

# Validation Testing

- HTML has been validated using [W3C HTML Validator](https://validator.w3.org/nu/) 

- CSS has been validated using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) 

- JS has been validated using [JSHint](https://jshint.com)
    - The line /*jshint esversion: 6 */ was added to the start each file for testing purposes. 

- Python has been checked for PEP8 compliance using [PEP8](http://pep8online.com)

## Validation Testing Results 

![HTML validation](/readme/images/validation/html.png)

- [Messages filtered were ones to do with UiKit](/readme/img/validation/message_filtering.png)

![CSS validation](/readme/images/validation/css.png)


![JS validation](/readme/images/validation/js.png)


![PEP8 validation](/readme/images/validation/pep8.png)


