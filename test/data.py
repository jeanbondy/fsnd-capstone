import config

header_exec_prod = [('Content-Type', 'application/json'),
                   ('Authorization', f'Bearer {config.Config.JWT_EXEC_PROD}')
                   ]

header_cast_dir = [('Content-Type', 'application/json'),
                   ('Authorization', f'Bearer {config.Config.JWT_CAST_DIR}')
                   ]

header_cast_assist = [('Content-Type', 'application/json'),
                      ('Authorization', f'Bearer {config.Config.JWT_CAST_ASSIST}')
                      ]

json_search_actor = {'searchTerm': "roger"}

json_search_actor_notfound = {'searchTerm': "starfish"}

json_new_actor = {
    "name":  "George Lazenby",
    "age":  "1939-09-05 00:00:00",
    "gender": "m",
    "phone": "+61 123 456789",
    "imdb_link": "https://www.imdb.com/title/tt0064757/",
    "image_link": "https://en.wikipedia.org/wiki/File:GeorgeLazenby11.14.08ByLuigiNovi.jpg"
}

json_new_actor_incomplete = {
    "age":  "1939-09-05 00:00:00",
    "gender": "m"
}

json_patch_actor = {
    "name":  "Updated Name",
    "age":  "1999-12-31 00:00:00",
    "gender": "m",
    "phone": "+61 123 456789",
    "imdb_link": "https://www.imdb.com/title/tt0064757/",
    "image_link": "https://en.wikipedia.org/wiki/File:GeorgeLazenby11.14.08ByLuigiNovi.jpg"
}

json_patch_actor_incomplete = {
    "name":  "Updated Name"
}

json_new_movie = {
    "image_link": "https://upload.wikimedia.org/wikipedia/en/a/ad/From_Russia_with_Love_%E2%80%93_UK_cinema_poster.jpg",
    "imdb_link": "https://www.imdb.com/title/tt0057076/",
    "release_date": "1963-10-10 00:00:00",
    "title": "From Russia with Love"
}

json_new_movie_incomplete = {
    "title": "From Russia with Love"
}

json_search_movie = {'searchTerm': "live"}

json_search_movie_notfound = {'searchTerm': "rainbow"}

json_patch_movie = {
    "image_link": "https://upload.wikimedia.org/wikipedia/en/a/ad/From_Russia_with_Love_%E2%80%93_UK_cinema_poster.jpg",
    "imdb_link": "https://www.imdb.com/title/tt0057076/",
    "release_date": "1963-10-10 00:00:00",
    "title": "From Russia with Love"
}

json_patch_movie_incomplete = {
    "image_link": "https://upload.wikimedia.org/wikipedia/en/a/ad/From_Russia_with_Love_%E2%80%93_UK_cinema_poster.jpg",
    "imdb_link": "https://www.imdb.com/title/tt0057076/",
    "release_date": "1963-10-10 00:00:00"
}