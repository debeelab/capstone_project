Casting Agency Capstone Project
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

Casting Agency Specifications
Models
Movies with attributes title and release date
Actors with attributes name, age and gender
Endpoints
GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/
Roles
Casting Assistant
Can view actors and movies
Casting Director
All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies
Executive Producer
All permissions a Casting Director has and…
Add or delete a movie from the database
Tests
One test for success behavior of each endpoint
One test for error behavior of each endpoint
At least two tests of RBAC for each role
Getting Started
Installing Dependencies
Python 3.7+
Follow instructions to install the latest version of python for your platform in the python docs

Virtual Enviornment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

By using anaconda you can create your envirement by running conda create -n name_of_your_env

Then activate it by running conda activate name_of_your_env
Install all your dependencies on this env :).
To deactivate the env run conda deactivate
PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the /backend directory and running:

pip3 install -r requirements.txt
This will install all of the required packages we selected within the requirements.txt file.

Key Dependencies
Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.

SQLAlchemy and Flask-SQLAlchemy are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in ./src/database/models.py. We recommend skimming this code first so you know how to interface with the Drink model.

jose JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

Running the server
From within the ./src directory first ensure you are working using your created virtual environment.


Each time you open a new terminal session, run:

export FLASK_APP="flaskr:create_app('config.DevelopmentConfig')"
Also set the following environmental variable for Auth0

export AUTH0_DOMAIN='your_auth0_domain'
export API_AUDIENCE='auth0_audience'
export DATABASE_URI_DEV='developmenent_db_uri'
export DATABASE_URI='your_production_db'
export DATABASE_URI_TEST='your_test_db'

On windows you should run this command instead:

set FLASK_APP=app.py;

To run the server, execute:

flask run --reload
The --reload flag will detect file changes and restart the server automatically.
Or you can directly run it with python app.py and everythin will be done automatically.

Note: To run the app correctly you need to export all the global variables for the auth and token. To do so if you are in linux evn it is easy you have just to the setup bash script. But to make things more easier do everything from bash.


Tasks

Setup Auth0
Create a new Auth0 Account

Select a unique tenant domain

Create a new, single page web application

Create a new API

in API Settings:
Enable RBAC
Enable Add Permissions in the Access Token

Create new API permissions:

get:movies
get:actors
post:movies
post:actors
patch:movies
patch:actors
delete:movies
delete:actors
Create new roles for:

Casting Assistant
can get:movies get:actors
Casting director
All permissions a Casting Assistant has and…
Add or delete an actor from the database post:actors delete:actors
Modify actors or movies patch:actors delete:movies
Executive producer
Can perform all actions
Test your endpoints with Postman.

Register 3 users - assign the Casting Assistant role to the first one, Casting Director role to the second and Executive porducer to the last one.
Sign into each account and make note of the JWT.
Import the postman collection ./capstone-project.postman_collection.json
Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
Run the collection and correct any errors.
Export the collection overwriting the included one to be able to run with your own jwt :).
Note: to sign in and get the tokens for the diff roles type on your broser:

https://YOUR_DOMAIN/authorize?audience=API_IDENTIFIER&response_type=token&client_id=YOUR_CLIENT_ID&redirect_uri={{YOUR_CALLBACK_URI}}
Like for example in my case:

https://jamb-fsnd.auth0.com/authorize?audience=capstone-app&response_type=token&client_id=p1U7BG6MaJxHOSEJzrdNwFsVrC9CZjnR&redirect_uri=https://casting-agency-app.herokuapp.com/ 

Testing
To run the tests, run

python3 capstone_test_app.py

Deploy the application on heroku
To depoloy your application follow this document => Deploy an application on Heroku. he is a fast resume, after installing heroku, and heroku CLI

heroku loginto loggin into heroku
Update requirements.txt each time you add dependency pip freeze > requirements.txt
Setting up your environement varibales in setup.sh
Install Gunicorn (a pure-Python HTTP server for WSGI applications used to deploy the app) => pip install gunicorn
Create Procfile include one line to instruct Heroku correctly for us: web: gunicorn app:app. app is the application's entry point var in th main module.
To allow heroku run all your migrations to the database you have hosted on the platforme, your application need to include manage.py file. Create manage.py file that should contain the following code

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from database.models import db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
    
Istall those package to run the migrations
pip install flask_script
pip install flask_migrate
pip install psycopg2-binary
Remember to freeze the dependecies every after you installing those packages.

Run our local migrations using our manage.py file, to mirror how Heroku will run behind the scenes for us when we deploy our app
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
Your file structure should contains those files
> migrations
.gitignore
app.py
manage.py
models.py
Procfile
requirements.text
Setup.sh
