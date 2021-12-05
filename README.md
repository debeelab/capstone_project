# Casting Agency - Capstone Project
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

### Models
- Movies with attributes: title and release date
- Actors with attributes: name, age and gender
    
## Getting Started
### Installing Dependencies
#### Python 3.7+
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) 

#### Virtual Enviornment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) 

#### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by running:

    pip3 install -r requirements.txt

This will install all of the required packages we selected within the requirements.txt file.

##### Key Dependencies
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. You'll primarily work in `app.py` and can reference models.py. 

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Database Setup
To test endpoints, with Postgres running, restore a database using the castingagency.sql file provided. From the file directory in terminal run:
```
psql castingagency < castingagency.sql
```

## Running the server
From within the `file directory` first ensure you are working using your created virtual environment.


Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py
```
   
On windows you should run this command instead:
 ```bash
 set FLASK_APP=app.py;
 ```
    
Also set the following environmental variable for Auth0
```bash 
export AUTH0_DOMAIN='your_auth0_domain'
export API_AUDIENCE='auth0_audience'
export DATABASE_URI_TEST='your_test_db'
```
To run the server, execute:

 ```bash
 flask run --reload
 ```

- The `--reload` flag will detect file changes and restart the server automatically.
- Or you can run the `python app.py` directly this will run your app.py automatically.


## Tasks
### Deployment
This app is hosted and deployed on heroku inorder to access it from cloud, as well as share with others. The link to the app is at [Capstone Casting Agency](http://capstone-agency-app.herokuapp.com/)

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
    
  ### Roles
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
>https://jamb-fsnd.us.auth0.com/authorize?audience=castingagency&response_type=token&client_id=p1U7BG6MaJxHOSEJzrdNwFsVrC9CZjnR&redirect_uri=https://capstone-agency-app.herokuapp.com/ 
>```

    
## Tests
- One test for success behavior of each endpoint
- One test for error behavior of each endpoint
- At least two tests of RBAC for each role
### Testing
To run the tests, run
```
python3 capstone_test_app.py
``` 

## Endpoints documentation
### Endpoints
- GET /actors and /movies
- DELETE /actors/ and /movies/
- POST /actors and /movies and
- PATCH /actors/ and /movies/

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
                  "release_date": "2020-05-04 00:00:00",
                  "title": "Blood Diamond"
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
            "age": 40,
            "gender": "male",
            "id": 1,
            "name": "Will Smith"
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
        "id_deleted": 2,
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
        "id_deleted": 1,
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
            "id": 5,
            "release_date": "2010-02-01 00:00:00",
            "title": "Tom and Jerry"
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
            "age": 55,
            "gender": "other",
            "id": 4,
            "name": "Harry Potter"
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
                "id": 3,
                "release_date": "2008-03-01 00:00:00",
                "title": "Fighting Temptation"
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
        "age": 39,
        "gender": "Female",
        "id": 2,
        "name": "Juno"
    },
    "status_code": 200,
    "status_message": "OK",
    "success": true
}
```
