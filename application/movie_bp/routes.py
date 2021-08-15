# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#
from flask import Blueprint, request, jsonify, abort
from application.models.movies import Movie
from application import db
from application.auth.auth import requires_auth

# Blueprint configuration
movie_bp = Blueprint('movie_bp', __name__)


#   ---------------------------------------------------------------
#   GET list of all movies
#   allowed roles: Executive Producer, Casting Director, Casting Assistant
#   forbidden roles: none
#   public access: forbidden
#  ----------------------------------------------------------------
@movie_bp.route('/movies', methods=['GET'])
@requires_auth('get:movies')
def movies(jwt):
    # pagination
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    end = start + 10
    # query
    query = Movie.query.all()
    # create list with movie objects of all query results
    movies = [movie.format() for movie in query]
    # abort if there are no results
    if len(movies[start:end]) == 0:
        return abort(404)
    else:
        return jsonify({
            'success': True,
            'totalMovies': len(query),
            'movies': movies[start:end]}), 200


#   ---------------------------------------------------------------
#   GET search movies
#   allowed roles: Executive Producer, Casting Director, Casting Assistant
#   forbidden roles: none
#   public access: forbidden
#  ----------------------------------------------------------------
@movie_bp.route('/movies/search', methods=['POST'])
@requires_auth('get:movies')
def search_movie(jwt):
    request_body = request.get_json()
    # check if request body is present, aborts if not
    if not request_body:
        abort(400)
    # check if 'searchTerm' is present, start search
    if 'searchTerm' in request_body:
        search_term = (request_body['searchTerm'])
        query = Movie.query.filter(Movie.title.ilike('%' + search_term + '%')).all()
        # create list with movie objects of all query results
        movies = [movie.format() for movie in query]
        # abort if no movie is found
        if len(query) == 0:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'totalMovies': len(query),
                'movies': movies
            }), 200
    # abort if 'searchTerm' not present
    else:
        abort(400)


#   ---------------------------------------------------------------
#   GET movie by id
#   allowed roles: Executive Producer, Casting Director, Casting Assistant
#   forbidden roles: none
#   public access: forbidden
#  ----------------------------------------------------------------
@movie_bp.route('/movies/<int:movie_id>', methods=['GET'])
@requires_auth('get:movies')
def movie_by_id(jwt, movie_id):
    # Query by ID, returns movie object or none
    movie = Movie.query.filter_by(id=movie_id).one_or_none()
    if movie is None:
        abort(404)
    else:
        return jsonify({
            'success': True,
            'totalMovies': len([movie]),
            'movies': [movie.format()]}), 200


#   ---------------------------------------------------------------
#   POST movie
#   allowed roles: Executive Producer
#   forbidden roles: Casting Assistant, Casting Director
#   public access: forbidden
#  ----------------------------------------------------------------
@movie_bp.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def create_movie(jwt):
    request_body = request.get_json()
    # check if request body is present, aborts if not
    if not request_body:
        abort(400)
    # check if all required fields are included, abort if not
    if not {'title', 'release_date', 'image_link', 'imdb_link'}.issubset(set(request_body)):
        abort(400)
    new_movie = Movie(title=request_body['title'],
                      release_date=request_body['release_date'],
                      image_link=request_body['image_link'],
                      imdb_link=request_body['imdb_link'])
    try:
        new_movie.insert()
        return jsonify({
            'success': True,
            'totalMovies': len([new_movie]),
            'movies': [new_movie.format()]}), 201

    except:
        db.session.rollback()
        abort(422)
    finally:
        db.session.close()


#   ---------------------------------------------------------------
#   DELETE movie
#   allowed roles: Executive Producer
#   forbidden roles: Casting Assistant, Casting Director
#   public access: forbidden
#  ----------------------------------------------------------------
@movie_bp.route('/movies/<movie_id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movie(jwt, movie_id):
    # Query by ID, returns movie object or none
    movie = Movie.query.filter_by(id=movie_id).one_or_none()
    if movie is None:
        abort(404)
    else:
        try:
            movie.delete()
            return jsonify({'success': True}), 200
        except:
            db.session.rollback()
            abort(422)
        finally:
            db.session.close()


#   ---------------------------------------------------------------
#   PATCH movie
#   allowed roles: Executive Producer, Casting Director
#   forbidden roles: Casting Assistant
#   public access: forbidden
#  ----------------------------------------------------------------
@movie_bp.route('/movies/<int:movie_id>/edit', methods=['PATCH'])
@requires_auth('patch:movies')
def edit_movie(jwt, movie_id):
    # check if request body is present, abort if not
    request_body = request.get_json()
    if not request_body:
        abort(400)
    # Query by ID, returns movie object or none
    edited_movie = Movie.query.filter_by(id=movie_id).one_or_none()
    if edited_movie is None:
        abort(404)
    # check if all required fields are included in the request
    if not {'title', 'release_date', 'image_link', 'imdb_link'}.issubset(set(request_body)):
        abort(400)
    # replace object's values with values from request
    edited_movie.title = request_body['title']
    edited_movie.release_date = request_body['release_date']
    edited_movie.image_link = request_body['image_link']
    edited_movie.imdb_link = request_body['imdb_link']
    try:
        edited_movie.update()
        return jsonify({'success': True,
                        'totalMovies': len([edited_movie]),
                        'movies': [edited_movie.format()]}), 200
    except:
        db.session.rollback()
        abort(422)
    finally:
        db.session.close()
