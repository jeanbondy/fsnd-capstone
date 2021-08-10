from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, abort
from application.models.actors import Actor
from application.models.movies import Movie
from application import db
from application.auth.auth import requires_auth
import sys
import logging

actor_bp = Blueprint('actor_bp', __name__)


#  All Actors
#  ----------------------------------------------------------------
@actor_bp.route('/actors', methods=['GET'])
@requires_auth('get:actors')
def actors(jwt):
    # pagination
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    end = start + 10
    # query
    query = Actor.query.all()
    actors = [actor.format() for actor in query]
    # create response
    if len(actors[start:end]) == 0:
        return abort(404)
    else:
        return jsonify({
            'success': True,
            'totalActors': len(query),
            'actors': actors[start:end]}), 200


#  Search Actor
#  ----------------------------------------------------------------
@actor_bp.route('/actors/search', methods=['POST'])
@requires_auth('get:actors')
def search_actor(jwt):
    request_body = request.get_json()
    if not request_body:
        abort(400)
    if 'searchTerm' in request_body:
        search_term = (request_body['searchTerm'])
        query = Actor.query.filter(Actor.name.ilike('%' + search_term + '%')).all()
        actors = [actor.format() for actor in query]
        if len(query) == 0:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'totalActors': len(query),
                'actors': actors
            }), 200
    else:
        abort(400)


#  Actor by ID
#  ----------------------------------------------------------------
@actor_bp.route('/actors/<int:actor_id>', methods=['GET'])
@requires_auth('get:actors')
def actor_by_id(jwt, actor_id):
    actor = Actor.query.filter_by(id=actor_id).one_or_none()
    if actor is None:
        abort(404)
    else:
        return jsonify({
            'success': True,
            'actors': [actor.format()]}), 200


#  Create Actor
#  ----------------------------------------------------------------
@actor_bp.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def create_actor(jwt):
    request_body = request.get_json()
    if not request_body:
        abort(400)
    # check if all fields are included in the request
    if not {'name', 'gender', 'age', 'phone', 'image_link', 'imdb_link'}.issuperset(set(request_body)):
        abort(400)
    new_actor = Actor(name=request_body['name'],
                      gender=request_body['gender'],
                      age=request_body['age'],
                      phone=request_body['phone'],
                      image_link=request_body['image_link'],
                      imdb_link=request_body['imdb_link'])
    try:
        new_actor.insert()
        return jsonify({'success': True}), 200
    except:
        db.session.rollback()
        abort(422)
    finally:
        db.session.close()


#  Delete Actor
#  ----------------------------------------------------------------
@actor_bp.route('/actors/<actor_id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actor(jwt, actor_id):
    actor = Actor.query.filter_by(id=actor_id).one_or_none()
    if actor is None:
        abort(404)
    else:
        try:
            actor.delete()
            return jsonify({'success': True}), 200
        except:
            db.session.rollback()
            abort(422)
        finally:
            db.session.close()


#  Update
#  ----------------------------------------------------------------
@actor_bp.route('/actors/<int:actor_id>/edit', methods=['PATCH'])
@requires_auth('patch:actors')
def edit_actor(jwt, actor_id):

    request_body = request.get_json()
    if not request_body:
        abort(400)
    actor = Actor.query.filter_by(id=actor_id).one_or_none()
    if actor is None:
        abort(404)

    # check if all fields are included in the request
    if not {'name', 'gender', 'age', 'phone', 'image_link', 'imdb_link'}.issuperset(set(request_body)):
        abort(400)
    actor.name = request_body['name']
    actor.gender = request_body['gender']
    actor.age = request_body['age']
    actor.phone = request_body['phone']
    actor.image_link = request_body['image_link']
    actor.imdb_link = request_body['imdb_link']
    try:
        actor.update()
        return jsonify({'success': True,
                        'actors': [actor.format()]}), 200
    except:
        db.session.rollback()
        abort(422)
    finally:
        db.session.close()
