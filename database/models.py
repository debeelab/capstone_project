import os
from sqlalchemy import Column, String, Integer, DateTime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import datetime

# database_name ='capstone_project'
# database_path = 'postgresql://{}:{}@{}/{}'.format('udacitystudent', 'postgres','localhost:5432', database_name)


db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


# def setup_db(app):
#     # Connect to the database
#     database_filename = "database.db"
#     # Get the folder path where the script runs.
#     project_dir = os.path.dirname(os.path.abspath(__file__))
#     database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))


#     # IMPLEMENT DATABASE URL
#     SQLALCHEMY_DATABASE_URI = database_path
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     # Enable debug mode.
    
#     db.app = app
#     db.init_app(app)
#     db.create_all()


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename
    variable to have multiple verisons of a database
'''


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


'''
Movie
a persistent movie entity, extends the base SQLAlchemy Model
'''

class Movie(db.Model):
    __tablename__ = "movies"
    
    #Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    #String title
    title = Column(String(80), nullable=False)
    # Release date
    release_date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow) 
    actors = db.relationship("Actor", backref="movies")             # parent-child relationship btw the Movie and Actor


    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    '''
    insert()
        inserts a new model into a database
        the model must have a unique name
        the model must have a unique id or null id
        EXAMPLE
            movie = Movie(title=req_title, realse_date=req_realse_date)
            movie.insert()
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()

    
    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            movie = Movie.query.filter(Movie.id == id).one_or_none()
            movie.title = 'New Movie'
            movie.update()
    '''
    def update(self):
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
        the model must exist in the database
        EXAMPLE
            movie = Movie(title=req_title,realse_date=req_realse_date)
            movie.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()


    '''
    get_movie(self)
        json form representation of the Movie model
    '''

    def get_movie(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date
            
        }

    def __repr__(self):
        return json.dumps(self.get_movie())
        # return "<Movies: {}, {}, {}>".get_movie(self.id, self.title, self.release_date)


'''
Actor
a persistent actor entity, extends the base SQLAlchemy Model
'''

class Actor(db.Model):
    __tablename__ = "actors"

    #Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    #String name
    name = Column(String(80), nullable=False)
    # Integer age
    age = Column(Integer(), nullable=False)
    #String gender
    gender = Column(String(6), nullable=False)
    # Add movie as foreign key for actor model
    movie_id = Column(Integer(), db.ForeignKey("movies.id"))

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.movie_id = movie_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    get_actor(self)
        json form representation of the Actor model
    '''

    def get_actor(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    def __repr__(self):
        return json.dumps(self.get_actor())