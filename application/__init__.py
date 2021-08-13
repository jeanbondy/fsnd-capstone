# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#
import logging
from logging import FileHandler, Formatter
import dateutil.parser
import babel.dates
from flask import Flask, jsonify
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config
from application.auth.auth import AuthError
from os import environ

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

# Globally accessible libraries
db = SQLAlchemy()
migrate = Migrate()
moment = Moment()


def init_app():
    app = Flask(__name__)

    if config.ENV == "development":
        app.config.from_object(config.DevelopmentConfig)
    elif config.ENV == "testing":
        app.config.from_object(config.TestingConfig)
    else:
        # production is fallback
        app.config.from_object(config.ProductionConfig)

    # initialize plugins
    db.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)

    ogg = app.config['SQLALCHEMY_DATABASE_URI']
    ugg = environ.get('XATABASE_URL')
    zog = environ.get('DATABASE_URL')
    print(f'database {ogg}')
    print(f'xatabase_url {ugg}')
    print(f'database_url {zog}')

    with app.app_context():
        from application.models.actors import Actor
        from application.models.movies import Movie
        from application.home_bp.routes import home_bp
        from application.actor_bp.routes import actor_bp
        from application.movie_bp.routes import movie_bp
        app.register_blueprint(home_bp)
        app.register_blueprint(actor_bp)
        app.register_blueprint(movie_bp)
        app.jinja_env.filters['datetime'] = format_datetime

        if not app.debug:
            file_handler = FileHandler('error.log')
            file_handler.setFormatter(
                Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
            )
            app.logger.setLevel(logging.INFO)
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)
            app.logger.info('errors')


        @app.errorhandler(400)
        def bad_request(error):
            return jsonify({
                'success': False,
                'error': '400',
                'message': 'bad request'
            }), 400

        @app.errorhandler(404)
        def not_found(error):
            return jsonify({
                'success': False,
                'error': '404',
                'message': 'resource not found'
            }), 404

        @app.errorhandler(405)
        def not_allowed(error):
            return jsonify({
                'success': False,
                'error': '405',
                'message': 'method not allowed'
            }), 405

        @app.errorhandler(422)
        def unprocessable(error):
            return jsonify({
                'success': False,
                'error': '405',
                'message': 'unprocessable'
            }), 405

        @app.errorhandler(500)
        def server_error(error):
            return jsonify({
                'success': False,
                'error': '500',
                'message': 'server error'
            })

        @app.errorhandler(AuthError)
        def handle_auth_error(e):
            return jsonify({
                "success": False,
                "error": e.status_code,
                'message': e.error
            }), e.status_code

        return app

# ----------------------------------------------------------------------------#
# Filters.
# ----------------------------------------------------------------------------#

def format_datetime(value, date_format='medium'):
    date = dateutil.parser.parse(value)
    if date_format == 'full':
        date_format = "EEEE MMMM, d, y 'at' h:mma"
    elif date_format == 'medium':
        date_format = "EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, date_format, locale='en')
