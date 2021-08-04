from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, abort
from application.models.actors import Actor
from application.models.movies import Movie
from application import db
import sys

movie_bp = Blueprint('movie_bp', __name__)


#  All Movies
#  ----------------------------------------------------------------
@movie_bp.route('/movies', methods=['GET'])
def movies():
    # pagination
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    end = start + 10
    # query
    query = Movie.query.all()
    movies = [movie.format() for movie in query]
    # create response
    if len(movies[start:end]) == 0:
        return abort(404)
    else:
        return jsonify({
            'success': True,
            'totalMovies': len(query),
            'movies': movies[start:end]}), 200


#  Search Movie
#  ----------------------------------------------------------------
@movie_bp.route('/movies/search', methods=['POST'])
def search_movie():
    request_body = request.get_json()
    if not request_body:
        abort(400)
    if 'searchTerm' in request_body:
        search_term = (request_body['searchTerm'])
        query = Movie.query.filter(Movie.title.ilike('%' + search_term + '%')).all()
        movies = [movie.format() for movie in query]
        if len(query) == 0:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'totalMovies': len(query),
                'movies': movies
            }), 200
    else:
        abort(400)


#  Movie by ID
#  ----------------------------------------------------------------
@movie_bp.route('/movies/<int:movie_id>', methods=['GET'])
def movie_by_id(movie_id):
    movie = Movie.query.filter_by(id=movie_id).one_or_none()
    if movie is None:
        abort(404)
    else:
        return jsonify({
            'success': True,
            'movies': [movie.format()]}), 200


#  Create Movie
#  ----------------------------------------------------------------
@movie_bp.route('/movies', methods=['POST'])
def create_movie():
    request_body = request.get_json()
    if not request_body:
        abort(400)
    # check if all fields are included in the request
    if not {'title', 'release_date', 'image_link', 'imdb_link'}.issuperset(set(request_body)):
        abort(400)
    new_movie = Movie(title=request_body['title'],
                      release_date=request_body['release_date'],
                      image_link=request_body['image_link'],
                      imdb_link=request_body['imdb_link'])
    try:
        new_movie.insert()
        return jsonify({'success': True}), 200
    except:
        db.session.rollback()
        abort(422)
    finally:
        db.session.close()


#  Delete Movie
#  ----------------------------------------------------------------
@movie_bp.route('/movies/<movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
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


#  Update
#  ----------------------------------------------------------------
@movie_bp.route('/movies/<int:movie_id>/edit', methods=['PATCH'])
def edit_movie(movie_id):

    request_body = request.get_json()
    if not request_body:
        abort(400)
    edited_movie = Movie.query.filter_by(id=movie_id).one_or_none()
    if edited_movie is None:
        abort(404)

    # check if all fields are included in the request
    if not {'title', 'release_date', 'image_link', 'imdb_link'}.issuperset(set(request_body)):
        abort(400)
    edited_movie.title = request_body['title']
    edited_movie.release_date = request_body['release_date']
    edited_movie.image_link = request_body['image_link']
    edited_movie.imdb_link = request_body['imdb_link']
    try:
        edited_movie.update()
        return jsonify({'success': True,
                        'movies': [edited_movie.format()]}), 200
    except:
        db.session.rollback()
        abort(422)
    finally:
        db.session.close()
