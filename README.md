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

### GET /categories
General:
- Returns an object containing all categories, and the success value.
- Sample: `curl http://192.168.0.1:5000/categories`

```js
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "success": true
}
```

### GET /categories/{id}/questions
General:
- Returns a list with question objects of the given category id, the current category, number of questions and the success value.
- Sample: `curl http://192.168.0.1:5000/categories/3/questions`

```js
{
    "currentCategory": "Geography",
    "questions": [
        {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        }
    ],
    "success": true,
    "totalQuestions": 2
}
```

### GET /questions
General:
- Returns an object containing all categories, success value, current category, number of total questions, and a list of question objects.
- Supports pagination. A request without page parameter returns the first page.
- Sample: `curl http://192.168.0.1:5000/questions?page=2`

```js
{

    "success": true,
    "totalQuestions": 26,
     "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "questions": [
        {
            "answer": "One",
            "category": 2,
            "difficulty": 4,
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?"
        }
        ]
    
}
```

### POST /questions
Search:
- Returns a list of question objects, number of total questions and success value.
- Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d {"searchTerm": "hank"}`

```js
{
    "success": true,
    "questions": [
        {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        }
    ],
    "totalQuestions": 1
}
```

New Question:
- Creates a new question. Returns a success value.
- Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d {"question":  "What is the answer to everything", "answer":  "42", "difficulty": 1, "category": 1}`

```js
{
    "success": true
}

```

### DELETE /questions/{id}
General:
- Deletes  the question with the given ID, returns an object with "resource deleted" message and success value
- Sample: `curl http://127.0.0.1:5000/questions/9 -X DELETE`

```js
{
    "message": "resource deleted",
    "success": true
}
```

### POST /quizzes
General:
- Deletes  the question with the given ID, returns an object with "resource deleted" message and success value
- Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d {"previous_questions": [1,4,20,15], "quiz_category": {"id": 1, "type": "science"}}`
- - Request body: The request body consists of a list of ids of the previous questions, and an current category object.

```js
{
    "previous_questions": [1,4,20,15],
    "quiz_category": {
        "id": 1,
        "type": "science"
    }
}
```
The response is a success value and a single question object.
```js
{
    "question": {
        "answer": "Blood",
        "category": 1,
        "difficulty": 4,
        "id": 22,
        "question": "Hematology is a branch of medicine involving the study of what?"
    },
    "success": true
}

```
