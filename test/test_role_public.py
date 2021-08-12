import unittest
import json
from application import init_app, db
import config
import test.data
import test.populate_db
from application.models.actors import Actor
from application.models.movies import Movie




class CapstoneTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        config.ENV = "testing"
        self.app = init_app()
        self.client = self.app.test_client
        with self.app.app_context():
            db.drop_all()
            db.create_all()
            for actor in test.populate_db.sample_actors:
                Actor(**actor).insert()

            for movie in test.populate_db.sample_movies:
                Movie(**movie).insert()
        return self.app
        # binds the app to the current context


    def tearDown(self):
        """Executed after each test"""
        pass


# Test Public MOVIES

    def test_401_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_get_actors_pagination(self):
        res = self.client().get('/actors?page=99')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    def test_401_search_actors(self):
        res = self.client().post('/actors/search',
                                 json=test.data.json_search_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    def test_401_search_actors_notfound(self):
        res = self.client().post('/actors/search',
                                 json=test.data.json_search_actor_notfound)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_search_actors_malformed(self):
        res = self.client().post('/actors/search')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_actor_by_id(self):
        res = self.client().get('/actors/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    def test_401_actor_by_id_notfound(self):
        res = self.client().get('/actors/99')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_post_new_actors(self):
        res = self.client().post('/actors',
                                 json=test.data.json_new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    def test_401_post_new_actors_malformed(self):
        res = self.client().post('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_post_new_actors_incomplete(self):
        res = self.client().post('/actors',
                                 json=test.data.json_new_actor_incomplete)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_patch_actors(self):
        res = self.client().patch('/actors/3/edit',
                                  json=test.data.json_patch_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_patch_actors_notfound(self):
        res = self.client().patch('/actors/9/edit',
                                  json=test.data.json_patch_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_patch_actors_malformed(self):
        res = self.client().patch('/actors/3/edit')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_patch_actors_incomplete(self):
        res = self.client().patch('/actors/3/edit',
                                  json=test.data.json_patch_actor_incomplete)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_delete_actor_by_id(self):
        res = self.client().delete('/actors/4')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_delete_actor_by_id_notfound(self):
        res = self.client().delete('/actors/99')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

# Test Public MOVIES

    def test_401_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_get_movies_pagination(self):
        res = self.client().get('/movies?page=99')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_search_movies(self):
        res = self.client().post('/movies/search',
                                 json=test.data.json_search_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_search_movies_notfound(self):
        res = self.client().post('/movies/search',
                                 json=test.data.json_search_movie_notfound)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401search_movies_malformed(self):
        res = self.client().post('/movies/search')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_movie_by_id(self):
        res = self.client().get('/movies/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_movie_by_id_notfound(self):
        res = self.client().get('/movies/99')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_post_new_movie(self):
        res = self.client().post('/movies',
                                 json=test.data.json_new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_post_new_movie_malformed(self):
        res = self.client().post('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_post_new_movie_incomplete(self):
        res = self.client().post('/movies',
                                 json=test.data.json_new_movie_incomplete)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_patch_movies(self):
        res = self.client().patch('/movies/3/edit',
                                  json=test.data.json_patch_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_patch_movies_notfound(self):
        res = self.client().patch('/movies/99/edit',
                                  json=test.data.json_patch_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_patch_movies_malformed(self):
        res = self.client().patch('/movies/99/edit')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_patch_movies_incomplete(self):
        res = self.client().patch('/movies/03/edit',
                                  json=test.data.json_patch_movie_incomplete)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_delete_movie_by_id(self):
        res = self.client().delete('/movies/3')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_401_delete_movie_by_id_notfound(self):
        res = self.client().delete('/movies/99')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


if __name__ == '__main__':
    unittest.main()