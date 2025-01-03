<h2 align="left"><img src="docs/pictures/am-i-responsive.jpg"></h2>

## Project Purpose

This is a Code Institute student project for Milestone 3, built to satisfy the requirements for the EKC DigitalLearn Diploma (Level 5) in [Web Application Development](https://www.ekcgroup.ac.uk/ekc-training/computing/web-application-development-diploma-level-5). 

This project has been created in order to provide a community CRUD application on a deployed interactive website. The project was built using **Gitpod**. 

The information has been presented in a way that ensures the users achieve their goals of:
* understanding what the site's function is
* understanding how to create, read, update and delete their own records or posts
* being able to register, log in and log out of this community site

The site also enhances the owner's goals by:
* showcasing their database design skills
* showcasing their Python programming skills
* showcasing their Flask skills
* showcasing their back-end development skills by allowing users to change data in a MongoDB database with the aid of the Flask mini-framework.


## Project Requirements

* The technologies used were HTML, CSS, **Python, Flask and MongoDB**.
* This interactive back-end project contains pages to enable users to create, read, update and delete user records in a non-relational database
* This README.md file explains what the project does and the value it provides for the users
* Version control is provided by Git and GitHub
* External code, libraries, templates, images, information, etc. will be listed in the **Credits**, at the bottom of this README.
* This project is deployed via **Heroku**. The code stored in a GitHub repository, whilst the data is stored in the non-relational database, **MongoDB Atlas**.

---

<h1 align="left">Flask App with MongoDB: Vazy Garden</h1>

![Python](https://img.shields.io/static/v1?label=Python&message=3.8.11&color=blue&logo=python&logoColor=ffffff)
![Flask](https://img.shields.io/static/v1?label=Flask&message=2.2&color=yellow&logo=flask)
![MongoDB](https://img.shields.io/static/v1?label=MongoDB&message=5.0.15&color=brightgreen&logo=mongodb&logoColor=ffffff)

[View the deployed app on Heroku.](https://vazy-garden.herokuapp.com/)

[View the video demo on YouTube.](https://youtu.be/LbvWNagwn6c)

The aim of the project is to provide a community site for garden and allotment enthusiasts. Users will be able to log in to create records for plants they wish to cultivate. It will be designed to aid the user in deciding which seeds or plants to set (sow/plant) in a particular month. They will also be able to add if the plants are for human (edible) or animal food. On the home page users will be able to see everyone's entries but on their own profile page they will only be able to view their own plants.

The site is designed to be responsive and accessible on a range of devices, making it easy to use for potential users.

<h2 align="left"><img src="https://images.unsplash.com/photo-1619029403797-7388c3f322a1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80"></h2>

---

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Owner Goals**](#owner-goals)
    - [**Design**](#design)
        - [**The CRUD App**](#the-crud-app)
        - [**Framework**](#framework)
        - [**Colour Scheme**](#colour-scheme)
        - [**Typography**](#typography)
        - [**Imagery**](#imagery)
    - [**Wireframes**](#wireframes)
    - [**Non-Relational Database**](#non-relational-database)

2. [**Features**](#features)
    - [**Current Features**](#current-features)
        - [**Navigation**](#navigation)
        - [**Home Page**](#home-page)
        - [**About**](#about)
        - [**Log In**](#log-in)
        - [**Register**](#register)
        - [**Profile**](#profile)
        - [**Add Plant**](#add-plant)
        - [**Add Category**](#add-category)
        - [**Log Out**](#log-out)
        - [**404 Page**](#404-page)
    - [**Future Features**](#future-features)

4. [**Technologies Used**](#technologies-used)
    - [**Design Tools**](#design-tools)
    - [**Front-End**](#front-end)
    - [**Back-End**](#back-end)
    - [**Validation and Evaluation**](#validation-and-evaluation)

5. [**Manual Testing**](TESTING.md)
    - [**Supported Browsers and Screen Sizes**](TESTING.md/#supported-browsers-and-screen-sizes)
    - [**Testing Against User Stories**](TESTING.md/#testing-against-user-stories)
    - [**Test Cases**](TESTING.md/#test-cases)
    - [**Code Validation**](TESTING.md/#code-validation)
    - [**Site Audit**](TESTING.md/#site-audit)
    - [**Compatibility**](TESTING.md/#compatibility)
    - [**Bugs Found**](TESTING.md/#bugs-found)
    - [**Known Issues**](TESTING.md/#known-issues)

6. [**Deployment**](DEPLOYMENT.md)
    - [**Local Deployment**](DEPLOYMENT.md/#local-deployment)
    - [**Remote Deployment**](DEPLOYMENT.md/#remote-deployment)

7. [**Credits**](#credits)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

---

## UX

### User stories

:white_check_mark: *denotes current features*

"**_As a user, I would like to_** _____________________________"

- :white_check_mark: *create, read, update and delete my own plant records*.
- :white_check_mark: *easily understand how to use the site*.
- :white_check_mark: *keep my information secure*.
- :white_check_mark: *view the site without logging in*.
- :white_check_mark: *search for plants to feed my pet*.
- :white_check_mark: *search for plants that I need to set in a particular month*.

### Owner goals

"**_As an owner, I would like to_** _____________________________"

- :white_check_mark: *build a Flask app*.
- :white_check_mark: *allow users to store their data via the app*.
- :white_check_mark: *build a community gardening app to also assist pet owners*.
- :white_check_mark: *build an app to be visually attractive*.

### Design

#### The CRUD App

- This app was inspired by the Code Institute backend development tutorial for a [Task Manager](https://github.com/Code-Institute-Solutions/TaskManagerAuth), by Tim Nelson.

- What is a CRUD app? This type of app allows the user to create, read, update and delete records or posts in a database via graphical interface. In this case the database is [MongoDB Atlas 5.0.15](https://www.mongodb.com/atlas) and as the app is developed with [Python 3.8.11](https://www.python.org/downloads/release/python-3811/), the graphical interface is provided by HTML5 and the mini-framework, [Flask 2.2](https://flask.palletsprojects.com/en/2.2.x/) with [Materialize CSS 1.0.0](https://materializecss.com/).

- Why this app? Our household has an allotment and every year in the early spring, we excitely purchase lots of seeds for pretty flowers and delicious vegetables. These precious packets are then stored in a 'safe place' until the time comes for sowing. As usual - out of sight, out of mind - these seeds get forgotten about until it is too late. So I developed this app for like minded folk - here we can create our plant posts stating in which month they can be set. A search facility on keywords allows the user to both search their own entries and others. The home page does not require login, but profile pages do. All entries are visible to every one, but only the post owner can edit or delete them. 

- View the website design flowchart to see which Python functions are associated with which web pages of the app:

<h2 align="left"><img src="docs/pictures/design-site.jpg"></h2>

Flask uses the route() decorator to bind a function to a URL. For example:
```Python
@app.route('/')
def index():
    return 'Index Page'
```

#### Framework

- [Materialize 1.0.0](https://materializecss.com/) is a modern and clean layout of Materialize as a front-end framework, with simple documentation.
- [jQuery 3.5.1](https://code.jquery.com/jquery/) was used for minimal JavaScript programming.
- [Flask 2.2.3](https://flask.palletsprojects.com/en/2.2.x/) is a microframework used to render the back-end Python with the front-end Materialize.

#### Colour Scheme

The following Materialize [colour scheme](https://materializecss.com/color.html) was chosen for simplicity,  readability and lends itself nicely to the subject of gardening.

<h2 align="left"><img src="docs/pictures/colours.png"></h2>

#### Typography

[Roboto font](https://fonts.google.com/specimen/Roboto) is the standard font used by Materialize, which is used for good readability and contrast when required. It is considered both [friendly and professional](https://xd.adobe.com/ideas/principles/web-design/best-modern-fonts-for-websites/), so should suit most sites and devices.

#### Imagery

- In general, all pages have the Materialize white background with dark teal or black text. This ties into the subject matter whilst matching the default shade of teal for Materialize toggle switches and dropdown selectors
- The Home and Profile pages feature the standard Materialize [Card Reveal](https://materializecss.com/cards.html) displayed in a grid style of up to three columns across the page. Each card has a image with minimum content, but when clicked, further information is revealed. At the top of the page is a search panel for finding plants via keywords or phrases with Reset and Search buttons.
- The About page contains only text and icons in a Materialize [Card Panel](https://materializecss.com/cards.html)
- The Add/Edit/Delete pages include a mixture of text, text inputs, toggle switches and dropdown selectors with Cancel and Add/Update/Delete buttons in a Card Panel.
- The Register and Log In pages also contain text inputs only with Log In/Register buttons within a Card Panel.
- The Categories page features the [Basic Card](https://materializecss.com/cards.html) displayed in a grid style of up to four columns across the page.

### Wireframes

View the wireframe PDF [here](docs/ux/wireframe-mp3.pdf).

The pages contain the same functionality and look the same on every device, with the exception to the menus and the number of plant cards displayed across the screen.

#### Tablet 

- Home

<h2 align="left"><img src="docs/ux/tablet-home.jpg"></h2>

- Profile

<h2 align="left"><img src="docs/ux/tablet-profile.jpg"></h2>

- Add / Edit Plants Form

<h2 align="left"><img src="docs/ux/tablet-update.jpg"></h2>

- Categories

<h2 align="left"><img src="docs/ux/tablet-categories.jpg"></h2>

- Register

<h2 align="left"><img src="docs/ux/tablet-register.jpg"></h2>

- Log In

<h2 align="left"><img src="docs/ux/tablet-login.jpg"></h2>

- Logged Out Screen

<h2 align="left"><img src="docs/ux/tablet-logout.jpg"></h2>

- Menu

    - Logged In

    <h2 align="left"><img src="docs/ux/tablet-menu-login.jpg"></h2>

    - Logged Out

    <h2 align="left"><img src="docs/ux/tablet-menu-logout.jpg"></h2>

#### Desktop

- Home

<h2 align="left"><img src="docs/ux/desktop-home.jpg"></h2>

- Other Pages - same as for tablet

#### Mobile

- Home

<h2 align="left"><img src="docs/ux/mobile-home.jpg"></h2>

- Other Pages - same as for tablet

### Non-Relational Database

Database Entity Relationship Diagram (MongoDB)

<h2 align="left"><img src="docs/pictures/db-erd.jpg"></h2>

Collection (Table) Examples

* Plants
<h2 align="left"><img src="docs/pictures/db-plants.jpg"></h2>

* Categories
<h2 align="left"><img src="docs/pictures/db-categories.jpg"></h2>

* Months
<h2 align="left"><img src="docs/pictures/db-months.jpg"></h2>

* Animals
<h2 align="left"><img src="docs/pictures/db-animals.jpg"></h2>

* Users
<h2 align="left"><img src="docs/pictures/db-users.jpg"></h2>

---

## Features

### Current Features

* This app consists of nine user pages for:
    - Home, About, Log In, Register, Profile, Add Plant, Edit Plant, Delete Plant, Log Out
* Plus two additional administrator pages for:
    - Categories and Add Category
* And a further two pages for:
    - 404 page not found and 500 internal server errors
 

#### Navigation :compass:

Navigation bar will be the default responsive Materialize one for all pages, except those for the 404 and 500 errors, which will have none.

* Desktops
   - the menu items: Vazy Garden branding, Home, About, Profile, Add Plant, LogOut will be inline and fixed across the top of the screen. All pages will have white text on a teal banner and on hover, a dark teal backgound.
    - Vazy Garden and Home will navigate to route /get_plants and render plants.html.
    - About to /about and render about.html.
    - Profile to /profile/(username) and render profile.html.
    - Add Plant to /add_plant and render add_plant.html.
    - Add Category (administrator user only) to /get_categories.
    - Log Out to /login and render login.html.

* Mobiles 
    - will feature the collapsed navigation with a hamburger icon, which when selected, will reveal a sidenav slide out menu with black text on a white background. On hover, the text background will change from white to light grey. This menu will contain the same items as the desktop one.

#### Home Page :bouquet:

Anyone (guest, member, administrator) can view this page which features everyone's plant cards and a search panel. The plant cards are laid out across the screen in alphabetical order of plant name.

#### About :information_source:

Outlines the reason for the app and it's instructions for use.

#### Register :bust_in_silhouette::heavy_plus_sign:

Anybody can *register* for free and create their own unique profile to store their own plants to set. This is built using [Werkzeug](https://werkzeug.palletsprojects.com/en/2.2.x/) for password hashing, authentication and authorisation. Passwords are hashed for security purposes. Werkzeug is a comprehensive [WSGI](https://wsgi.readthedocs.io/en/latest/) (Web Server Gateway Interface) web application library.

#### Log In :bust_in_silhouette:

This facility is built using Flask [wrapper functions and decorators](https://pythonprogramming.net/decorator-wrappers-flask-tutorial-login-required/) for authentication and authorization in order to validate user details. Two login decorators have been created; one for registered users and another for the administrator.

#### Profile :lock:

Flask decorators protect users' profiles and data. Only the current logged-in owner can add, edit or delete their plants. The owner's plants are displayed across the screen in plant-name alphabetical order. Owners select the vertical ellipsis on each plant card to reveal delete/edit buttons.

#### Add Plant :seedling::heavy_plus_sign:

Logged-in users can add plants with the following information:
- plant category e.g. flower, vegetable, etc
- plant name
- plant description
- month to set (sow or plant)
- indicate if *edible* (for humans)
- specify an animal to feed
- add an Unsplash image link
- add plant catalogue link for easy purchase
- indicate if the sowing or planting is *done*

#### Edit Plant :pencil2:

Logged-in users can only edit their own plants and update the plant information previously added. Owners select the vertical ellipsis on each plant card to reveal *edit* button. On selecting *edit*, they will then be taken to the *Edit Plant* page where they can change all fields and *update*, or otherwise *cancel* at any time.

#### Delete Plant :scissors:

Logged-in users can only delete their own plants by selecting the vertical ellipsis on each plant card to reveal *delete* button. On selecting *delete*, they will then be taken to the *Delete Plant* page where they can confirm *delete*, or otherwise *cancel*.

#### Log Out :point_right:

Logged-in users can *log out* of their account.

#### 404 Page :no_entry:

A 404 page-not-found is visible when the user tries to access an unknown page. This can happen if they mistype an url for a site page, e.g. mistype 
```vazy-garden.herokuapp.com/loggin``` 
instead of the correct one 
```vazy-garden.herokuapp.com/login```
A link back to the home page is provided.

#### 500 Page :warning:

A 500 internal server error page is visible when the server encounters an unexpected condition that prevents it from fulfilling a request. A link back to the home page is provided.

#### View Categories :card_index_dividers:

Only the **administrator** can view the page with the list of categories. From here they can navigate to the Add Category page.

#### Add Category :card_index_dividers::heavy_plus_sign:

Only the **administrator** can view this page in order to add categories.


### Future Features

- Modify the administrator to be a named person, identified by an extra field in the database, e.g. admin: "yes".
- Allow users to change their passwords.
- Allow users to 'like' other's plants.
- Allow users to 'borrow' other's plants for own profile, but not allow editing of these.
- Allow the administrator to delete and edit categories
- Allow users to message each other
- Checking for inappropriate material.

---

## Technologies Used

* Cloud developer platform from [Gitpod](https://www.gitpod.io/).
* IDE integrated into Gitpod from [Visual Studio Code](https://code.visualstudio.com/).
* Debugging assisted by [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/).
* Version control integrated into Gitpod from [Git](https://git-scm.com/).

### Design Tools

* Wireframes from [Balsamiq](https://balsamiq.com/).
* Roboto font from [Materialize](https://fonts.google.com/specimen/Roboto).
* Colour palette generated by [Materialize](https://materializecss.com/color.html).
* Icon library and toolkit from [Font Awesome 5](https://fontawesome.com/).
* Favicon created on [favicon.cc](https://www.favicon.cc/).
* Online photo editor from [Pixlr](https://pixlr.com/x/).
* Stock photos from [Unsplash](https://unsplash.com).
* Showcasing the site on different devices by [Bytes](https://ui.dev/amiresponsive)
* Paint from [Microsoft](https://apps.microsoft.com/store/detail/paint/9PCFS5B6T72H?hl=en-us&gl=us)
* Snip and Sketch from [Microsoft](https://apps.microsoft.com/store/detail/snipping-tool/9MZ95KL8MR0L?hl=en-gb&gl=gb)
* PDF Reader from [Adobe Acrobat Reader](https://www.adobe.com/uk/)
* Flowchart by [diagrams.net/draw.io](https://www.diagrams.net/)
* MongoDB ERD created by [DbSchema](https://dbschema.com/)
* Demo video for YouTube created on [Clipchamp](https://app.clipchamp.com/)

### Front-End

- ![HTML5](https://img.shields.io/static/v1?label=HTML&message=5&color=E34F26&logo=html5&logoColor=ffffff)
    - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) as the base for markup text.
- ![CSS3](https://img.shields.io/static/v1?label=CSS&message=3&color=1572B6&logo=css3&logoColor=ffffff)
    - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) for custom styling the site.
- ![jQuery 3.5.1](https://img.shields.io/static/v1?label=jQuery&message=3.5.1&color=0769AD&logo=jquery&logoColor=ffffff)
    - [jQuery 3.5.1](https://code.jquery.com/jquery/) for JavaScript functionality.
- ![Materialize 1.0.0](https://img.shields.io/static/v1?label=Materialize&message=1.0.0&color=ee6e73)
    - [Materialize 1.0.0](https://materializecss.com/) is a modern responsive CSS framework based on Material Design by Google.

### Back-End

- ![Python](https://img.shields.io/static/v1?label=Python&message=3.8.11&color=blue&logo=python&logoColor=ffffff)
    - [Python 3.8.11](https://www.python.org/) is a high-level, general-purpose programming language.
- ![Flask](https://img.shields.io/static/v1?label=Flask&message=2.2&color=yellow&logo=flask)
    - [Flask 2.2](https://flask.palletsprojects.com/en/2.2.x/) is a micro web framework written in Python.
- ![Jinja](https://img.shields.io/static/v1?label=Jinja&message=2&color=E34F26&logo=jinja)
    - [Jinja2](https://palletsprojects.com/p/jinja/) for templating with Flask.
- ![Werkzeug](https://img.shields.io/static/v1?label=Werkzeug&message=2.2.3&color=orange&logo=werkzeug)
    - [Werkzeug 2.2.3](https://werkzeug.palletsprojects.com/en/2.2.x/) for password hashing, authentication and authorisation.
- ![Heroku](https://img.shields.io/static/v1?label=Heroku&message=PaaS&color=430098&logo=heroku)
    - [Heroku](https://www.heroku.com) is used as *"Platform as a Service"* (PaaS) for app hosting.
- ![MongoDB](https://img.shields.io/static/v1?label=MongoDB&message=5.0.15&color=brightgreen&logo=mongodb&logoColor=ffffff)
    - [MongoDB Atlas 5.0.15](https://www.mongodb.com/atlas) is used as a non-relational database plugin via Heroku.

### Validation and Evaluation

* HTML validation from [W3C](https://validator.w3.org/#validate_by_input).
* CSS validation from [Jigsaw (W3C)](https://jigsaw.w3.org/css-validator/).
* Python validation from [CI Python Linter](https://pep8ci.herokuapp.com/).
* jQuery validation from [JSHint](https://jshint.com/).
* Web page quality improvements assisted by [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) and [WebPageTest](https://www.webpagetest.org/).

---

## Project Testing

See the document [TESTING.md](TESTING.md) for the code validation, site evaluation and manual tests.

---

## Deployment

See the document [DEPLOYMENT.md](DEPLOYMENT.md) for local and Heroku deployment.

---

## Credits

A huge thank you to the following people and organisations, because without you, the website would not have been produced in it's present form.

### From the Course

Heroku deployment instructions from Code Institute video tutorial

Readme styling from Tim Nelson's project [Unicorn Attractor](https://github.com/TravelTimN/ci-milestone05-fsfw)

Markdown Cheatsheet from [Adam Pritchard](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#html)

### Media

Plant images from [Dean Lewis](https://unsplash.com/@infinitecreations21) on Unsplash

Forget-me-not image from [Noah Boyer](https://unsplash.com/@emerald_) on Unsplash

Default/fallback plant image (pineapple wearing sunglasses) from [Heather Ford](https://unsplash.com/@the_modern_life_mrs) on Unsplash

Wallpaper for 404/500 page from [Maxim Berg](https://unsplash.com/@maxberg) on Unsplash

Emoji shortcodes from [Ikatyang](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md) on GitHub


### Code

Although the code is the work of the author, some of the code has been sourced from or inspired by others.

Many of the references have been embedded as links throughout this document and indicated by the active blue text links.

The code is based on [Task Manager Tutorial](https://github.com/Code-Institute-Solutions/TaskManagerAuth) by Tim Nelson

[Fort Knox Password Generator](https://randomkeygen.com/) from RandomKeygen

[Adding custom validation to Materialize dropdown](https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/04-AddingATask-WritingToTheDatabase/02-materialize-select-validation/static/js/script.js) by Tim Nelson

[View Decorators](https://flask.palletsprojects.com/en/2.2.x/patterns/viewdecorators/) documentation from Flask

[Flask Decorators - Login_Required pages Flask Tutorial](https://pythonprogramming.net/decorator-wrappers-flask-tutorial-login-required/) by Sentdex on YouTube

---

## Acknowledgements

Rachel Furlong - [EKC Training](https://ekcgroup.ac.uk/business-units/ekc-training) Course Facilitator, for generous support and advice.

Rohit Sharma - [Code Institute](https://codeinstitute.net/) Mentor, for the continuous feedback and guidance in industry standards.

Alan McGee - [Code Institute](https://codeinstitute.net/) Tutor, for assisting with some coding issues.

 
