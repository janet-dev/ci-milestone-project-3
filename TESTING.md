# Manual Testing

**The site was built, tested and validated on the [Chrome browser](docs/pictures/chrome.jpg) only.**

---

## Testing Contents

- [**Supported Browsers and Screen Sizes**](#supported-browsers-and-screen-sizes)
- [**Testing Against User Stories**](#testing-against-user-stories)
- [**Test Cases**](#test-cases)
- [**Code Validation**](#code-validation)
- [**Site Audit**](#site-audit)
- [**Compatibility**](#compatibility)
- [**Bugs Found**](#bugs-found)
- [**Known Issues**](#known-issues)

Back to [**README.md**](README.md)

---

## Supported Browsers and Screen Sizes

Materialize v1.0.0 was used for building the site - see the [supported browsers](https://github.com/Dogfalo/materialize).
* Materialize is compatible with:
    - Chrome 35+
    - Firefox 31+
    - Safari 9+
    - Opera
    - Edge
    - IE 11+

* Devices supported:
    - Mac
    - Windows
    - Android
    - iOS

* The Materialize standard grid has 12 columns. No matter the size of the browser, each of these columns will always have an equal width. See the section [Creating Responsive Layouts](https://materializecss.com/grid.html) in the Materialize documentation on how to design the layouts so that they look great on all screen sizes. 

    | Device                   | Class Prefix   | Dimensions |
    | ------------------------ | -------------- | ---------- |
    | Mobile                   | .s             | <=600px    |
    | Tablet                   | .m             | > 600px    |
    | Desktop                  | .l             | > 992px    |
    | Large Desktop            | .xl            | > 1200px   |

---

## Testing Against User Stories

"**_As a user, I would like to_** _____________________________"

- *create, read, update and delete my own plant records*
    - All logged-on users are able to view, add, edit or delete their own plants via appropriate pages:
        - View
        <h2 align="left"><img src="docs/testing/user/profile.jpg"></h2>
        - Add
        <h2 align="left"><img src="docs/testing/user/add.jpg"></h2>
        - Edit or delete
        <h2 align="left"><img src="docs/testing/user/edit-delete.jpg"></h2>
        - Edit
        <h2 align="left"><img src="docs/testing/user/edit.jpg"></h2>
        - Delete
        <h2 align="left"><img src="docs/testing/user/delete.jpg"></h2>

- *easily understand how to use the site*
    - Instructions on how to use the site are detailed on the **About** page.
    <h2 align="left"><img src="docs/testing/user/about.jpg"></h2>

- *keep my information secure*
    - Users need to register with a unique username and password. 

    <h2 align="left"><img src="docs/testing/user/register.jpg"></h2>

    - Passwords are hashed for security purposes by Werkzeug. This is a comprehensive [WSGI](https://wsgi.readthedocs.io/en/latest/) (Web Server Gateway Interface) web application library.

    - Further security is provided by defensive programming and Flask login-decorators. There are two decorators for this site; one for users and another for the administrator. These decorators 'wrap' the user/administrator editing functions and check if they are in fact the owner of the records:
        - User login decorator for the profile page.

        <h2 align="left"><img src="docs/testing/user/login-decorator.jpg"></h2>

        The same decorator is used for the *log out / add plant* pages
        - Administrator login decorator for the category page.

        <h2 align="left"><img src="docs/testing/user/admin-decorator.jpg"></h2>

        The same decorator is used for the *add category* page.

    - For the *edit plant / delete plant* pages; a check is made to see if the current session user is the owner of the plant record. If not, they are taken to a 404 page.

    <h2 align="left"><img src="docs/testing/user/defense.jpg"></h2>

- *view the site without logging in*
    - Anyone can view all the plants on the home page, without registering or logging in:

    <h2 align="left"><img src="docs/testing/user/home.jpg"></h2>

- *search for plants to feed my pet*
    - Users are able to search on keywords from the fields:
        - plant name
        - plant description
        - set month
        - animal name

    <h2 align="left"><img src="docs/testing/user/search-animal.jpg"></h2>

- *search for plants that I need to set in a particular month*

    <h2 align="left"><img src="docs/testing/user/search-month.jpg"></h2>

---

## Test Cases

These cases are included in order to help the next developer understand the design of the site and how to extend it. They document the look and functionality of each page. All pages and features will function and look the same whether on desktop, tablet or mobile, except for the 
- shorter branding (**Vazy** instead of **Vazy Garden**) and *hamburger* menu for mobiles and some tablets

    <h2 align="left"><img src="docs/testing/testcases/nav-hamburger.jpg"></h2>

    When the menu icon is selected, it reveals a sliding lefthand panel listing the menu options. Select an option to navigate to the appropriate page.

    <h2 align="left"><img src="docs/testing/testcases/nav-mobile.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/nav-tablet.jpg"></h2>


- number of cards displayed across the screen:
    - desktops tend to show three cards across

    <h2 align="left"><img src="docs/testing/testcases/home-desktop.jpg"></h2>

    - tablets tend to show two cards across

    <h2 align="left"><img src="docs/testing/testcases/home-tablet.jpg"></h2>
    
    - mobiles tend to show one card across

    <h2 align="left"><img src="docs/testing/testcases/home-mobile.jpg"></h2>

### Test Case Logs

Note that some limited defensive programming is included in order to build a more secure app, but it is outside the scope of the project criteria.

The following logs detail the testing carried out:

---

#### Register Page

<h2 align="left"><img src="docs/testing/testcases/testcases-register.jpg"></h2>

- Results

    <h2 align="left"><img src="docs/testing/testcases/testcases-register1-xls.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcases-register2-xls.jpg"></h2>

- Screenshots

    - Step 2
    <h2 align="left"><img src="docs/testing/testcases/testcases-register-02.jpg"></h2>
    - Step 3
    <h2 align="left"><img src="docs/testing/testcases/testcases-register-03.jpg"></h2>
    - Step 4
    <h2 align="left"><img src="docs/testing/testcases/testcases-register-04.jpg"></h2>
    - Step 5
    <h2 align="left"><img src="docs/testing/testcases/testcases-register-05.jpg"></h2>
    - Step 6
    <h2 align="left"><img src="docs/testing/testcases/testcases-register-06.jpg"></h2>
    - Step 6 - database
    <h2 align="left"><img src="docs/testing/testcases/testcases-register-06b.jpg"></h2>
    - Step 8
    <h2 align="left"><img src="docs/testing/testcases/testcases-register-08.jpg"></h2>
    - Access Denied
    <h2 align="left"><img src="docs/testing/testcases/testcases-access-denied.jpg"></h2>
    - 404 Page
    <h2 align="left"><img src="docs/testing/testcases/testcases-404.jpg"></h2>

---

#### Log In Page

<h2 align="left"><img src="docs/testing/testcases/testcases-login.jpg"></h2>

- Results

    <h2 align="left"><img src="docs/testing/testcases/testcases-login1-xls.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcases-login2-xls.jpg"></h2>

- Screenshots

    - Step 2
    <h2 align="left"><img src="docs/testing/testcases/testcases-login-02.jpg"></h2>
    - Step 3
    <h2 align="left"><img src="docs/testing/testcases/testcases-login-03.jpg"></h2>
    - Step 4
    <h2 align="left"><img src="docs/testing/testcases/testcases-login-04.jpg"></h2>
    - Step 5
    <h2 align="left"><img src="docs/testing/testcases/testcases-login-05.jpg"></h2>
    - Step 6
    <h2 align="left"><img src="docs/testing/testcases/testcases-login-06.jpg"></h2>
    - Incorrect User
    <h2 align="left"><img src="docs/testing/testcases/testcases-incorrect-user.jpg"></h2>
    - Step 11
    <h2 align="left"><img src="docs/testing/testcases/testcases-login-11.jpg"></h2>
    - Step 12
    <h2 align="left"><img src="docs/testing/testcases/testcases-login-12.jpg"></h2>

    - Access Denied
    <h2 align="left"><img src="docs/testing/testcases/testcases-access-denied.jpg"></h2>
    - 404 Page
    <h2 align="left"><img src="docs/testing/testcases/testcases-404.jpg"></h2>

---

#### About Page

<h2 align="left"><img src="docs/testing/testcases/testcases-about.jpg"></h2>


- Results

    <h2 align="left"><img src="docs/testing/testcases/testcases-about-xls.jpg"></h2>

- Screenshots

    - Access Denied
    <h2 align="left"><img src="docs/testing/testcases/testcases-access-denied.jpg"></h2>
    - 404 Page
    <h2 align="left"><img src="docs/testing/testcases/testcases-404.jpg"></h2>





[Test Case Template](https://www.guru99.com/download-sample-test-case-template-with-explanation-of-important-fields.html) provided by Thomas Hamilton on GURU99

---

## Code Validation
* HTML - No errors or warnings were detected by [W3C](https://validator.w3.org/#validate_by_input) Validation for pages:
    - [get_plants.html PDF report](docs/testing/validation/w3c-html-get_plants.pdf)
    - [about.html PDF report](docs/testing/validation/w3c-html-about.pdf)
    - [profile.html PDF report](docs/testing/validation/w3c-html-profile.pdf)
    - [add_plant.html PDF report](docs/testing/validation/w3c-html-add_plant.pdf)
    - [edit_plant.html PDF report](docs/testing/validation/w3c-html-edit_plant.pdf)
    - [delete_plant.html PDF report](docs/testing/validation/w3c-html-delete_plant.pdf)
    - [categories.html PDF report](docs/testing/validation/w3c-html-categories.pdf)
    - [add_category.html PDF report](docs/testing/validation/w3c-html-add_category.pdf)
    - [register.html PDF report](docs/testing/validation/w3c-html-register.pdf)
    - [login.html PDF report](docs/testing/validation/w3c-html-login.pdf)
    - [404.html PDF report](docs/testing/validation/w3c-html-404.pdf)
    - [500.html PDF report](docs/testing/validation/w3c-html-500.pdf)

    <h2 align="left"><img src="docs/testing/validation/w3c-html.jpg"></h2>

    HTML with Jinja2 code will cause errors in the validator. A quick fix is to: 
    - right-click the live page and 
    - select "View page source" instead of "Inspect"
    <h2 align="left"><img src="docs/testing/validation/w3c-html-jinja2.jpg"></h2>
    this will open a new tab with the generated code for easy copying and pasting into the validator.
    
    Credit: [Jo Heyndels](https://www.linkedin.com/in/joke-heyndels/), Learning Success Executive at Code Institute


* CSS - No errors or warnings were detected by [Jigsaw (W3C)](https://jigsaw.w3.org/css-validator/#validate_by_input) Validation for:
    - [style.css PDF report](docs/testing/validation/w3c-css.pdf)

    <h2 align="left"><img src="docs/testing/validation/w3c-css.jpg"></h2>

* JavaScript - No errors or warnings were detected by [JSHint](https://jshint.com/) for script.js:

    <h2 align="left"><img src="docs/testing/validation/jshint.jpg"></h2>

* Python - No errors or warnings were detected by [CI Python Linter](https://pep8ci.herokuapp.com/) for: 
    - app.py

    <h2 align="left"><img src="docs/testing/validation/ci-pylinter-app.jpg"></h2>

    - decorators.py

    <h2 align="left"><img src="docs/testing/validation/ci-pylinter-decorators.jpg"></h2>

---

## Site Audit

### Desktop audits

* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) minimum scores:

    <h2 align="left"><img src="docs/testing/audit/lighthouse-min-desktop.jpg"></h2>

    Full PDF reports:

    - [get_plants.html report](docs/testing/audit/lighthouse-get-plants-desktop.pdf)
    - [about.html report](docs/testing/audit/lighthouse-about-desktop.pdf)
    - [profile.html report](docs/testing/audit/lighthouse-profile-desktop.pdf)    
    - [add_plant.html report](docs/testing/audit/lighthouse-add-plant-desktop.pdf)
    - [edit_plant.html report](docs/testing/audit/lighthouse-edit-plant-desktop.pdf)
    - [delete_plant.html report](docs/testing/audit/lighthouse-delete-plant-desktop.pdf)
    - [categories.html report](docs/testing/audit/lighthouse-get-categories-desktop.pdf)    
    - [add_category.html report](docs/testing/audit/lighthouse-add-category-desktop.pdf)
    - [register.html report](docs/testing/audit/lighthouse-register-desktop.pdf)
    - [login.html report](docs/testing/audit/lighthouse-login-desktop.pdf)

    - 404.html report - Lighthouse was unable to generate this:.

    <h2 align="left"><img src="docs/testing/audit/lighthouse-404-desktop.jpg"></h2>

    - Used **WebPageTest** instead - see the article [Why you should be testing your 404 pages web performance](https://nooshu.com/blog/2020/08/25/you-should-be-testing-your-404-pages-web-performance/) by Matt Hobbs on Nooshu.com

* [WebPageTest](https://www.webpagetest.org/) summary:

    <h2 align="left"><img src="docs/testing/audit/webpagetest-404-500.jpg"></h2>

    Full PDF reports:

    - [404.html report](docs/testing/audit/webpagetest-404-desktop.pdf)
    - [500.html report](docs/testing/audit/webpagetest-500-desktop.pdf)

### Mobile audits

* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) minimum scores:

    <h2 align="left"><img src="docs/testing/audit/lighthouse-min-mobile.jpg"></h2>

    Full PDF reports:

    - [get_plants.html report](docs/testing/audit/lighthouse-get-plants-mobile.pdf)
    - [about.html report](docs/testing/audit/lighthouse-about-mobile.pdf)
    - [profile.html report](docs/testing/audit/lighthouse-profile-mobile.pdf)    
    - [add_plant.html report](docs/testing/audit/lighthouse-add-plant-mobile.pdf)
    - [edit_plant.html report](docs/testing/audit/lighthouse-edit-plant-mobile.pdf)
    - [delete_plant.html report](docs/testing/audit/lighthouse-delete-plant-mobile.pdf)
    - [categories.html report](docs/testing/audit/lighthouse-get-categories-mobile.pdf)    
    - [add_category.html report](docs/testing/audit/lighthouse-add-category-mobile.pdf)
    - [register.html report](docs/testing/audit/lighthouse-register-mobile.pdf)
    - [login.html report](docs/testing/audit/lighthouse-login-mobile.pdf)

* [WebPageTest](https://www.webpagetest.org/) summary:

    <h2 align="left"><img src="docs/testing/audit/webpagetest-404-500.jpg"></h2>

    Full PDF reports:

    - [404.html report](docs/testing/audit/webpagetest-404-mobile.pdf)
    - [500.html report](docs/testing/audit/webpagetest-500-mobile.pdf)

---

## Compatibility

The majority of testing and validation was carried out on the Chrome browser with a Windows 10 desktop, but to ensure that a broad range of users can successfully use this site, it was also tested with other browsers in both desktop and mobile configuration.

- Chrome v.112
- Edge v.18
- Firefox v.106
- Safari v.13
- Opera v.97

The results are shown below in a testing matrix:

<h2 align="left"><img src="docs/testing/audit/compatibility.jpg"></h2>

The original Excel version created by Tim Nelson, can be found [here](https://github.com/TravelTimN/ci-milestone04-dcd/blob/main/app/testing/testing-ci-milestone04-dcd.xlsx).

---

## Bugs Found

1. Misalignment of Materialize grid columns

<h2 align="left"><img src="docs/testing/bugs/bug-01.jpg"></h2>

- Solved by assigning margin-left to 0 

<h2 align="left"><img src="docs/testing/bugs/bug-01-soln.jpg"></h2>

for both tablet and desktop

<h2 align="left"><img src="docs/testing/bugs/bug-01-css.jpg"></h2>

2. Unauthorised access to get_category page

Whilst not logged in, a user was able to access this page by manually typing the url

<h2 align="left"><img src="docs/testing/bugs/bug-02.jpg"></h2>

- Solved by using a Flask [login required decorator](https://flask.palletsprojects.com/en/2.2.x/patterns/viewdecorators/). This decorator can be found in decorators.py

<h2 align="left"><img src="docs/testing/bugs/bug-02-soln-decor.jpg"></h2>

it is used to wrap the administrator functions in app.py

<h2 align="left"><img src="docs/testing/bugs/bug-02-soln-app.jpg"></h2>

3. Large card image

User was able to add link to a large image

<h2 align="left"><img src="docs/testing/bugs/bug-03.jpg"></h2>

- Solved by limiting the image size in the CSS. See [CodePen Home Materialize - Fixing Card Images](https://codepen.io/j_holtslander/pen/KbXyrq) by Jay Holtslander

<h2 align="left"><img src="docs/testing/bugs/bug-03-soln.jpg"></h2>

4. Overflow of branding and logo on mobiles

<h2 align="left"><img src="docs/testing/bugs/bug-04.jpg"></h2>

- Solved by adding separate media queries for default branding and an abreviated one for mobiles. See post from [George Kagan and FdM](https://stackoverflow.com/questions/39894291/how-to-change-text-not-font-size-according-to-screen-size-in-css) on Stack Overflow

<h2 align="left"><img src="docs/testing/bugs/bug-04-soln.jpg"></h2>

5. Duplicate categories

<h2 align="left"><img src="docs/testing/bugs/bug-05.jpg"></h2>

- Solved by converting category text to lowercase before checking if it exists in the database.

<h2 align="left"><img src="docs/testing/bugs/bug-05-soln.jpg"></h2>

6. Not listing plants in alphabetical order

<h2 align="left"><img src="docs/testing/bugs/bug-06.jpg"></h2>

- Solved by converting the plant name to lowercase before storing in the database because uppercase letters are listed before lowercase

<h2 align="left"><img src="docs/testing/bugs/bug-06-soln.jpg"></h2>

7. Materialize form validation issue for dropdown selection on Chrome with Windows 10/11. 

The dropdown fields for the Add Plant form showed the red underline on fields already selected. It did not affect the functionality as these records were still able to be added to the database. After discussion with the Alan McGee, Code Institute tutor, we decide that this was a Chrome browser issue in Windows 10 (my PC) and 11 (tutor's PC). I had already cleared the cache, deleted all history, restarted Chrome, restarted Windows, checked Chrome was the latest version. This issue was not present for Chrome on Mac, iPhone or Android. 

<h2 align="left"><img src="docs/testing/bugs/bug-07.jpg"></h2>

- Solved - As Windows with Chrome is a very popular setup, this issue could not be ignored, so I decided to set default values for the dropdown selections on the Add Plant form - this was inspired by the Edit Plant form not presenting this validation issue.

<h2 align="left"><img src="docs/testing/bugs/bug-07-soln.jpg"></h2>
<h2 align="left"><img src="docs/testing/bugs/bug-07-soln-form.jpg"></h2>

8. W3C error for section tag containing Flash messages in template, base.html

<h2 align="left"><img src="docs/testing/bugs/bug-08.jpg"></h2>

- Solved by replacing the section tags with div ones

<h2 align="left"><img src="docs/testing/bugs/bug-08-soln.jpg"></h2>

9. W3C error on add_plant.html for option element of select element with a required attribute

<h2 align="left"><img src="docs/testing/bugs/bug-09.jpg"></h2>

- Solved by removing the required attribute - there is already a default selected

<h2 align="left"><img src="docs/testing/bugs/bug-09-soln.jpg"></h2>

10. W3C error on edit_plant.html for select element cannot have more than one select option descendent

<h2 align="left"><img src="docs/testing/bugs/bug-10.jpg"></h2>

- Solved by setting the value attribute as an empty string as the value is selected in for-loop of the Jinja code

<h2 align="left"><img src="docs/testing/bugs/bug-10-soln.jpg"></h2>

11. User mistypes Unsplash image link

- Solved by adding a backup imaging informing the user of the broken link. See [Setting a Fallback Image in HTML for Broken or Missing Images](https://www.codu.co/articles/setting-a-fallback-image-in-html-for-broken-or-missing-images-otom_bhg) by Niall Maher on Codú

<h2 align="left"><img src="docs/testing/bugs/bug-11-soln.jpg"></h2>

---

## Known Issues

1. The error was removed by running the site on Chrome in Incognito mode.

<h2 align="left"><img src="docs/testing/bugs/bug-00.jpg"></h2>


Stack Overflow user [Chrostip Schaejn](https://stackoverflow.com/questions/72494154/a-listener-indicated-an-asynchronous-response-by-returning-true-but-the-messag) advised that this error was cause by various Chrome extensions.

2. Fallback image for when a user mistypes the image address on forms

<h2 align="left"><img src="static/img/fallback_image.jpg"></h2>

This causes a 404 error in the console and should only be used as an indicator of a broken link. The moderator should discourage users from leaving any links broken.

---

