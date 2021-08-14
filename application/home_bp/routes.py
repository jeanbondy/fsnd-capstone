from flask import current_app as app, redirect, request
from flask import Blueprint

home_bp = Blueprint('home_bp', __name__)


@home_bp.route('/')
def index():
    return "hello"


@home_bp.route('/login')
def login():
    return redirect(f'{app.config["AUTH0_LOGIN_URL"]}')


@home_bp.route('/callback')
def callback():
    url = request.url
    url_root = request.url_root
    baseurl = request.base_url
    path = request.path
    full_path = request.full_path
    stri = str(request.url_rule)
    return f'url {url} url_root {url_root} baseurl {baseurl} path {path} full_path {full_path} stri {stri}'



