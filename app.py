import os
from flask import (
    Flask, flash, render_template,
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


@app.route("/")
@app.route("/get_plants")
def get_plants():
    plants = list(mongo.db.plants.find())
    return render_template("plants.html", plants=plants)


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
def profile(username):
    # grab the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        # go to profile
        return render_template("profile.html", username=username)

    # else go to login
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    # session.clear()  # to remove all session cookies applicable to this app
    session.pop("user")  # to only remove session cookie for 'user'
    return redirect(url_for("login"))


@app.route("/add_plant", methods=["GET", "POST"])
def add_plant():
    if request.method == "POST":
        plant = {
            "category_name": request.form.get("category_name"),
            "plant_name": request.form.get("task_name"),
            "plant_description": request.form.get("task_description"),
            "sow": request.form.get("sow"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(plant)
        flash("Task Successively Added")
        return redirect(url_for("get_plants"))

    categories = mongo.db.categories.find().sort("category_name")
    months = mongo.db.months.find()

    return render_template("add_plant.html", categories=categories, months=months)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
# on final deployment change to *** debug=False ***
