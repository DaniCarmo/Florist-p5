# The Happy Florist



View the live site [here](https://the-happy-florist-5c44ce792179.herokuapp.com/)



![screenshot of the live site](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/Main.png?raw=true)



## Contents



* [Purpose](#purpose)

* [User Experience](#user-experience)

   * [Project Goals](#project-goals)

   * [User Stories](#user-stories)

   * [Wireframes](#wireframes)

   * [Color Scheme and Typography](#color-scheme)

* [Features](#features)

   * [Existing Features](#existing-features)

      * [Navbar](#navbar)

      * [Homepage](#the-main-menu)

      * [The Search Bar](#the-search-bar)

      * [User Login/Sign up](#user-login)

      * [Free Delivery for Members](#free-delivery)

      * [About Us](#about-us)

      * [Newsletter Sign up](#newsletter)

      * [Product List](#product-list)

      * [Product Details](#product-details)

      * [Product Management – Admin](#product-admin)

      * [Events](#events)

      * [Events Gallery](#gallery)

      * [Events Management – Admin](#events-admin)

      * [Order Confirmation](#order-confirmation)

      * [Add to Wishlist](#wishlist)

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


![screenshot of wireframe](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/wireframes/wireframe.png?raw=true)



### Color Scheme & Typography



The colors mainly revolve around the background image consisting of pastel greens, reds and yellow. These colors compliment each other and give the site an earthy and elegant tone which is in keeping with the vibe of a florist shop. The header and footer are a shade of pastel green taken from the background image and the home image of the outside of a florist also reflects these floral and earthy tones. The pastel green is used throughout the site, and the dark text and buttons serve as a nice contrast.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/background-img.png?raw=true)



The fonts used throughout the site are Quicksand and Dancing Script. The first being used for the main home page banner texts as a call to action, as well as the about us section and product details text. While the more fluid and fun Dancing Script is used for the site name and headings. These fonts provided a great contrast for the user to identify sections and work well together, as both are rounded in nature and have similar weight. Quicksand is more uniform while Dancing Script is reminiscent of florals and floats across the page.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/fonts.png?raw=true)



## Features



### Existing Features



#### Navbar



Allows user to navigate through the site and also exapnds on smaller devices for better ux design.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/navbar.png?raw=true)



![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/navbar-collapsed.png?raw=true)


The expanded and collapsed navbars also have dropdown menues:

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/navbar-options.png?raw=true)



![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/navbar-collapsed-menu.png?raw=true)



#### Homepage



The landing page with a call to action and a refreshing floral backgorund image.



![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/homepage.png?raw=true)



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



#### Product Management – Admin



Here staff and super users can add new products and set all elements of the products.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/admin-delete-edit.png?raw=true)


![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/add-product.png?raw=true)



#### Events



The events page allows users to view upcoming events on the events dashboard and click to register for an event.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/fonts.png?raw=true)


![screenshot]()



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

The add to wishlist function is currently not working, I ran in to an error and caould not fix it before project submission deadline unfortunatelty.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/readme/wishlist-product.png?raw=true)



### Future Features



Features to be implemented may include:

* Allowing logged in users to rate products

* Allowing logged in users to leave reviews under products

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



The code has been tested using:

[W3 HTML validator](https://validator.w3.org/) - A few minor error were flagged related to how the tool reads repeated templates and structure from the Boutique Ado walkthrough project where this project is based on. Throughout manual testing, it was identified these minor error have no impact when running e-commerce application.


[W3 CSS validator](https://jigsaw.w3.org/css-validator/) - no errors


[jshint](https://jshint.com/) - no errors


[CI Python Linter](https://pep8ci.herokuapp.com/) - a few minor warnings due to whitespace and lines too long, but nothing that affected the site itself or the functionality.



The code was also checked throughout the project where errors showed up on Visual Studios and these were fixed as they arose, as well as ongoing debugging in Chrome Developer Tools, Stack Overflow, Django documentation, W3Schools and Chat GBT.



### Lighthouse Performance



Below are screenshots fromm Goofle's lighthouse testing showing performance levels of the site pages.

![screenshot](https://github.com/DaniCarmo/Florist-p5/blob/main/static/testing/lighthouse-home.png?raw=true)


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



### Unfixed Bugs



The add to wishlist function is currently not working, I ran in to an error and caould not fix it before project submission deadline unfortunatelty.



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



To deploy the project through Heroku I followed these steps:



1. Create a Heroku account.

2. Sign up with a student account for credits. (optional)

3. Once logged in, select create a new app.

4. Select an app name and region EU.

5. Select deployment method as connect to github.

6. Find the desired repo from your github.

7. Enable automatic deploys and select the main branch.

8. In the settings tab select reveal config vars and Input the required hidden variables, such as Stripe keys, AWS keys, Database url, and your project’s secret key.

9. Navigate to the 'Deploy' page and 'GitHub' from the 'Deployment method' section.

10. Select deploy and once built you will see a notice on Heroku that build was successful and you click on “Open App” to view the live site.



## Credits



* Used the Code Institute’s P5 sample project, Boutique Ado, as a guide and basic template for the site.

* Followed tips and troubleshooting throughout the project on Stackoverflow [stackoverflow](https://stackoverflow.blog/), Python.org [python-org](https://www.python.org/) and w3Schools[w3schools](https://www.w3schools.com/).

* Got the site and product images from Pexels [Pexels](https://www.pexels.com/).

* I used ChatGBT [chat-gbt](https://chat.openai.com/) to assist with coming up with the ‘about us’ and product descriptions.