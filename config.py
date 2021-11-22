import os
# Enable debug mode.
DEBUG = True
# Connect to the database
database_filename = "database.db"
# Get the folder path where the script runs.
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))


# IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = database_path
SQLALCHEMY_TRACK_MODIFICATIONS = True
FLASK_ENV = "development"
SQLALCHEMY_ECHO = True
DEVELOPMENT = True


# class TestingConfig(Config):
#     FLASK_ENV = "testing"
#     TESTING = True
#     DEBUG = True
#     SQLALCHEMY_ECHO = False
#     SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI_TEST")

