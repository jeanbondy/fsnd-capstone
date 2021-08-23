# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#
from application import db, format_datetime
from application.models.basemodel import BaseModel

class Movie(BaseModel):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    release_date = db.Column(db.DateTime(timezone=False), nullable=False)
    image_link = db.Column(db.String(500))
    imdb_link = db.Column(db.String(120))

    def __init__(self, title, release_date, imdb_link, image_link):
        self.title = title,
        self.release_date = release_date,
        self.imdb_link = imdb_link,
        self.image_link = image_link

    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": format_datetime(str(self.release_date)),
            "imdb_link": self.imdb_link,
            "image_link": self.image_link
        }

    def __repr__(self):
        return '<Movie %r>' % self

