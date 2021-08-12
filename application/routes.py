from flask import current_app as app
from flask import jsonify
from application.auth.auth import AuthError

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/')
def index():
    return "hello"



