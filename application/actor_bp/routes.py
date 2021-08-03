from flask import Blueprint, render_template, request, redirect, url_for, flash
from application.models.actors import Actor
from application.models.movies import Movie
from application.templates.forms import *
from application import db
import sys

actor_bp = Blueprint('actor_bp', __name__)


#  Actors
#  ----------------------------------------------------------------
@actor_bp.route('/actors')
def actors():
    # TODO: replace with real data returned from querying the database
    data = Actor.query.all()
    return render_template('pages/actors.html', actors=data)


@actor_bp.route('/actors/search', methods=['POST'])
def search_actors():
    # TODO: implement search on actors with partial string search. Ensure it is case-insensitive.
    # search for "A" should return "Guns N Petals", "Matt Quevedo", and "The Wild Sax Band".
    # search for "band" should return "The Wild Sax Band".
    search_term = request.form.get('search_term', '').strip().lower()
    actors_query = Actor.query.filter(Actor.name.ilike('%' + search_term + '%')).all()
    actors_found = []

    for actor in actors_query:
        actor_data = actor.data()
        actor_upcoming_shows = Show.query.filter_by(actor_id=actor.id).filter(Show.start_time > datetime.now()).all()
        actor_data["num_upcoming_shows"] = len(actor_upcoming_shows)
        actors_found.append(actor_data)

    response = {
        "count": len(actors_found),
        "data": actors_found}
    return render_template('pages/search_actors.html', results=response,
                           search_term=request.form.get('search_term', ''))


@actor_bp.route('/actors/<int:actor_id>')
def show_actor(actor_id):
    # shows the actor page with the given actor_id
    # TODO: replace with real actor data from the actor table, using actor_id
    actor_query = Actor.query.get(actor_id)
    actor_data = actor_query.data()
    actor_shows = Show.query.filter_by(actor_id=actor_id).all()
    upcoming_shows = []
    past_shows = []
    for show in actor_shows:
        if show.start_time > datetime.now():
            upcoming_shows.append(show.data())
        else:
            past_shows.append(show.data())
    actor_data['past_shows'] = past_shows
    actor_data['upcoming_shows'] = upcoming_shows
    actor_data["past_shows_count"] = len(past_shows)
    actor_data["upcoming_shows_count"] = len(upcoming_shows)
    return render_template('pages/show_actor.html', actor=actor_data)


#  Create Actor
#  ----------------------------------------------------------------

@actor_bp.route('/actors/create', methods=['GET'])
def create_actor_form():
    form = ActorForm()
    return render_template('forms/new_actor.html', form=form)


@actor_bp.route('/actors/create', methods=['POST'])
def create_actor_submission():
    # called upon submitting the new actor listing form
    # TODO: insert form data as a new Venue record in the db, instead
    # TODO: modify data to be the data object returned from db insertion

    form = ActorForm(request.form)
    error = False
    try:
        # create new actor object and populate with form values
        new_actor = Actor()
        # populate with form values
        form.populate_obj(new_actor)
        # write to database
        db.session.add(new_actor)
        db.session.commit()
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        # TODO: on unsuccessful db insert, flash an error instead.
        # e.g., flash('An error occurred. Actor ' + data.name + ' could not be listed.')
        flash('An error occurred. Actor ' + request.form['name'] + ' could not be listed.')
    else:
        # on successful db insert, flash success
        flash('Actor ' + request.form['name'] + ' was successfully listed!')
    return render_template('pages/home.html')


#  Update
#  ----------------------------------------------------------------
@actor_bp.route('/actors/<int:actor_id>/edit', methods=['GET'])
def edit_actor(actor_id):
    # TODO: populate form with fields from actor with ID <actor_id>
    actor = Actor.query.get(actor_id)
    form = ActorForm(obj=actor)

    return render_template('forms/edit_actor.html', form=form, actor=actor)


@actor_bp.route('/actors/<int:actor_id>/edit', methods=['POST'])
def edit_actor_submission(actor_id):
    # TODO: take values from the form submitted, and update existing
    # actor record with ID <actor_id> using the new attributes
    form = ActorForm()
    # create the actor object from database
    actor = Actor.query.get(actor_id)
    # create error variable and set to false
    error = False

    try:
        # populate the actor object with form values
        actor.name = form.name.data.strip()
        actor.city = form.city.data.strip()
        actor.state = form.state.data
        actor.phone = form.phone.data.strip()
        actor.genres = form.genres.data
        actor.seeking_venue = form.seeking_venue.data
        actor.seeking_description = form.seeking_description.data.strip()
        actor.image_link = form.image_link.data
        actor.website = form.website_link.data
        actor.facebook_link = form.facebook_link.data
        # write to database
        db.session.add(actor)
        db.session.commit()
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        flash('An error occurred. Actor ' + request.form['name'] + ' could not be updated.')
    else:
        # on successful db insert, flash success
        flash('Actor ' + request.form['name'] + ' was successfully updated!')

    return redirect(url_for('actor_bp.show_actor', actor_id=actor_id))


@actor_bp.route('/actors/<actor_id>', methods=['DELETE'])
def delete_actor(actor_id):
    actor = Actor.query.get(actor_id)
    error = False
    try:
        db.session.delete(actor)
        db.session.commit()
    except:
        error = True
        db.session.rollback()
    finally:
        db.session.close()
        if error:
            flash('An error occurred. Actor ' + actor.name + ' could not be deleted.')
        else:
            flash('Successfully deleted Actor ' + actor.name + '.')
        # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
        # clicking that button delete it from the db then redirect the user to the homepage
        return redirect(url_for('index'))
