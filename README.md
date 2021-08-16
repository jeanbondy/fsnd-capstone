# FSND Final Project - Capstone

## Getting started
These are the requirements to run the app or the unittests locally.

### Prerequisites
1. **Python 3.8 or higher** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Postgres** - Follow the instructions to install the latest version of Postgres for your platform on [postgresql.org](https://www.postgresql.org/download/)

### Get it running

1. **Clone** the repository and open a terminal in the project's directory, likely `fsnd-capstone`.

2. **Virtual Enviornment** - I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `fsnd-capstone` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages.

4. **Database Setup**
With Postgres running, we'll start with a clean slate so that the results are not influenced by previous data. We delete existing databases, and create new databases.

We assume the user to be the default user "postgres". If you want to use a different user, adapt the follwing commands accordingly.

From the backend folder in terminal run:

On Linux:
```bash
sudo su postgres
dropdb --if-exists capstone
dropdb --if-exists capstone_test
createdb capstone
createdb capstone_test
```

On Windows:
```bash
dropdb -U postgres --if-exists capstone
dropdb -U postgres --if-exists capstone_test
createdb -U postgres capstone
createdb -U postgres capstone_test

```

5. **Setting environment variables**
For your convenience, the repo includes a `setup.sh` that will set all required environment variables for you.

| environment variable | value |  what is this |
| ------ | ------ | ------ |
| DATABASE_URL | --- | Production db, e.g. running on Heroku |
| DEV_DATABASE_URI | postgresql://postgres@localhost:5432/capstone | local db for development |
| TEST_DATABASE_URI | postgresql://postgres@localhost:5432/capstone_test | local db for testing |
| ENV | development | Setting app either to testing, development or production |
| AUTH0_DOMAIN | --- | Application domain as defined on auth0.com |
| AUTH0_CLIENT_ID | --- | Client ID as defined on auth0.com |
| AUTH0_CLIENT_SECRET | --- | Client as defined on auth0.com |
| API_AUDIENCE | --- | API audience as defined on auth0.com |
| AUTH0_CALLBACK_URL | https://jb-capstone.herokuapp.com/callback | calback URL configured on auth0|
| JWT_EXEC_PROD | --- | jwt for Executive Producer role |
| JWT_CAST_ASSIST | --- | jwt for Casting Assistant role |
| JWT_CAST_DIR | --- | jwt for Casting Director role |


### Testing
Now it's time to run the unittests to make sure everything works as expected.  

The unittests require the postgres database to be running and defined in the environment variable TEST_DATABASE_URI. If you ran the `setup.sh`, this has been taken care of. The tests deletes the tables, creates new tables and populates them with sample data for each role.  
The unittests call each endpoint for the roles public, executive producer, casting director and casting assistant.  
To run the tests, make sure that the jwt for the all roles are valid, and run from the backend folder in terminal:

On windows
```bash
python -m unittest discover test
```

On Linux
```bash
python -m unittest discover test
```

### Running the app locally

## Error Handling

Errors are returned as JSON objects:

```js
{
    "success": False, 
    "error": 404,
    "message": "resource not found"
}

```
These are the error types the API will return when requests fail:
- 400: Bad request
- 401: Authorization header missing, or malformed, or toke expired
- 403: Not permittet
- 404: Resource not found
- 405: Method not allowed
- 422: Unprocessable
- 500: Server error




## Endpoints

### General Endpoints
These are a set of general endpoints not used for the API.

#### GET /
Returns "hello", a simple check to see if the app is running.

#### GET /login
Redirects to the auth0.com login page

#### GET /callback
Called by auth0.com after succesful login

### Actors Endpoints
Endpoints to get, post, update and delete actors

#### GET /actors
Returns an object containing all actors, the total number of actors, and the success value.  
Requires permission: `get:actors`

| Role | Permission |
| ------ | ------ |
| Executive Producer | yes |
| Casting Director | yes |
| Casting Assistant | yes |
| Public | no |

Sample response:
```js
{
    "actors": [
        {
            "age": 93,
            "gender": "m",
            "id": 1,
            "image_link": "https://en.wikipedia.org/wiki/File:Roger_Moore_12_Allan_Warren.jpg",
            "imdb_link": "https://www.imdb.com/name/nm0000549/",
            "name": "Roger Moore",
            "phone": "+44 12345678"
        },
        ...
      ],
    "success": true,
    "totalActors": 4
}
```

#### GET /actors/{id}
Returns a list with a single actor with the given id, the total number of actors, and the success value.  
Requires permission: `get:actors`

| Role | Permission |
| ------ | ------ |
| Executive Producer | yes |
| Casting Director | yes |
| Casting Assistant | yes |
| Public | no |

```js
{
    "actors": [
        {
            "age": 93,
            "gender": "m",
            "id": 1,
            "image_link": "https://en.wikipedia.org/wiki/File:Roger_Moore_12_Allan_Warren.jpg",
            "imdb_link": "https://www.imdb.com/name/nm0000549/",
            "name": "Roger Moore",
            "phone": "+44 12345678"
        }
    ],
    "success": true,
    "totalActors": 1
}
```


#### POST /actors/search
Returns a list of actors, number of total actors and success value.  
Requires permission: `get:actors`

| Role | Permission |
| ------ | ------ |
| Executive Producer | yes |
| Casting Director | yes |
| Casting Assistant | yes |
| Public | no |

Request body:
```js
{
    "searchTerm": "roger"
}
```

Sample response:
```js
{
    "actors": [
        {
            "age": 93,
            "gender": "m",
            "id": 1,
            "image_link": "https://en.wikipedia.org/wiki/File:Roger_Moore_12_Allan_Warren.jpg",
            "imdb_link": "https://www.imdb.com/name/nm0000549/",
            "name": "Roger Moore",
            "phone": "+44 12345678"
        }
    ],
    "success": true,
    "totalActors": 1
}
```

#### POST /actors
Creates an actor. Returns a list of actors, number of total actors and success value.  
Requires permission: `post:actors`

| Role | Permission |
| ------ | ------ |
| Executive Producer | yes |
| Casting Director | yes |
| Casting Assistant | no |
| Public | no |

Request body:
```js
{
    "name":  "George Lazenby",
    "age":  "1939-09-05 00:00:00",
    "gender": "m",
    "phone": "+61 123 456789",
    "imdb_link": "https://www.imdb.com/title/tt0064757/",
    "image_link": "https://en.wikipedia.org/wiki/File:GeorgeLazenby11.14.08ByLuigiNovi.jpg"
}
```

Sample response:

```js
{
    "actors": [
        {
            "age": 81,
            "gender": "m",
            "id": 9,
            "image_link": "https://en.wikipedia.org/wiki/File:GeorgeLazenby11.14.08ByLuigiNovi.jpg",
            "imdb_link": "https://www.imdb.com/title/tt0064757/",
            "name": "George Lazenby",
            "phone": "+61 123 456789"
        }
    ],
    "success": true,
    "totalActors": 1
}
```

#### PATCH /actors/{id}
Updates an existing actor with the given id. Returns a list of actors, number of total actors and success value.  
Requires permission: `patch:actors`

| Role | Permission |
| ------ | ------ |
| Executive Producer | yes |
| Casting Director | yes |
| Casting Assistant | no |
| Public | no |

Sample request body:

```js
{
    "name":  "George Lazenby",
    "age":  "1939-09-05 00:00:00",
    "gender": "m",
    "phone": "+61 123 456789",
    "imdb_link": "https://www.imdb.com/title/tt0064757/",
    "image_link": "https://en.wikipedia.org/wiki/File:GeorgeLazenby11.14.08ByLuigiNovi.jpg"
}
```
Sample response:

```js
{
    "actors": [
        {
            "age": 81,
            "gender": "m",
            "id": 1,
            "image_link": "https://en.wikipedia.org/wiki/File:GeorgeLazenby11.14.08ByLuigiNovi.jpg",
            "imdb_link": "https://www.imdb.com/title/tt0064757/",
            "name": "George Lazenby",
            "phone": "+61 123 456789"
        }
    ],
    "success": true,
    "totalActors": 1
}
```

#### DELETE /actors/{id}
Deletes an existing actor with the given id. Returns a success value.  
Requires permission: `delete:actors`

| Role | Permission |
| ------ | ------ |
| Executive Producer | yes |
| Casting Director | yes |
| Casting Assistant | no |
| Public | no |

Sample response:

```js
{
    "success": true
}
```

### Movies endpoints
Endpoints to get, post, update and delete movies


#### GET /movies
Returns an object containing all movies, the total number of movies, and the success value.  
Requires permission: `get:movies`

| Role | Permission |
| ------ | ------ |
| Executive Producer | yes |
| Casting Director | yes |
| Casting Assistant | yes |
| Public | no |

Sample response:
```js
{
    "actors": [
        {
            "age": 93,
            "gender": "m",
            "id": 1,
            "image_link": "https://en.wikipedia.org/wiki/File:Roger_Moore_12_Allan_Warren.jpg",
            "imdb_link": "https://www.imdb.com/name/nm0000549/",
            "name": "Roger Moore",
            "phone": "+44 12345678"
        },
        ...
      ],
    "success": true,
    "totalActors": 4
}
```

#### GET /movies/{id}
Returns a list with a single movie with the given id, the number of returned movies, and the success value.  
Requires permission: `get:movies`

| Role | Permission |
| ------ | ------ |
| Executive Producer | yes |
| Casting Director | yes |
| Casting Assistant | yes |
| Public | no |

```js
{
    "actors": [
        {
            "age": 93,
            "gender": "m",
            "id": 1,
            "image_link": "https://en.wikipedia.org/wiki/File:Roger_Moore_12_Allan_Warren.jpg",
            "imdb_link": "https://www.imdb.com/name/nm0000549/",
            "name": "Roger Moore",
            "phone": "+44 12345678"
        }
    ],
    "success": true,
    "totalActors": 1
}
```


#### POST /movies/search
Returns a list of movies, number of returned movies and success value.  
Requires permission: `get:movies`

| Role | Permission |
| ------ | ------ |
| Executive Producer | yes |
| Casting Director | yes |
| Casting Assistant | yes |
| Public | no |

Request body:
```js
{
    "searchTerm": "roger"
}
```

Sample response:
```js
{
    "actors": [
        {
            "age": 93,
            "gender": "m",
            "id": 1,
            "image_link": "https://en.wikipedia.org/wiki/File:Roger_Moore_12_Allan_Warren.jpg",
            "imdb_link": "https://www.imdb.com/name/nm0000549/",
            "name": "Roger Moore",
            "phone": "+44 12345678"
        }
    ],
    "success": true,
    "totalActors": 1
}
```

#### POST /movies
Creates a movie. Returns a list of movies, number of returned movies and success value.  
Requires permission: `post:movies`

| Role | Permission |
| ------ | ------ |
| Executive Producer | yes |
| Casting Director | no |
| Casting Assistant | no |
| Public | no |

Request body:
```js
{
    "name":  "George Lazenby",
    "age":  "1939-09-05 00:00:00",
    "gender": "m",
    "phone": "+61 123 456789",
    "imdb_link": "https://www.imdb.com/title/tt0064757/",
    "image_link": "https://en.wikipedia.org/wiki/File:GeorgeLazenby11.14.08ByLuigiNovi.jpg"
}
```

Sample response:

```js
{
    "actors": [
        {
            "age": 81,
            "gender": "m",
            "id": 9,
            "image_link": "https://en.wikipedia.org/wiki/File:GeorgeLazenby11.14.08ByLuigiNovi.jpg",
            "imdb_link": "https://www.imdb.com/title/tt0064757/",
            "name": "George Lazenby",
            "phone": "+61 123 456789"
        }
    ],
    "success": true,
    "totalActors": 1
}
```

#### PATCH /movies/{id}
Updates an existing movie with the given id. Returns a list of pathched movies, number of returned movies and success value.  
Requires permission: `patch:movies`

| Role | Permission |
| ------ | ------ |
| Executive Producer | yes |
| Casting Director | yes |
| Casting Assistant | no |
| Public | no |

Sample request body:

```js
{
    "name":  "George Lazenby",
    "age":  "1939-09-05 00:00:00",
    "gender": "m",
    "phone": "+61 123 456789",
    "imdb_link": "https://www.imdb.com/title/tt0064757/",
    "image_link": "https://en.wikipedia.org/wiki/File:GeorgeLazenby11.14.08ByLuigiNovi.jpg"
}
```
Sample response:

```js
{
    "actors": [
        {
            "age": 81,
            "gender": "m",
            "id": 1,
            "image_link": "https://en.wikipedia.org/wiki/File:GeorgeLazenby11.14.08ByLuigiNovi.jpg",
            "imdb_link": "https://www.imdb.com/title/tt0064757/",
            "name": "George Lazenby",
            "phone": "+61 123 456789"
        }
    ],
    "success": true,
    "totalActors": 1
}
```

#### DELETE /movies/{id}
Deletes an existing movie with the given id. Returns a success value.  
Requires permission: `delete:movies`

| Role | Permission |
| ------ | ------ |
| Executive Producer | yes |
| Casting Director | no |
| Casting Assistant | no |
| Public | no |

Sample response:

```js
{
    "success": true
}
```
