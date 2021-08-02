from application import db
from flask import jsonify


class Artist(db.Model):
    __tablename__ = 'actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String(120))
    age = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    imdb_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    movies = db.relationship('Show', backref='guest_actor', lazy=True, cascade="all, delete-orphan")

    def data(self):
        data = {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "age": self.age,
            "phone": self.phone,
            "website": self.website,
            "imdb_link": self.imdb_link,
            "image_link": self.image_link
        }
        return data

    def __repr__(self):
        return '<Actor %r>' % self

