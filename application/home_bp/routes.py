from flask import current_app as app
from flask import Blueprint

home_bp = Blueprint('home_bp', __name__)


@home_bp.route('/')
def index():
    return "hello"


@home_bp.route('/login')
def login():
    return "login"


@home_bp.route('/callback')
def callback():
    return "callback"



