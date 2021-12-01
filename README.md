
# Casting Agency - Capstone Project
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## **Casting Agency Specifications**

### Models
- Movies with attributes: title and release date
- Actors with attributes: name, age and gender

### Endpoints
- GET /actors and /movies
- DELETE /actors/ and /movies/
- POST /actors and /movies and
- PATCH /actors/ and /movies/

### Roles
- Casting Assistant:
    * Can view actors and movies
- Casting Director:
    * All permissions a Casting Assistant has and…
    * Add or delete an actor from the database
    * Modify actors or movies
 - Executive Producer:
    * All permissions a Casting Director has and…
    * Add or delete a movie from the database
    
### Tests
- One test for success behavior of each endpoint
- One test for error behavior of each endpoint
- At least two tests of RBAC for each role
    
## Getting Started
### Installing Dependencies
#### Python 3.7+
Follow instructions to install the latest version of python for your platform in the [python docs]https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) 

#### Virtual Enviornment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) 

#### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by running:

    pip3 install -r requirements.txt

This will install all of the required packages we selected within the requirements.txt file.

##### Key Dependencies
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in ./src/database/models.py. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.


## Running the server
From within the `file directory` first ensure you are working using your created virtual environment.


Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
```
   
On windows you should run this command instead:
 ```bash
 set FLASK_APP=app.py;
 ```
    
Also set the following environmental variable for Auth0
```bash 
export AUTH0_DOMAIN='your_auth0_domain';
export API_AUDIENCE='auth0_audience';
export DATABASE_URI_DEV='developmenent_db_uri';
export DATABASE_URI_TEST='your_test_db';
```
To run the server, execute:

 ```bash
 flask run --reload
 ```

. The `--reload` flag will detect file changes and restart the server automatically.
. Or you can directly run it with `python app.py` and everythin will be done automatically.


### Tasks

### Setup Auth0
1. Create a new Auth0 Account

2. Select a unique tenant domain

3. Create a new, single page web application

4. Create a new API
    * in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token

5. Create new API permissions:
    - get:movies
    - get:actors
    - post:movies
    - post:actors
    - patch:movies
    - patch:actors
    - delete:movies
    - delete:actors
    
6. Create new roles for:
    * Casting Assistant
        - can get:movies get:actors
    * Casting director
        - All permissions a Casting Assistant has and…
        - Add or delete an actor from the database post:actors delete:actors
        - Modify actors or movies patch:actors delete:movies
    * Executive producer
        - Can perform all actions
        
7. Test your endpoints with Postman [Postman](https://getpostman.com). 
     * Register 3 users - assign the Casting Assistant role to the first one, Casting Director role to the second and Executive porducer to the last one.
    * Sign into each account and make note of the JWT.
    * Import the postman collection ./capstone-project.postman_collection.json
    * Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    * Run the collection and correct any errors.
    * Export the collection overwriting the included one to be able to run with your own jwt :).
   
> Note: to sign in and get the tokens for the diff roles type on your broser:
>```http
>https://YOUR_DOMAIN/authorize?audience=API_IDENTIFIER&response_type=token&client_id=YOUR_CLIENT_ID&redirect_uri={{YOUR_CALLBACK_URI}}
>```
>Like for example in my case:
>```http
>https://jamb-fsnd.us.auth0.com/authorize?audience=castingagency&response_type=token&client_id=p1U7BG6MaJxHOSEJzrdNwFsVrC9CZjnR&redirect_uri=https://casting-agency-app.herokuapp.com/ 
>```


## Testing
To run the tests, run
```
python3 capstone_test_app.py
```
   
## Deploy the application on heroku
To depoloy your application follow this document => [Deploy an application on Heroku]() . he is a fast resume, after installing heroku, and heroku CLI

1. `heroku login` loginto loggin into heroku
2. Update requirements.txt each time you add dependency `pip freeze > requirements.txt`
3. Setting up your environement varibales in `setup.sh`
4. Install Gunicorn (a pure-Python HTTP server for WSGI applications used to deploy the app) => `pip install gunicorn`
5. Create `Procfile` include one line to instruct Heroku correctly for us: `web: gunicorn app:app`. app is the application's entry point var in th main module.
6. To allow heroku run all your migrations to the database you have hosted on the platforme, your application need to include `manage.py` file. Create `manage.py` file that should contain the following code.

         from flask_script import Manager
         from flask_migrate import Migrate, MigrateCommand

         from app import app
         from database.models import db

         migrate = Migrate(app, db)
         manager = Manager(app)

         manager.add_command('db', MigrateCommand)

         if __name__ == '__main__':
               manager.run()
    
7. Install those package to run the migrations

         pip install flask_script
         pip install flask_migrate
         pip install psycopg2-binary
    
> Remember to freeze the dependecies every after you installing those packages.

8. Run our local migrations using our `manage.py` file, to mirror how Heroku will run behind the scenes for us when we deploy our app.

       python manage.py db init
       python manage.py db migrate
       python manage.py db upgrade
    
9. Your file structure should contains those files
      ```bash
      > migrations
      > database
      .gitignore
      app.py
      manage.py
      Procfile
      requirements.text
      setup.sh
      ```
10. Crete heroku app => `heroku create name_of_your_app`
    
11. Add git remote for heroku to local repo that you get from the previous command or you can get it from heroku web site on by clicking on your app there and click on settings. You will find it there :). => `git remote add heroku heroku_git_url` 

> If you the previous commend through an error fata remote already exsit because you created a previous app just run thsi commend and you fix the issue => `git remote set-url heroku heroku_git_url`

12. Add postgresql add on for your database => `heroku addons:create heroku-postgresql:hobby-dev --app name_of_your_application`
    
> Run the under command to check your config vars in heroku `heroku config --app name_of_your_application`

13. Push it :D. After you push everything to your git now push from git to heroku => `git push heroku master`

> To check if you everthing is staged use `git status`

14. Run migrations: Once your app is deployed, run migrations by running: `heroku run python manage.py db upgrade --app name_of_your_application`

And that is it all. Congratulation :D. Now we have a live app :D. Open it from the heroku dashboard and see it live :D. Make additional requests using curl or Postman as you build your application and make more complex endpoints :).


## API Reference
### Getting Started
- **Base URL**: Actually, this app can be run locally and it is hosted also as a base URL using heroku (the deplyed application URL is : https://capstone-agency-app.herokuapp.com/). The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration.
- **Authentication**: This version of the application require authentication or API keys using Auth0 (Ps: The setup is givin in setup Auth0 section).

### Error Handling
Errors are returned as JSON object in the following format:
```json
{
            "success": False,
            "error": 400,
            "message": "bad request"
}
```

The API will return four(04) error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 405: Method Not allowed
- 422: Not Processable
- 401: AuthError Unauthorized error
- 403: AuthError Permission not found

## Endpoints documentation
### GET '/movies'
- Fetches a dictionary of movies
- Required URL Arguments: None
- Required Data Arguments: None
- Returns: Returns Json data about movies
- Success Response:
```json
{
            "movies": [
               {
                   "id": 1,
                  "release_date": "Sun, 01 Jan 2012 00:00:00 GMT",
                  "title": "Lion King"
               },
        {
            "id": 2,
            "release_date": "Mon, 12 Aug 2019 00:00:00 GMT",
            "title": "Joker"
        },
        {
            "id": 3,
            "release_date": "Mon, 12 Dec 2011 00:00:00 GMT",
            "title": "Frozen"
        },
        {
            "id": 4,
            "release_date": "Wed, 01 Aug 2012 00:00:00 GMT",
            "title": "Yes Man"
        }
    ],
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```
### GET '/actors'
- Fetches a dictionary of actors
- Required Data Arguments: None
- Returns: Json data about actors
- Success Response:

```json
{
    "actors": [
        {
            "age": 36,
            "gender": "male",
            "id": 1,
            "name": "Edward"
        },
        {
            "age": 25,
            "gender": "other",
            "id": 2,
            "name": "David"
        },
        {
            "age": 35,
            "gender": "female",
            "id": 3,
            "name": "Jeff"
        }
    ],
    "status_code": 200,
    "status_message": "OK",
    "success": true
    }
```

### DELETE '/movies/<int:movie_id>'
- Deletes the movie_id of movie
- Required URL Arguments: movie_id: movie_id_integer
- Required Data Arguments: None
- Returns: Json data about the deleted movie's ID
- Success Response:
 ```json
 {
        "id_deleted": 5,
        "status_code": 200,
        "status_message": "OK",
        "success": true
    }
```

### DELETE '/actors/<int:actor_id>'
- Deletes the actor_id of actor
- Required URL Arguments: actor_id: actor_id_integer
- Required Data Arguments: None
- Returns: Json data about the deleted actor's ID
- Success Response:
 ```json
 {
        "id_deleted": 4,
        "status_code": 200,
        "status_message": "OK",
        "success": true
}
```

### POST '/movies'
- Post a new movie in a database.
- Required URL Arguments: None
- Required Data Arguments: Json data
- Success Response:
 ```json
 {
        "movie": {
            "id": 6,
            "release_date": "Thu, 01 Aug 2002 00:00:00 GMT",
            "title": "Toy Story"
        },
        "status_code": 200,
         "status_message": "OK",
        "success": true
}
```

### POST '/actors'
- Post a new actor in a database.

- Required URL Arguments: None

- Required Data Arguments: Json data

- Success Response:
 ```json
 {
        "actor": {
            "age": 18,
            "gender": "other",
            "id": 4,
            "name": "Penny"
        },
        "status_code": 200,
        "status_message": "OK",
        "success": true
 }
 ```

### PATCH '/movies/<int:movie_id>'
- Updates the movie_id of movie
- Required URL Arguments: movie_id: movie_id_integer
- Required Data Arguments: None
- Returns: Json data about the updated movie
- Success Response:
```json
{
        "movie": {
                "id": 5,
                "release_date": "Wed, 05 Dec 2018 00:00:00 GMT",
                "title": "Avenger"
                },
                "status_code": 200,
                "status_message": "OK",
                "success": true
}
```

### PATCH '/actors/<int:actor_id>'
- Updates the actor_id of actor
- Required URL Arguments: actor_id: actor_id_integer
- Required Data Arguments: None
- Returns: Json data about the deleted actor's ID
- Success Response:
```json
{
        "actor": {
        "age": 28,
        "gender": "other",
        "id": 4,
        "name": "Penny"
    },
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```
