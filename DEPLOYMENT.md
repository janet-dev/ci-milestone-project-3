## Deployment

Notes sourced from [Tim Nelson](https://github.com/TravelTimN/ci-milestone04-dcd/edit/main/README.md)

### Local Deployment

Please note - in order to run this project locally on your own system, you will need the following installed:
- [Python3](https://www.python.org/downloads) to run the application.
- [PIP](https://pip.pypa.io/en/stable/installation/) to install all app requirements.
- Any IDE such as [Microsoft Visual Studio Code](https://code.visualstudio.com).
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control.
- [MongoDB](https://www.mongodb.com) to develop your own database either locally or remotely on MongoDB Atlas.

Next, there's a series of steps to take in order to proceed with local deployment:

- Clone this GitHub repository by either clicking the green *Clone or download* button and downloading the project as a zip-file (remember to unzip it first)

- Navigate to the correct file location after unpacking the files
    - `cd <path to folder>`
- Create a `env.py` file with your credentials. 

	<h2 align="left"><img src="docs/pictures/deploy-env.jpg"></h2>

	Be sure to include your *MONGO_URI* and *SECRET_KEY* values.
- Install all requirements from the requirements.txt file using this command:
    - `sudo -H pip3 -r requirements.txt`

	<h2 align="left"><img src="docs/pictures/deploy-requirements.jpg"></h2>

- Sign up for a free account on [MongoDB](https://www.mongodb.com) and create a new Database called **vazy_garden**. The *Collections* (tables) in that database should be as follows:

**plants**
```
_id: <ObjectId>
category_name: <string>
plant_name: <string>
plant_description: <string>
sow: <string>
is_edible: <string>
is_done: <string>
animal_name: <string>
link: <string>
seed_link: <string>
created_by: <string>
```

**categories**
```
_id: <ObjectId>
category_name: <string>
```

**months**
```
_id: <ObjectId>
sow: <string>
```

**animals**
```
_id: <ObjectId>
animal_name: <string>
```

**users**
```
_id: <ObjectId>
username: <string>
password: <string>
```

- You should now be able to launch your app using the following command in your terminal:
    - `flask run`
- The app should now be running on *localhost* on an address similar to `http://127.0.0.1:5000`. Simply copy/paste this into the browser of your choice! More information [here](https://code.visualstudio.com/docs/python/tutorial-flask).

### Remote Deployment

This site is currently deployed on [Heroku](https://www.heroku.com/) using the **main** branch on GitHub. To implement this project on Heroku, the following steps were taken:

1. Create a **requirements.txt** file so Heroku can install the required dependencies to run the app.
    - `sudo pip3 freeze --local > requirements.txt`

	<h2 align="left"><img src="docs/pictures/deploy-requirements.jpg"></h2>

2. Create a **Procfile** to tell Heroku what type of application is being deployed, and how to run it.
    - `echo web: python app.py > Procfile`

	<h2 align="left"><img src="docs/pictures/deploy-procfile.jpg"></h2>

	- Make sure there are no blanks lines at the end of the file!

3. Sign up for a free Heroku account, create your project app, and click the **Deploy** tab, at which point you can *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.

4. In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables as follows:
    - **IP** : 0.0.0.0
    - **PORT** : 5000
    - **SECRET_KEY** : <your_own_secret_key>
    - **MONGO_URI** : <link_to_your_MongoDB>
    - **MONGO_DBNAME** : vazy_garden
    - **DEBUG** : False

5. Your app should be successfully deployed to Heroku at this point.

