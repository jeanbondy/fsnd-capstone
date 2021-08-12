import unittest
import json
from application import init_app, db
import config
import test.data
import test.populate_db
from application.models.actors import Actor
from application.models.movies import Movie

header = test.data.header_cast_dir


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


# Test Casting Director ACTORS

    def test_get_actors(self):
        res = self.client().get('/actors',
                                headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['totalActors'])
        self.assertTrue(len(data['actors']))

    def test_404_get_actors_pagination(self):
        res = self.client().get('/actors?page=99',
                                headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_search_actors(self):
        res = self.client().post('/actors/search',
                                 json=test.data.json_search_actor,
                                 headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['totalActors'])
        self.assertTrue(len(data['actors']))

    def test_404_search_actors_notfound(self):
        res = self.client().post('/actors/search',
                                 json=test.data.json_search_actor_notfound,
                                 headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_400_search_actors_malformed(self):
        res = self.client().post('/actors/search',
                                 headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_actor_by_id(self):
        res = self.client().get('/actors/1',
                                headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['totalActors'])
        self.assertTrue(len(data['actors']))

    def test_404_actor_by_id_notfound(self):
        res = self.client().get('/actors/99',
                                headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_post_new_actors(self):
        res = self.client().post('/actors',
                                 json=test.data.json_new_actor,
                                 headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['totalActors'])
        self.assertTrue(len(data['actors']))

    def test_400_post_new_actors_malformed(self):
        res = self.client().post('/actors',
                                 headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_400_post_new_actors_incomplete(self):
        res = self.client().post('/actors',
                                 json=test.data.json_new_actor_incomplete,
                                 headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_patch_actors(self):
        res = self.client().patch('/actors/3/edit',
                                  json=test.data.json_patch_actor,
                                  headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['totalActors'])
        self.assertTrue(len(data['actors']))

    def test_404_patch_actors_notfound(self):
        res = self.client().patch('/actors/9/edit',
                                  json=test.data.json_patch_actor,
                                  headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_400_patch_actors_malformed(self):
        res = self.client().patch('/actors/3/edit',
                                  headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_400_patch_actors_incomplete(self):
        res = self.client().patch('/actors/3/edit',
                                  json=test.data.json_patch_actor_incomplete,
                                  headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_delete_actor_by_id(self):
        res = self.client().delete('/actors/4',
                                   headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_400_delete_actor_by_id_notfound(self):
        res = self.client().delete('/actors/99',
                                   headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

# Test Casting Director MOVIES

    def test_get_movies(self):
        res = self.client().get('/movies',
                                headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['totalMovies'])
        self.assertTrue(len(data['movies']))

    def test_404_get_movies_pagination(self):
        res = self.client().get('/movies?page=99',
                                headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_search_movies(self):
        res = self.client().post('/movies/search',
                                 json=test.data.json_search_movie,
                                 headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['totalMovies'])
        self.assertTrue(len(data['movies']))

    def test_404_search_movies_notfound(self):
        res = self.client().post('/movies/search',
                                 json=test.data.json_search_movie_notfound,
                                 headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_400_search_movies_malformed(self):
        res = self.client().post('/movies/search',
                                 headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_movie_by_id(self):
        res = self.client().get('/movies/1',
                                headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['totalMovies'])
        self.assertTrue(len(data['movies']))

    def test_404_movie_by_id_notfound(self):
        res = self.client().get('/movies/99',
                                headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_403_post_new_movie(self):
        res = self.client().post('/movies',
                                 json=test.data.json_new_movie,
                                 headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    def test_403_post_new_movie_malformed(self):
        res = self.client().post('/movies',
                                 headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    def test_403_post_new_movie_incomplete(self):
        res = self.client().post('/movies',
                                 json=test.data.json_new_movie_incomplete,
                                 headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    def test_patch_movies(self):
        res = self.client().patch('/movies/3/edit',
                                  json=test.data.json_patch_movie,
                                  headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_patch_movies_notfound(self):
        res = self.client().patch('/movies/99/edit',
                                  json=test.data.json_patch_movie,
                                  headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_400_patch_movies_malformed(self):
        res = self.client().patch('/movies/99/edit',
                                  headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_400_patch_movies_incomplete(self):
        res = self.client().patch('/movies/03/edit',
                                  json=test.data.json_patch_movie_incomplete,
                                  headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_403_delete_movie_by_id(self):
        res = self.client().delete('/movies/3',
                                   headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)

    def test_403_delete_movie_by_id_notfound(self):
        res = self.client().delete('/movies/99',
                                   headers=header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)


if __name__ == '__main__':
    unittest.main()