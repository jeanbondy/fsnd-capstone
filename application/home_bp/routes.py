from flask import current_app as app
from flask import Blueprint

home_bp = Blueprint('home_bp', __name__)


@home_bp.route('/')
def index():
    return "hello"



