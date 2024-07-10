# The Happy Florist



View the live site [here](https://the-happy-florist-5c44ce792179.herokuapp.com/)



![screenshot of the live site](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/main-updated.png?raw=true)



## Contents



* [Purpose](#purpose)

* [User Experience](#user-experience)

   * [Project Goals](#project-goals)

   * [User Stories](#user-stories)

   * [Wireframes](#wireframes)

   * [ERD](#erd)

   * [Color Scheme and Typography](#color-scheme)

* [Features](#features)

   * [Existing Features](#existing-features)

      * [Navbar](#navbar)

      * [Homepage](#the-main-menu)

      * [The Search Bar](#the-search-bar)

      * [User Login/Sign up](#user-login)

      * [Free Delivery for Members](#free-delivery)

      * [About Us](#about-us)

      * [Custom Products](#custom-products)

      * [Newsletter Sign up](#newsletter)

      * [Product List](#product-list)

      * [Product Details](#product-details)

      * [Product Management – Admin](#product-admin)

      * [Events](#events)

      * [Events Gallery](#gallery)

      * [Events Management – Admin](#events-admin)

      * [Order Confirmation](#order-confirmation)

      * [Add to Wishlist](#wishlist)

      * [Reviews](#reviews)

   * [Future Features](#future-features)

* [Marketing Strategies](#marketing-strategies)

   * [Overview](#overview)

   * [Key Marketing Strategies](#key-strategies)

   * [Meta Tags for SEO](#meta-tags)

   * [Facebook Page](#facebook)

   * [Newsletter](#newsletter)

* [Technologies Used](#technologies-used)

* [Testing](#testing)

     * [Lighthouse Testing](#lighthouse-testing)

     * [Manual Testing](#manual-testing)

     * [Unfixed Bugs](#unfixed-bugs)

* [Deployment](#deployment)

   * [Deploying the App](#deploying-the-app)

   * [Forking The Repository](#forking-the-repository)

   * [Cloning The Repository](#cloning-the-repository)

   * [Heroku](#heroku)

* [Credits](#credits)



## Purpose



This Django e-commerce site is for a mock florist business that sells online and instore. The site allows the user to navigate through pages to view products as well as view events created by the business admin and view events galleries.



This program is developed to demonstrate competency in python, django, javascript, sql, APIs and is purely for educational purposes.



## User Experience



### Project Goals



As the site owner, I want the program to:

* Provide information on products for sale on the website.

* Be easy to navigate.

* Allow a user to create a log in and profile.

* Allow signed in users to receive free delivery.

* Allow the user to search for a product by keyword, rating, price or category.



### User Stories



All user stories are available to view [here](https://github.com/users/DaniCarmo/projects/3) on Github.

![screenshot of user stories](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/issues-user-stories.png?raw=true)


![screenshot of kanban](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/kanban.png?raw=true)



### Wireframes


Wireframes were created on Miro, example below and all designs available to view [here](https://github.com/DaniCarmo/Florist-p5/tree/main/static/testing/wireframes)

The homepage wireframe looks slightly different as a last minute change was made to have 1 call to action box instead of 2, and add in the custome product piece.


![screenshot of wireframe](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/wireframes/wireframe.png?raw=true)



### ERD


#### Relationships

* A User can have multiple Orders.
* A User can write multiple Reviews.
* A User can have multiple Wishlist items.
* A User can have one Cart.
* An Order can have multiple OrderItems.
* A Product can belong to one Category.
* A Category can have multiple Products.
* A Product can have multiple Reviews.
* A Product can have multiple Wishlist entries.


ERD shown below created with [dbdiagram](https://dbdiagram.io/):

![screenshot of erd](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/wireframes/ERD.png?raw=true)



### Color Scheme & Typography



The colors mainly revolve around the background image consisting of pastel greens, reds and yellow. These colors compliment each other and give the site an earthy and elegant tone which is in keeping with the vibe of a florist shop. The header and footer are a shade of pastel green taken from the background image and the home image of the outside of a florist also reflects these floral and earthy tones. The pastel green is used throughout the site, and the dark text and buttons serve as a nice contrast.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/background-img.png?raw=true)



The fonts used throughout the site are Quicksand and Dancing Script. The first being used for the main home page banner texts as a call to action, as well as the about us section and product details text. While the more fluid and fun Dancing Script is used for the site name and headings. These fonts provided a great contrast for the user to identify sections and work well together, as both are rounded in nature and have similar weight. Quicksand is more uniform while Dancing Script is reminiscent of florals and floats across the page.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/fonts.png?raw=true)



## Features



### Existing Features



#### Navbar



Allows user to navigate through the site and also exapnds on smaller devices for better ux design.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/navbar-updated.png?raw=true)



![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/navbar-collapsed.png?raw=true)


The expanded and collapsed navbars also have dropdown menues:

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/navbar-options.png?raw=true)



![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/navbar-collapsed-menu.png?raw=true)



#### Homepage



The landing page with a call to action and a refreshing floral backgorund image.



![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/homepage-updated.png?raw=true)



#### Search Bar



For users to search by word or feature.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/searchbar.png?raw=true)



#### User Login/Sign Up



Django Allauth register page, allows users to make an account.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/signup.png?raw=true)



![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/login.png?raw=true)


All users signing up for an account will receive a verification link to confirm their email for security purposes, screenshot below shows email received in to test email account:

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/email-verification.png?raw=true)


![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/emails-received.png?raw=true)



#### Free Delivery for Members

Users with an account can avail of free delivery on all orders, no min price, to encourage site users to sign up and create an account.


Screenshot below shows user without account/not logged in and has a 10% delivery charge applied:


![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/no-free-delivery.png?raw=true)



Screenshot below shows user who is logged in to their account and has no delivery fee applied:


![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/user-free-delivery.png?raw=true)



#### About Us – Staff


Section for users to get an insight in to the business and recognise the faces of staff to provide a more friendly user experience.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/about.png?raw=true)



#### Custom Products


Section to advise users that all products can be customised to suit their design requirements, with a link to get a quote that leads the user to the Facebook page where they can message us.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/custom-products.png?raw=true)



#### Newsletter Sign up



Users can subscribe to The Happy Florist's newsletter to stay up to date with news, events and offers.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/footer.png?raw=true)


The sign up form also contains error and success messages for user:

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/newsletter-success.png?raw=true)


![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/newsletter-error.png?raw=true)



#### Products List



This page has many versions based on user searches and sorting parameters. Users can see available products sorted here with image, product name, price, and average rating.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/products-list.png?raw=true)



 #### Product Details



Here users can view a specific product details and pricing. This will give a full review of the product, and the user can also select sizes for flower bouquets. The default price and size is set to ‘Medium’ bouquet sizes, and when the user selects ‘Small’ or ‘Large’ from the dropdown then the price automatically updates to reflect size. For other products such as balloons and sweets, there is one set price.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/products-detail2.png?raw=true)


![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/products-detail.png?raw=true)


And if user is logged in they will see the add to wishlist option:

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/product-detail-wishlist.png?raw=true)



#### Product Management – Admin



Here staff and super users can add new products and set all elements of the products.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/admin-delete-edit.png?raw=true)


![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/add-product.png?raw=true)



#### Events



The events page allows users to view upcoming events on the events dashboard and click to register for an event.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/fonts.png?raw=true)



#### Events Gallery



Users can view past events via the gallery carousel on the events page, to get a  feel for what the events may be like.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/gallery.png?raw=true)



#### Events Management – Admin



The site admin/staff can log in here to add, delete or update and event.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/admin-events.png?raw=true)


![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/event-added.png?raw=true)


#### Order Confirmation

Users are brought to a confirmation page to confirm their order has been placed successfully, as well as receining a confirmation email.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/order-success.png?raw=true)


![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/order-email.png?raw=true)



#### Add to Wishlist

The add to wishlist function allows user to click search a dropdown and add a product to a wishlist, this list is then stored and can be accessed under the user login under "Wishlist". These items can also be edited and deleted.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/wishlist-product.png?raw=true)


The user can select products from a dropdown to add to their wishlist (if they are logged in):

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/wishlist.png?raw=true)


And users can view their wishlist:

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/my-wishlist.png?raw=true)



#### Reviews

The reviews page allows user to view all reviews created for products, as well as search by keywords for a specific product. Users can add a review from their profile page and the admin can also delete reviews if they wish.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/reviews.png?raw=true)



### Future Features



Features to be implemented may include:

* Allowing logged in users to rate products

* Create a user-friendly event sign up page, where user can enter their details and chose events from a dropdown schedule and they will receive a confirmation email invite so it will sync up with their personal calendars on their phone, PC, etc.

* Build a mailing list to send regular newsletters via mailchimp.

* More social media features to encourage a larger online presence and support, such as an Instagram and Twitter as well as a YouTube chanel to show events and demonstrations.



## Marketing


### Overview
The Happy Florist aims to connect directly with consumers who value fresh, hbeautifully arranged, and locally sourced flowers and other products. To achieve this, our marketing strategy focuses on building a strong online presence, engaging with our audience through various digital channels, and leveraging the power of social media.


### Key Marketing Strategies

  1. **Social Media Engagement via Facebook:** Create and maintain an active Facebook page where we share updates, promotions, and engaging content such as classes and events related to flower arrangment and coffee mornings, and sneak peeks of the behind-the-scenes of running a busy florist. Encourage customer interactions through comments, reviews, and sharing user-generated content.
    
  2. **Content Marketing:** Develop an events page on our website featuring events and a gallery of past events and classes, and sharing these posts across social media platforms to drive traffic to our site.

  3. **Email Marketing:** Build a mailing list to send regular newsletters with exclusive offers, new product announcements, and personalized recommendations. Include visually appealing content and incentives for subscribers to make repeat purchases.

  4. **SEO and Paid Advertising:** Optimize our website with targeted keywords and meta tags to improve search engine rankings and increase organic traffic. Implement Google Ads and Facebook Ads to target potential customers based on their interests and online behavior.


### Meta Tags for SEO
```html
  <meta name="keywords" content="County Kerry, Ireland, SouhtWest, florist, flower arrangement, weddings, events, anniversary, celebration, floral design, flower delivery, floral gifts, bridal flowers, special occasions, floral decor, flower shop, local florist, flower arrangements for events, flower bouquets, floral centerpieces, floral decorations, wedding flowers, floral arrangements for weddings">
  ```


### Facebook Page

[The Happy Florist FB Page](https://www.facebook.com/profile.php?id=61560638586222)

![Facebook Page](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/Screenshot%20FB.png?raw=true)


### Newsletter
Using integration with [Mailchimp](https://mailchimp.com/?currency=EUR).



## Technologies used



* [Bootstrap](https://www.bootstrapcdn.com/)

   * For adding responsive styling to the site.

* [Python](https://www.python.org/)

   * Used to provide functionality to the site.

* [Visual Studios](https://visualstudio.microsoft.com/vs/community/)

   * Used to create the code and content for the repository.

* [Github](https://github.com/)

   * Used to host the repository.

* [Miro](https://miro.com/app/dashboard/)

   * To create the wireframes and design at planning stage.

* [Amazon Web Services](https://dashboard.heroku.com/apps).

   * Used to host the static files.

* [Heroku](https://dashboard.heroku.com/apps).

   * Used to host the website and used Heroku Postgres to attach database.



## Testing



The site pages have been tested on various screen sizes to ensure that the content is responsive and all screenshots can be viewed [here](https://github.com/DaniCarmo/Florist-p5/tree/main/static/testing)

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/responsive-sizes.png?raw=true)



The code has been tested using:

[W3 HTML validator](https://validator.w3.org/) - A few minor error were flagged related to how the tool reads repeated templates and structure from the Boutique Ado walkthrough project where this project is based on. Throughout manual testing, it was identified these minor error have no impact when running e-commerce application.


[W3 CSS validator](https://jigsaw.w3.org/css-validator/) - no errors


[jshint](https://jshint.com/) - no errors


[CI Python Linter](https://pep8ci.herokuapp.com/) - a few minor warnings due to whitespace and lines too long, but nothing that affected the site itself or the functionality.



The code was also checked throughout the project where errors showed up on Visual Studios and these were fixed as they arose, as well as ongoing debugging in Chrome Developer Tools, Stack Overflow, Django documentation, W3Schools and Chat GBT.



### Lighthouse Performance



Below are screenshots fromm Goofle's lighthouse testing showing performance levels of the site pages.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/lighthouse-home-updated.png?raw=true)


![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/lighthouse-products.png?raw=true)


![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/lighthouse-product-detail.png?raw=true)


![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/lighthouse-events.png?raw=true)



### Manual Testing



Ran each test mentioned in the table below multiple times and each action executes as intended, providing confirmation of successful user story requirements and actions.


| Test                                                        | Action                                                                                                                                        | Expectation                                                                                                                                                                              | Result     |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| Navigate to the website's homepage                          | Click on logo or on Home on navbar                                                                                                            | User is directed to home page                                                                                                                                                            | Successful |
| Navigate to all products page                               | Click on All Products on navbar and from dropdown chose All Products                                                                          | User is directed to the list of All Products                                                                                                                                             | Successful |
| Navigate to all products page - sort by rating              | Click on All Products on navbar and from dropdown chose By Rating                                                                             | User is directed to the list of All Products sorted by rating highest to lowest                                                                                                          | Successful |
| Navigate to flowers page                                    | Click on Flowers on navbar and from dropdown chose All Products                                                                               | User is directed to the list of All Flower Products                                                                                                                                      | Successful |
| Navigate to balloons page - sorted by price                 | Click on Balloons on navbar and from dropdown chose By Price                                                                                  | User is directed to the list of all balloon products sorted by price lowest to highest                                                                                                   | Successful |
| Navigate to profile page                                    | Only logged in users can see their profile page and a Profile option on nav bar; click on Profile on the nav bar.                             | Logged in users are brough to their profile page, and user is brought to their profile page                                                                                              | Successful |
| Sign-up/Register                                            | Click on Register on nav bar                                                                                                                  | User is directed to sign-up page                                                                                                                                                         | Successful |
| Login                                                       | Click on Login on nav bar                                                                                                                     | User is directed to sign-in/login page                                                                                                                                                   | Successful |
| Edit or Delete a product - admin                            | As a site admin I can see the edit/delete options on each product and click to edit/delete to update the product                              | Admin can edit or delete a product                                                                                                                                                       | Successful |
| Edit or Delete a product - as user but not admin            | As a logged in user I click on a product to view                                                                                              | No option to edit or delete product                                                                                                                                                      | Successful |
| Edit or Delete a product - not logged in to account/profile | As a site user with no account I click on a product to view                                                                                   | No option to edit or delete product                                                                                                                                                      | Successful |
| Add product - admin                                         | As a site admin I can see the Product Management option on the navbar                                                                         | Admin can see option to add a product                                                                                                                                                    | Successful |
| Add product - not admin                                     | As a site user I click on my profile options and search on navbar for option to add a new product                                             | No option to add a product                                                                                                                                                               | Successful |
| Logout                                                      | As a logged in user I click on Logout on the nav bar and then confirm sign out                                                                | Logout option appears when clicked on nav bar and warning shows to confirm if user wants to log out or not, user then proceeds and is logged out of their account                        | Successful |
| Edit Profile                                                | As a logged in user I click on my Profile and go to Edit                                                                                      | When the Edit button is clicked a modal will appear within the Profile page where user can update their profile - they can add bio information and/or upload a profile picture           | Successful |
| Forgot password                                             | Click on forgot password link in sign in page                                                                                                 | user is brought to the password reset option where they can enter email address - an email is sent to user to folllow password reset link and enter new password                         | Successful |
| Product detail                                              | Click on a product card on products list page to view the product in more detail and view options                                             | Full product page is brought up with details and options showing to add to cart or continue shopping                                                                                     | Successful |
| Product detail - with sizes                                 | Click on a product card on products list page to view the product in more detail and view sizing and oricing options - update size to S and L | Dropdown option available to user to select S, M or L and price will update accordingly. The default size and price is for the Medium bouquet size                                       | Successful |
| Product detail - no sizes to chose from                     | Click on a product card on products list page to view the product in more detail and view options                                             | No option to update sizes available                                                                                                                                                      | Successful |
| Search Bar                                                  | Add "happy" to search bar and click search.                                                                                                   | All products with "happy" in description appear for me to view                                                                                                                           | Successful |
| Search Bar                                                  | Add "chocolates" to search bar and click search.                                                                                              | All products with "chocolates" in description appear for me to view                                                                                                                      | Successful |
| Events page                                                 | As site user I navigate to events from the navbar                                                                                             | As site user I navigate to events from the navbar and brought to the events page                                                                                                         | Successful |
| Event details - admin                                       | As admin I navigate to the events page and click on the add.edit and delete buttons                                                           | Admin can click on add event and be brought to the event scheduling page to add an event, or can edit/delete current events from the events page                                         | Successful |
| Event details - not admin                                   | As a site user I navigate to the events page                                                                                                  | No options available to add, edit or delete an event                                                                                                                                     | Successful |
| Product details page - Cart                                 | As site user I click add to cart to add a balloon product to cart                                                                             | product added to cart and successful toast appears                                                                                                                                       | Successful |
| Product details page - Quantity                             | As a site user I click on the plus sign to add additional products to my cart                                                                 | multiples of the selected product added to cart                                                                                                                                          | Successful |
| Navbar - shopping cart                                      | Click the cart icon on navbar                                                                                                                 | click on the cart and brought to shopping cart page with option to checkout                                                                                                              | Successful |
| Shopping cart - view                                        | Navigate to shopping cart page                                                                                                                | can view all added products with image, price, quantity selected, subtotal for each product, a total of all products and options to continue shopping or checkout                        | Successful |
| Shopping cart - add-remove items                            | Within the shopping cart page click on the minus/plus boxes to add or reduce product quantity                                                 | Product quantity feature will work and allow user to add/remove multiples of a product                                                                                                   | Successful |
| Shopping cart - update cart                                 | Within the shopping cart page click on the minus/plus boxes to add or reduce product quantity and then click on Update                        | After updating, the subtotal and total will update according to the current quantitiy of the product in the cart                                                                         | Successful |
| Shopping cart - remove product                              | Within the shopping cart page click on Remove under the quantity box of an item                                                               | The entire product (whether singular or multiple) will be deleted and removed form the cart, cart page will refresh and the removed product will no longer show, prices will also update | Successful |
| Checkout                                                    | click on checkout from the shopping cart page                                                                                                 | User is brought to the checkout page where there shopping cart items are carried over and are presented with option to add checkout personal and card details                            | Successful |
| Checkout - stripe form                                      | complete the checkout form and submit with all correct details - click on complete order button                                               | user enters info, clicks on complete order and form submits successfully and user gets success message                                                                                   | Successful |
| Checkout - stripe form - incorrect info                     | complete the checkout form and submit with missing info - click on complete order button                                                      | user enters info, clicks on complete order and receives error message showing what sections are required in red                                                                          | Successful |
| Checkout confirmation page                                  | click on complete order in the shopping cart                                                                                                  | user is brought to the checkout confirmation page where they are provided with their order details                                                                                       | Successful |
| Order confirmation email                                    | complete online order successfully                                                                                                            | user receives an email from happyfloristtralee@gmail.com with order details and order confirmation                                                                                       | Successful |
| Add to wishlist                                             | Click on any product and add to wishlist                                                                                                      | Select add to wishlist and user brought to page to chose product from dropdown and can view wishlist in their list                                                                       | Successful |
| Delete from wishlist                                        | Logged in user navigates to their wishlist from dropdown nav item to see wishlist and delete item                                             | User click on wishlist from navbar dropdown and brought to their wishlist - click on delete item and item is deleted                                                                     | Successful |
| View Reviews                                                | Click on Reviews from navbar and user can view all reviews                                                                                    | Click on Reviews from navbar and user can view all reviews                                                                                                                               | Successful |
| Search Reviews                                              | On reviews page user adds keyword to searchbar and provided with relevant product reviews                                                     | In search bar on review page type in 'Balloon' - all results with balloon in the name are returned                                                                                       | Successful |
| Search Reviews                                              | On reviews page user adds keyword to searchbar and provided with relevant product reviews                                                     | In search bar on review page type in 'Meadow' - all results with meadow in the name are returned                                                                                         | Successful |
| Add a Review                                                | User navigates to their profile and scrolls down to add review                                                                                | Under user profile click on dropdown for reviews to chose the product to review, add comments in comment box and click save - review available to view on reveiews page                  | Successful |
| Admin - Delete Review                                       | Admin navigates to reviews page and selects 'Delete' on a review                                                                              | Admin navigates to reviews page and selects 'Delete' on a review - review is deleted and no longer available on the site                                                                 | Successful |


### Unfixed Bugs



There are currently no unfixed bugs recorded, however I would like to update the user reviews so that the user can see all of their submitted reviews on their profile page. Also when a user clicks 'Add to Wishlist' on the product details page, instead of being brough to the add to wishlist page with a dropdown to select a product, it would provide a better user experience if the product they were viewing can be added to the wishlist by clicking that button, instead of being brought to the dropdown page to search for the product. These are two features I would improve on given more time.



## Deployment



### Forking The Repository



This can be done to create a copy of the repository. The copy can be viewed and edited without affecting the original repository.



To fork the repository through GitHub, take the following steps:



1. In the relevant github repository, click on the "fork" tab in the top right corner.

2. Click on "create fork" to fork the repository.



### Cloning The Repository



To clone the repository through GitHub:



1. In the repository, select the "code" tab located just above the list of files and next to the GitHub button.

2. Ensure HTTPS is selected in the dropdown menu.

3. Copy the URL under HTTPS.

4. Open Git Bash in your IDE of choice.

5. Change the current working directory to the location where you want the cloned directory to be created.

6. Type "git clone" and paste the URL that was copied from the repository.

7. Press the "enter" key to create the clone.



### Heroku



**In your app** 

1. add the list of requirements by writing in the terminal "pip3 freeze --local > requirements.txt"
2. Git add and git commit the changes made

**Log into heroku**

3. Log into [Heroku](https://dashboard.heroku.com/apps) or create a new account and log in

4. top right-hand corner click "New" and choose the option Create new app, if you are a new user, the "Create new app" button will appear in the middle of the screen

5. Write app name - it has to be unique, it cannot be the same as this app
6. Choose Region - I am in Europe
7. Click "Create App"

**The page of your project opens.**

8. Go to Resources Tab, Add-ons, search and add Heroku Postgres

9. Choose "settings" from the menu on the top of the page

10. Go to section "Config Vars" and click button "Reveal Config Vars". 

11. Add the below variables to the list

    * Database_URL from  PostgresQL.  
    * Secret_Key - is the djnago secret key can be generated [here](https://miniwebtool.com/django-secret-key-generator/). 


**Go back to code**

12. Procfile needs to be created in your app
```
web: gunicorn PROJ_NAME.wsgi:application
```

13. In settings in your app add Heroku to ALLOWED_HOSTS

14. Add and commit the changes in your code and push to github

**Final step - deployment**

15. Next go to "Deploy" in the menu bar on the top 

16. Go to section "deployment method", choose "GitHub"

17. New section will appear "Connect to GitHub" - Search for the repository to connect to

18. type the name of your repository and click "search"

19. once Heroku finds your repository - click "connect"

20. Scroll down to the section "Memual Deploys"

21. Click choose "Deploy branch" and manually deploy

22. Click "Deploy branch"

Once the program runs:
you should see the message "the app was sussesfully deployed"


### Getting Stripe keys
Go to developers tab. On side menu you will find API keys. Copy STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY.

Go to Webhooks. Click Add Endpoint button in top right hand corner.
Add endpoint URL (your local or deployed URL)
Add all events 
Than click add endpoint
You should be redirected to this webhook's page. Reveal webhook sign in secret and copy to Settings and to heroku as STRIPE_WH_SECRET variable

### Getting email variables from gmail


- Log into gmail account
- Go to Settings and than See all settings
- Top menu go to Accounts and import
- Find on the list Other google account settings
- Left side menu - Security
- Turn on two step verification: add phone number and follow instructions
- Go back to security
App passwords - Select Mail, Select Device - Other, Django, Copy app password.

In Heroku 
EMAIL_HOST_PASS is the password copied from above.
EMAIL_HOST_USER is the gmail email address


### Setting AWS bucket


1. Go to [Amzon Web Services](https://aws.amazon.com/) page and login or register

2. You should be redirected to AWS Managment Console, if not click onto AWS logo in top left corner or click Services icon and choose Console Home

3. Below the header AWS Services click into All Services and find **S3** under Storage

4. Create New Bucket using **Create Bucket** button in top right hand corner

- **Configuration:** type in your chosen name for the bucket (preferably matching your heroku app name) and AWS Region closest to you


- **Object ownership:** ACLs enabled, Bucket owner preffered

- **Block Public Access settings:** Uncheck to allow public access, Acknowledge that the current settings will result that the objects within the bucket will become public

- Click **Create Bucket**

5. You are redirected to Amazon S3 with list of your buckets. Click into the name of the bucket you just created

6. Find the tab **Properties** on the top of the page:
**Static website hosting** at the bottom of the properties page: clik to edit, click enable, fill in index document: index.html and error.html for error

7. On the **Permissions** tab:
- Cross-origin resource sharing (**CORS**) Paste in the below code as configuration and save

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- **Bucket Policy** within permissions tab: Edit bucket policy
Click AWS Policy Generator (top right conrner)

Select type of policy: S3 Bucket policy
Principal: * (allows all)
Actions: Get object
Amazon Resource Name (ARN): paste from the Edit bucket policy page in permissions
Click Add statement Than Click Generate Policy and Copy the policy into bucket policy editor. 
In the policy code find "Resource" key and add "/*" after the name of the bucket to enable all
Save changes

- **Access control list (ACL)** within permissions tab: click Edit

find Everyone (public access) and check List box and save

8. Identity and Access Management (IAM)
Go back to the AWS Management Console and find IAM in AWS Services

- side menu - User Groups and click **Create Group**
name group "manage-your-app-name" and click Create group

- side menu - Policies and click **Create Policy**
Click import managed policy - find AmazonS3FullAccess
Copy ARN again and paste into "Resource" add list containint two elements "[ "arn::..", ""arn::../*]" First element is for bucket itself, second element is for all files and foldrs in the bucket

Click bottom right Add Tags, than Click bottom right Next: Review
Add name of the policy and description

Click bottom right Create policy

9. Attach policy to the group we created:
- go to User Groups on side menu
- select your group from the list
- go to permissions tab and add permissions drop down and choose **Attach policies**
- find the policy created above and click button in bottom right Add permissions

10. Create User to go in the group
- **Users** in the side menu and click add users

User name: your-app-staticfiles-user
Check option: Access key - Programmatic access
Click button at the bottom right for Next
- Add user group and add user to the group you created earlier
Click Next Tags and Next: review and Create user
- Download .csv file

11. Connect django to AWS S3 bucket
- install boto3
- install django-storages
- freeze to requirements.txt
- add storages to installed apps in settings.py

```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'mahir-store'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```

12. Go to heroku to set up enviromental variables

open CSV file downloaded earlier and copy each variable into heroku Settings

AWS_STORAGE_BUCKET_NAME
AWS_ACCESS_KEY_ID from csv
AWS_SECRET_ACCESS_KEY from csv
USE_AWS = True
remove DISABLE_COLLECTSTATIC variable from heroku

13. Create file in root directory custom_storages.py

```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

14. Go to settings.py, add the AWS settings

```
     # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

```

15. To load the media files to S3 bucket

- Go to your S3 bucket page on AWS. Create new folder "media"
- go to the media folder and click Upload


## Credits


* Used the Code Institute’s P5 sample project, Boutique Ado, as a guide and basic template for the site.

* Followed tips and troubleshooting throughout the project on Stackoverflow [stackoverflow](https://stackoverflow.blog/), Python.org [python-org](https://www.python.org/) and w3Schools[w3schools](https://www.w3schools.com/).

* Got the site and product images from Pexels [Pexels](https://www.pexels.com/).

* I used ChatGBT [chat-gbt](https://chat.openai.com/) to assist with coming up with the ‘about us’ and product descriptions.