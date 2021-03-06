from dotenv import load_dotenv
from os import environ, path
import os
import logging

ENV = environ.get('ENV')

# Grabs the folder where the script runs.
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    # Flask
    SECRET_KEY = os.urandom(32)
    DEBUG = False

    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Auth0
    AUTH0_DOMAIN = environ.get('AUTH0_DOMAIN')
    ALGORITHMS = environ.get('ALGORITHMS')
    API_AUDIENCE = environ.get('API_AUDIENCE')
    AUTH0_LOGIN_URL = f'https://{environ.get("AUTH0_DOMAIN")}/authorize?audience={environ.get("API_AUDIENCE")}&response_type=token&client_id={environ.get("AUTH0_CLIENT_ID")}&redirect_uri={environ.get("AUTH0_CALLBACK_URL")}'

    # Auth0 Tokens
    JWT_EXEC_PROD = environ.get('JWT_EXEC_PROD')
    JWT_CAST_DIR = environ.get('JWT_CAST_DIR')
    JWT_CAST_ASSIST = environ.get('JWT_CAST_ASSIST')

    # App
    PAGINATION = 10


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL').replace("postgres://", "postgresql://", 1)
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    SQLALCHEMY_DATABASE_URI = environ.get('DEV_DATABASE_URI')
    SQLALCHEMY_ECHO = True
    DEBUG = True
    TESTING = True


class TestingConfig(Config):
    FLASK_ENV = 'development'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get('TEST_DATABASE_URI')