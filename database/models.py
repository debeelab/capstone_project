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

def setup_db(app):
    db.app = app
    db.init_app(app)
    # db.create_all()

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename
    variable to have multiple verisons of a database
'''

def db_drop_and_create_all():
    db.drop_all()
    # db.create_all()

'''
Extend the base Model class to add common methods
'''
class inheritedCastingAgencyModel(db.Model):
    __abstract__ = True

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
'''
Movie
a persistent movie entity, extends the base SQLAlchemy Model
'''

class Movie(inheritedCastingAgencyModel):
    id: int
    title: String
    release_date:DateTime
    actor_id: int

    __tablename__ = "movies"
    
    #Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    #String title
    title = Column(String(80), nullable=False)
    # Release date
    release_date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow) 
    actor_id = db.relationship("Actor", backref="movies")             # parent-child relationship btw the Movie and Actor


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
class Actor(inheritedCastingAgencyModel):
    id: int
    name: String
    age: int
    gender:String
    movie_id: int

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

    # def __init__(self, name, age, gender):
    #     self.name = name
    #     self.age = age
    #     self.gender = gender
    #     self.movie_id = movie_id

    # def insert(self):
    #     db.session.add(self)
    #     db.session.commit()

    # def update(self):
    #     db.session.commit()

    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()

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