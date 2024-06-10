# The Happy Florist



View the live site [here](https://the-happy-florist-5c44ce792179.herokuapp.com/)



![screenshot of the live site](main)



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

      * [Facebook Page](#facebook)

   * [Future Features](#future-features)

* [Technologies Used](#technologies-used)

* [Testing](#testing)

     * [Lighthouse Testing](#lighthouse-testing)

     * [Manual Testing](#manual-testing)

     * [Automated Testing](#automated-testing)

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



All user stories are available to view [here](https://github.com/users/DaniCarmo/projects/2) on Github.

(link to user stories kanban)



(screenshot of kanban)



### Wireframes



Desktop:



Tablet:



Mobile:



### Color Scheme & Typography



The colors mainly revolve around the background image consisting of pastel greens, reds and yellow. These colors compliment each other and give the site an earthy and elegant tone which is in keeping with the vibe of a florist shop. The header and footer are a shade of pastel green taken from the background image and the home image of the outside of a florist also reflects these floral and earthy tones. The pastel green is used throughout the site, and the dark text and buttons serve as a nice contrast.

(screenshot of background image with color picker)



The fonts used throughout the site are Quicksand and Dancing Script. The first being used for the main home page banner texts as a call to action, as well as the about us section and product details text. While the more fluid and fun Dancing Script is used for the site name and headings. These fonts provided a great contrast for the user to identify sections and work well together, as both are rounded in nature and have similar weight. Quicksand is more uniform while Dancing Script is reminiscent of florals and floats across the page.

(screenshot of fonts)



## Features



### Existing Features



#### Navbar



Allows user to navigate through the site and also exapnds on smaller devices for better ux design.

(multiple screenshots of navbar)



#### Homepage



The landing page with a call to action and a soothing floral backgorund image.



(screenshot)



#### Search Bar



For users to search by word or feature.

(screenshot)



#### User Login/Sign Up



Django Allauth register page, allows users to make an account.

(screenshots)



#### Free Delivery for Members

Users with an account can avail of free delivery on all orders, no min. Price, to encourage site users to sign up and create an account.

(screenshot)



#### About Us – Staff



Section for users to get an insight in to the business and recognise the faces of staff to provide a more friendly user experience.

(screenshot)



#### Newsletter Sign up



Users can subscribe to The Happy Florist's newsletter to stay up to date with news, events and offers.

(screenshot)



#### Products List



This page has many versions based on user searches and sorting parameters. Users can see available products sorted here with image, product name, price, and average rating.

(screenshot)



 #### Product Details



Here users can view a specific product details and pricing. This will give a full review of the product, and the user can also select sizes for flower bouquets. The default price and size is set to ‘Medium’ bouquet sizes, and when the user selects ‘Small’ or ‘Large’ from the dropdown then the price automatically updates to reflect size. For other products such as balloons and sweets, there is one set price.

(screenshots with diff sizes and price)



#### Product Management – Admin



Here staff and super users can add new products and set all elements of the products.

(screenshot)



#### Events



The events page allows users to view upcoming events on the events dashboard and click to register for an event.

(screenshot)



#### Events Gallery



Users can view past events via the gallery carousel on the events page, to get a  feel for what the events may be like.

(screenshot)



#### Events Management – Admin



The site admin/staff can log in here to add, delete or update and event.

(screenshot)



#### Facebook Page

I created a Facebook business page for users to follow, interact and get in touch with the business.

(screenshot)



### Future Features



Features to be implemented may include:

* Allowing logged in users to rate products

* Allowing logged in users to leave reviews under products

* Create a user-friendly event sign up page, where user can enter their details and chose events from a dropdown schedule and they will receive a confirmation email invite so it will sync up with their personal calendars on their phone, PC, etc.

* More social media features to encourage a larger online presence and support, such as an Instagram and Twitter as well as a YouTube chanel to show events and demonstrations.



## Technologies used



* [Bootstrap](https://www.bootstrapcdn.com/)

   *For adding responsive styling to the site.

* [Python](https://www.python.org/)

   * Used to provide functionality to the site.

* [Visual Studios](https://visualstudio.microsoft.com/vs/community/)

   * Used to create the code and content for the repository.

* [Github](https://github.com/)

   * Used to host the repository.

* [Wireframe.cc](https://wireframe.cc/).

   * To create the wireframes and design at planning stage.

* [Quickbase](https://www.quickbase.com/).

   * Used to create a database schema during planning stage.

* [Heroku](https://dashboard.heroku.com/apps).

   * Used to host the website.

* [Amazon Web Services](https://dashboard.heroku.com/apps).

   * Used to host the static files.

* [Heroku](https://dashboard.heroku.com/apps).

   * Used to host the website and used Heroku Postgres to attach database.



## Testing



The site pages have been tested on various screen sizes to ensure that the content is responsive and all screenshots can be viewed [here](link to testing folder with screenshots)



The code has been tested using:

[W3 HTML validator](https://validator.w3.org/) - no errors



[W3 CSS validator](https://jigsaw.w3.org/css-validator/) - no errors



[jshint](https://jshint.com/) - no errors



The code was also checked throughout the project where errors showed up on Visual Studios regarding lines too long and white space trailing, and these were fixed as they arose, as well as ongoing debugging in Chrome Developer Tools, Stack Overflow, Django documentation, W3Schools and Chat GBT.



### Lighthouse Performance



Below are screenshots fromm Goofle's lighthouse testing showing performance levels of the site pages.

(screenshots - multiple)



### Manual Testing



Ran each test mentioned in the table below multiple times and each action executes as intended, providing confirmation of successful user story requirements and actions.



### Automated Testing





### Unfixed Bugs



There are no unfixed bugs recorded.



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



Create a Heroku account.

Sign up with a student account for credits. (optional)

Once logged in, select create a new app.

Select an app name and region EU.

Select deployment method as connect to github.

Find the desired repo from your github.

Enable automatic deploys and select the main branch.

In the settings tab select reveal config vars and Input the required hidden variables, such as Stripe keys, AWS keys, Database url, and your project’s secret key.

Navigate to the 'Deploy' page and 'GitHub' from the 'Deployment method' section.

Select deploy and once built you will see a notice on Heroku that build was successful and you click on “Open App” to view the live site.



## Credits



* User the Code Institute’s P5 sample project, Boutique Ado, as a guide and basic template for the site.

* Followed tips and troubleshooting throughout the project on Stackoverflow [stackoverflow](https://stackoverflow.blog/), Python.org [python-org](https://www.python.org/) and w3Schools[w3schools](https://www.w3schools.com/).

* Got the site and product images from Pexels [Pexels](https://www.pexels.com/).

* I used ChatGBT [chat-gbt](https://chat.openai.com/) to assist with coming up with the ‘about us’ and product descriptions.