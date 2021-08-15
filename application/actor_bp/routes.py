# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#
from flask import Blueprint, request, jsonify, abort
from application.models.actors import Actor
from application import db
from application.auth.auth import requires_auth
from config import Config

# Blueprint configuration
actor_bp = Blueprint('actor_bp', __name__)

#   ---------------------------------------------------------------
#   GET list of all actors
#   allowed roles: Executive Producer, Casting Director, Casting Assistant
#   forbidden roles: none
#   public access: forbidden
#  ----------------------------------------------------------------
@actor_bp.route('/actors', methods=['GET'])
@requires_auth('get:actors')
def actors(jwt):
    # pagination
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * Config.PAGINATION
    end = start + Config.PAGINATION
    # query
    query = Actor.query.all()
    # create list with actor objects of all query results
    actors = [actor.format() for actor in query]
    # abort if there are no results
    if len(actors[start:end]) == 0:
        return abort(404)
    else:
        return jsonify({
            'success': True,
            'totalActors': len(query),
            'actors': actors[start:end]}), 200


#   ---------------------------------------------------------------
#   GET search actors
#   allowed roles: Executive Producer, Casting Director, Casting Assistant
#   forbidden roles: none
#   public access: forbidden
#  ----------------------------------------------------------------
@actor_bp.route('/actors/search', methods=['POST'])
@requires_auth('get:actors')
def search_actor(jwt):
    request_body = request.get_json()
    # check if request body is present, aborts if not
    if not request_body:
        abort(400)
    # check if 'searchTerm' is present, start search
    if 'searchTerm' in request_body:
        search_term = (request_body['searchTerm'])
        query = Actor.query.filter(Actor.name.ilike('%' + search_term + '%')).all()
        # create list with actor objects of all query results
        actors = [actor.format() for actor in query]
        # abort if no actor is found
        if len(query) == 0:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'totalActors': len(query),
                'actors': actors
            }), 200
    # abort if 'searchTerm' not present
    else:
        abort(400)


#   ---------------------------------------------------------------
#   GET actor by id
#   allowed roles: Executive Producer, Casting Director, Casting Assistant
#   forbidden roles: none
#   public access: forbidden
#  ----------------------------------------------------------------
@actor_bp.route('/actors/<int:actor_id>', methods=['GET'])
@requires_auth('get:actors')
def actor_by_id(jwt, actor_id):
    # Query by ID, returns actor object or none
    actor = Actor.query.filter_by(id=actor_id).one_or_none()
    if actor is None:
        abort(404)
    else:
        return jsonify({
            'success': True,
            'totalActors': len([actor]),
            'actors': [actor.format()]}), 200


#   ---------------------------------------------------------------
#   POST actor
#   allowed roles: Executive Producer, Casting Director
#   forbidden roles: Casting Assistant
#   public access: forbidden
#  ----------------------------------------------------------------
@actor_bp.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def create_actor(jwt):
    request_body = request.get_json()
    # check if request body is present, aborts if not
    if not request_body:
        abort(400)
    # check if all required fields are included, abort if not
    if not {'name', 'gender', 'age', 'phone', 'image_link', 'imdb_link'}.issubset(set(request_body)):
        abort(400)
    # create an actor object with the parameters from request body
    # Actor(**request_body) ** shorthand works when json fields are named like the model's parameters
    new_actor = Actor(**request_body)
    try:
        new_actor.insert()
        return jsonify({'success': True,
                        'totalActors': len([new_actor]),
                        'actors': [new_actor.format()]
                        }), 201
    except:
        db.session.rollback()
        abort(422)
    finally:
        db.session.close()


#   ---------------------------------------------------------------
#   DELETE actor
#   allowed roles: Executive Producer, Casting Director
#   forbidden roles: Casting Assistant
#   public access: forbidden
#  ----------------------------------------------------------------
@actor_bp.route('/actors/<actor_id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actor(jwt, actor_id):
    # Query by ID, returns actor object or none
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


#   ---------------------------------------------------------------
#   PATCH actor
#   allowed roles: Executive Producer, Casting Director
#   forbidden roles: Casting Assistant
#   public access: forbidden
#  ----------------------------------------------------------------
@actor_bp.route('/actors/<int:actor_id>/edit', methods=['PATCH'])
@requires_auth('patch:actors')
def edit_actor(jwt, actor_id):
    # check if request body is present, abort if not
    request_body = request.get_json()
    if not request_body:
        abort(400)
    # Query by ID, returns actor object or none
    actor = Actor.query.filter_by(id=actor_id).one_or_none()
    if actor is None:
        abort(404)
    # check if all required fields are included in the request
    if not {'name', 'gender', 'age', 'phone', 'image_link', 'imdb_link'}.issubset(set(request_body)):
        abort(400)
    # replace object's values with values from request
    actor.name = request_body['name']
    actor.gender = request_body['gender']
    actor.age = request_body['age']
    actor.phone = request_body['phone']
    actor.image_link = request_body['image_link']
    actor.imdb_link = request_body['imdb_link']
    try:
        actor.update()
        return jsonify({'success': True,
                        'totalActors': len([actor]),
                        'actors': [actor.format()]}), 201
    except:
        db.session.rollback()
        abort(422)
    finally:
        db.session.close()
