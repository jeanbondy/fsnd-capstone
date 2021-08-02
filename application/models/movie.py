from application import db, format_datetime
from flask import jsonify

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    release_date = db.Column(db.DateTime(timezone=False), nullable=False)
    image_link = db.Column(db.String(500))
    imdb_link = db.Column(db.String(120))
    actors = db.relationship('Cast', backref='cast_movie', lazy=True, cascade="all, delete-orphan")

    def data(self):
        data = {
            "id": self.id,
            "title": self.title,
            "release_date": format_datetime(str(self.start_time)),
            "imdb_link": self.imdb_link,
            "image_link": self.image_link
        }
        return data

    def __repr__(self):
        return '<Movie %r>' % self

