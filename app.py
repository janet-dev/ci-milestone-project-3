import os
from functools import wraps
from flask import (
    Flask, flash, g, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)       # instance of Flask stored in variable 'app'

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


def login_required_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session["user"] == "admin":
            return f(*args, **kwargs)
        else:
            flash("Access Denied")
            return redirect(url_for('login'))

    return decorated_function


def login_required_user(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login")
            return redirect(url_for('login'))

    return decorated_function


@app.route("/")
@app.route("/get_plants")
def get_plants():
    plants = list(mongo.db.plants.find().sort("plant_name", 1))
    return render_template("plants.html", plants=plants)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    plants = list(mongo.db.plants.find({"$text": {"$search": query}}))
    return render_template("plants.html", plants=plants)


@app.route("/search_profile", methods=["GET", "POST"])
def search_profile():
    query = request.form.get("query")
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        plants = list(mongo.db.plants.find({"$text": {"$search": query}}))
        return render_template(
            "profile.html", username=username, plants=plants)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # else register user and hash the password
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
        # send user to profile page
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                session['logged_in'] = True
                # send user to profile page
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # existing username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    # Don't need to write any logic for an 'else' statement here
    # it defaults to the "GET" method,
    # which acts automatically as the 'else' condition
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required_user
def profile(username):
    # grab the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        # go to profile
        plants = list(mongo.db.plants.find().sort("sow", 1))
        return render_template(
            "profile.html", username=username, plants=plants)

    # else go to login
    return redirect(url_for("login"))


@app.route("/logout")
@login_required_user
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    # session.clear()  # to remove all session cookies applicable to this app
    session.pop("user")  # to only remove session cookie for 'user'
    return redirect(url_for("login"))


@app.route("/add_plant", methods=["GET", "POST"])
@login_required_user
def add_plant():
    if request.method == "POST":
        is_edible = "on" if request.form.get("is_edible") else "off"
        plant = {
            "category_name": request.form.get("category_name"),
            "plant_name": request.form.get("plant_name"),
            "plant_description": request.form.get("plant_description"),
            "sow": request.form.get("sow"),
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
    plant = plant = mongo.db.plants.find_one({"_id": ObjectId(plant_id)})

    # Code from CI video DBMS Masterclass 2
    if "user" not in session or session["user"] != plant["created_by"]:
        flash("You can only edit your own tasks!")
        return redirect(url_for("get_plants"))

    if request.method == "POST":
        is_edible = "on" if request.form.get("is_edible") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "plant_name": request.form.get("plant_name"),
            "plant_description": request.form.get("plant_description"),
            "sow": request.form.get("sow"),
            "is_edible": is_edible,
            "animal_name": request.form.get("animal_name"),
            "link": request.form.get("link"),
            "seed_link": request.form.get("seed_link"),
            "created_by": session["user"]
        }
        mongo.db.plants.replace_one({"_id": ObjectId(plant_id)}, submit)
        flash("Plant Successively Updated")

    categories = mongo.db.categories.find().sort("category_name")
    months = mongo.db.months.find()
    animals = mongo.db.animals.find().sort("animal_name", 1)
    return render_template(
        "edit_plant.html",
        plant=plant,
        categories=categories,
        months=months,
        animals=animals)


@app.route("/delete_plant/<plant_id>")
def delete_plant(plant_id):
    plant = plant = mongo.db.plants.find_one({"_id": ObjectId(plant_id)})

    # Code from CI video DBMS Masterclass 2
    if "user" not in session or session["user"] != plant["created_by"]:
        flash("You can only delete your own tasks!")
        return redirect(url_for("get_plants"))

    mongo.db.plants.delete_one({"_id": ObjectId(plant_id)})
    flash("Plant Successively Deleted")
    return redirect(url_for("get_plants"))


@app.route("/get_categories")
@login_required_admin
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
@login_required_admin
def add_category():
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
        debug=True)
# on final deployment change to *** debug=False ***
