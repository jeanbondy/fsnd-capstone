# FSND Final Project - Capstone

### Getting started

1. **Python 3.9** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

5. **Postgres** - Follow the instructions to install the latest version of Postgres for your platform on [postgresql.org](https://www.postgresql.org/download/)

### Database Setup
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

### Running the server

Ensure you are working using your created virtual environment.

#### Setting environment variables
The app defaults to user 'postgres', no password and the url localhost:5432.

You can set other values using these environment variables:
 - DATABASE_USER
 - DATABASE_PASSWORD
 - DATABASE_URL

From the backend folder in terminal run:
Windows:
```bash
set DATABASE_USER=youruser
set DATABASE_USER=yourpassword
set DATABASE_USER=yourdatabaseurl
```

Linux:
```bash
export DATABASE_USER=youruser
export DATABASE_USER=yourpassword
export DATABASE_USER=yourdatabaseurl
```

To run the server, execute in the same terminal:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Testing
To run the tests, make sure that the jwt for the all roles are valid, and run from the backend folder in terminal:

On windows
```bash
python test_flaskr.py
```

On Linux
```bash
python test_flaskr.py
```

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

### GET /actors
General:
- Returns an object containing all actors, the total number of actors, and the success value.
- Sample: `curl https://jb-capstone.herokuapp.com/actors`

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

### GET /actors/{id}
General:
- Returns a list with a single actor with the given id, the total number of actors, and the success value.
- Sample: `curl https://jb-capstone.herokuapp.com/actors/1`

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


### POST /actors/search
- Returns a list of actors, number of total actors and success value.
- Sample: `curl https://jb-capstone.herokuapp.com/actors/search -X POST -H "Content-Type: application/json" -d {"searchTerm": "roger"}`

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

### POST /actors
- Creates a new question. Returns a success value.
- Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d {"question":  "What is the answer to everything", "answer":  "42", "difficulty": 1, "category": 1}`

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

### PATCH /actors/{id}

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

### DELETE /actors/{id}
General:
- Deletes  the question with the given ID, returns an object with "resource deleted" message and success value
- Sample: `curl http://127.0.0.1:5000/questions/9 -X DELETE`

Sample response:

```js
{
    "success": true
}
```

