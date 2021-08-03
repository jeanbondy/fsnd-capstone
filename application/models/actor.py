from application import db, format_datetime
from flask import jsonify
import datetime


class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String(120))
    age = db.Column(db.DateTime(timezone=False), nullable=False)
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    imdb_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    appearance = db.relationship('Cast', backref='cast_actor', lazy=True, cascade="all, delete-orphan")

    def data(self):
        data = {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "age": format_datetime(str(self.start_time)),
            "phone": self.phone,
            "website": self.website,
            "imdb_link": self.imdb_link,
            "image_link": self.image_link
        }
        return data

    def __repr__(self):
        return '<Actor %r>' % self

