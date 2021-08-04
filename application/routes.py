from flask import current_app as app
from flask import jsonify

# ----------------------------------------------------------------------------#
# Controllers.
# ----------------------------------------------------------------------------#


@app.route('/')
def index():
    return "hello"


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
