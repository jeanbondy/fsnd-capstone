from dotenv import load_dotenv
import os
import logging

load_dotenv()
ENV = os.environ.get('ENV')

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.


# Connect to the database

class Config:
    # Flask
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.urandom(32)
    DEBUG = False
    AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
    ALGORITHMS = os.environ.get('ALGORITHMS')
    API_AUDIENCE = os.environ.get('API_AUDIENCE')

class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
