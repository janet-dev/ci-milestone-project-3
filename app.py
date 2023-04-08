"""
Diploma in Web Application Development: Backend (Data Centric) Development
Milestone Project 3 :   CRUD app developed with the Flask mini-framework,
                        Materialize CSS and Mongo Atlas Database.
                        This MVP app allows registered users to store
                        information on plant seeds they wish to sow for the
                        coming year. A search facility enables them to see
                        which seeds should be sown in a particular month or
                        which plants are suitable as animal feed.
File name:  app.py
Created:    April, 2023
Author:     Janet Dornan
Credit:     Tim Nelson, Code Institite
Source:     https://github.com/Code-Institute-Solutions/TaskManagerAuth
"""

import os
from functools import wraps
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from decorators import login_required_admin, login_required_user

if os.path.exists("env.py"):
    import env


app = Flask(__name__)       # instance of Flask stored in variable 'app'

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.errorhandler(404)
def page_not_found(error_404):
    '''
    An error handler is registered with the errorhandler() decorator
    for the status code 404 for page not found. Further info from:
    https://flask.palletsprojects.com/en/2.2.x/errorhandling/

    :param error_404:   page not found error raised
    :return:    rendered template for the 404 page,
                if an explicit error of 404 is raised
    '''
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error_500):
    '''
    An error handler is registered with the errorhandler() decorator
    for the status code 500 internal server error. Further info from:
    https://flask.palletsprojects.com/en/2.2.x/errorhandling/

    :param error_500:   Internal Server Error raised
    :return:    rendered template for the 500 page,
                if an explicit error of 500 is raised
    '''
    return render_template('500.html'), 500


@app.route("/")
@app.route("/get_plants")
def get_plants():
    '''
    This function collects all the plant info from MongoDB.
    This will be used for the home page

    :return:    Rendered home page, displaying all plants
    '''
    plants = list(mongo.db.plants.find().sort("plant_name", 1))
    return render_template("plants.html", plants=plants)


@app.route("/about")
def about():
    '''
    This function displays the About and Instructions page

    :return:    Rendered about page
    '''
    return render_template("about.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    '''
    This function enables the user to search through all plants
    using key words in the fields plant name, description,
    sow month and animal to feed.

    :return:    Rendered home page with the filtered plants
    '''
    query = request.form.get("query")
    plants = list(mongo.db.plants.find({"$text": {"$search": query}}))
    return render_template("plants.html", plants=plants)


@app.route("/search_profile", methods=["GET", "POST"])
def search_profile():
    '''
    This function enables the user to search through their own plants
    using key words in the fields plant name, description,
    sow month and animal to feed.

    :return:    Rendered profile page with the filtered plants
    '''
    query = request.form.get("query")
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        plants = list(mongo.db.plants.find({"$text": {"$search": query}}))
        return render_template(
            "profile.html", username=username, plants=plants)

    plants = list(mongo.db.plants.find().sort("plant_name", 1))
    return render_template("plants.html", plants=plants)


@app.route("/register", methods=["GET", "POST"])
def register():
    '''
    This function enables new users to register their name and password,
    in order to create their own profile page.
    Initially the function checks if the user exists,
    if yes, they are told this and the register page reloads.
    Otherwise the username and hashed password are added to the database.
    New user's name is put into the session cookie and
    they are sent to their profile page.

    :return:    register route, or
                profile route for new user
    '''
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register_user)

        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    '''
    This function initially checks the db if the user is already registered;
    if yes, the password is verified and they are greeted
    with a welcome message on their profile page.
    Otherwise they are directed to the register page if user does not exist
    or the login page if the password is incorrect

    :return:    profile route if login successful, or
                login route if password incorrect, or
                register route if user does not exist
    '''
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                welcome = request.form.get("username").capitalize()
                flash(f"Welcome, {welcome}")
                session['logged_in'] = True
                return redirect(url_for("profile", username=session["user"]))
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

        flash("Incorrect Username and/or Password")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required_user
def profile(username):
    '''
    This function is wrapped with decorator which enforces user security
    for protecting post owners.
    Plant info is fetched from the db for the current logged in user.

    :param username:    session user's username retrieved from db
    :return:    rendered profile page for current user, or
                login route if not
    '''
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        plants = list(mongo.db.plants.find().sort("plant_name", 1))
        return render_template(
            "profile.html", username=username, plants=plants)

    return redirect(url_for("login"))


@app.route("/logout")
@login_required_user
def logout():
    '''
    This function is wrapped with decorator which enforces user security
    - a user who is not logged in, should not be able to log out.
    The current user will be removed from the session on logout and
    redirected to the login page.

    :return: login route
    '''
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_plant", methods=["GET", "POST"])
@login_required_user
def add_plant():
    '''
    This function is wrapped with decorator which enforces user security
    for protecting post owners.
    This functionality enables the user to add plants to their profile page,
    via the Add Plant form. If the form is submitted, then the plant dictionary
    is written to the database.

    :return: home page route
    '''
    if request.method == "POST":
        is_edible = "on" if request.form.get("is_edible") else "off"
        is_done = "on" if request.form.get("is_done") else "off"

        plant = {
            "category_name": request.form.get("category_name"),
            "plant_name": request.form.get("plant_name"),
            "plant_description": request.form.get("plant_description"),
            "sow": request.form.get("sow"),
            "is_done": is_done,
            "is_edible": is_edible,
            "animal_name": request.form.get("animal_name"),
            "link": request.form.get("link"),
            "seed_link": request.form.get("seed_link"),
            "created_by": session["user"]
        }
        mongo.db.plants.insert_one(plant)
        flash("Plant Successively Added")
        return redirect(url_for("get_plants"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    months = mongo.db.months.find()
    animals = mongo.db.animals.find().sort("animal_name", 1)

    return render_template(
        "add_plant.html",
        categories=categories,
        months=months,
        animals=animals)


@app.route("/edit_plant/<plant_id>", methods=["GET", "POST"])
def edit_plant(plant_id):
    '''
    This function enables the user to edit their own plants,
    via the Edit Plant form. If the form is submitted, then the plant
    dictionary is written to the database.

    :return:    home page route
    '''
    plant = mongo.db.plants.find_one({"_id": ObjectId(plant_id)})

    # Code from CI video DBMS Masterclass 2
    if "user" not in session or session["user"] != plant["created_by"]:
        flash("You can only edit your own tasks!")
        return redirect(url_for("get_plants"))

    if request.method == "POST":
        is_edible = "on" if request.form.get("is_edible") else "off"
        is_done = "on" if request.form.get("is_done") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "plant_name": request.form.get("plant_name"),
            "plant_description": request.form.get("plant_description"),
            "sow": request.form.get("sow"),
            "is_edible": is_edible,
            "is_done": is_done,
            "animal_name": request.form.get("animal_name"),
            "link": request.form.get("link"),
            "seed_link": request.form.get("seed_link"),
            "created_by": session["user"]
        }
        mongo.db.plants.replace_one({"_id": ObjectId(plant_id)}, submit)
        flash("Plant Successively Updated")
        return redirect(url_for("get_plants"))

    categories = mongo.db.categories.find().sort("category_name")
    months = mongo.db.months.find()
    animals = mongo.db.animals.find().sort("animal_name", 1)

    return render_template(
        "edit_plant.html",
        plant=plant,
        categories=categories,
        months=months,
        animals=animals)


@app.route("/delete_plant/<plant_id>", methods=["GET", "POST"])
def delete_plant(plant_id):
    '''
    This function enables the user to delete their own plants,
    via the Delete button on their plant card.

    :return:    home page route
    '''
    plant = mongo.db.plants.find_one({"_id": ObjectId(plant_id)})

    # Code from CI video DBMS Masterclass 2
    if "user" not in session or session["user"] != plant["created_by"]:
        flash("You can only delete your own tasks!")
        return redirect(url_for("get_plants"))

    if request.method == "POST":
        mongo.db.plants.delete_one({"_id": ObjectId(plant_id)})
        flash("Plant Successively Deleted")
        return redirect(url_for("get_plants"))

    return render_template("delete_plant.html", plant=plant)


@app.route("/get_categories")
@login_required_admin
def get_categories():
    '''
    This function is wrapped with decorator which enforces admin security
    for protecting the administrator tasks.
    Only the admin can view the categories page.

    :return:    rendered categories page for admin user only
    '''
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
@login_required_admin
def add_category():
    '''
    This function is wrapped with decorator which enforces admin security
    for protecting the administrator tasks.
    Only the admin can view and add a category.

    :return:    rendered categories page for admin user only
    '''
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG"))
