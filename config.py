from dotenv import load_dotenv
import os

load_dotenv()
ENV = os.environ.get('ENV')

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.


# Connect to the database

class Config:
    # Flask
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = ('SECRET_KEY')
    DEBUG = False

class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
