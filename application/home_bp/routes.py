# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#
from flask import current_app as app, redirect
from flask import Blueprint

# Blueprint configuration
home_bp = Blueprint('home_bp', __name__)


#   ---------------------------------------------------------------
#   GET homepage
#   allowed roles: Executive Producer, Casting Director, Casting Assistant
#   forbidden roles: none
#   public access: allowed
#  ----------------------------------------------------------------
@home_bp.route('/')
#   does nothing, but is useful to check if the app is running
def index():
    return "hello"


#   ---------------------------------------------------------------
#   GET login
#   allowed roles: Executive Producer, Casting Director, Casting Assistant
#   forbidden roles: none
#   public access: allowed
#  ----------------------------------------------------------------
@home_bp.route('/login')
# redirects to auth0 login
def login():
    return redirect(f'{app.config["AUTH0_LOGIN_URL"]}')


#   ---------------------------------------------------------------
#   GET callback
#   allowed roles: Executive Producer, Casting Director, Casting Assistant
#   forbidden roles: none
#   public access: allowed
#  ----------------------------------------------------------------
@home_bp.route('/callback')
# auth0 calls this endpoint after login
def callback():
    return "callback"



