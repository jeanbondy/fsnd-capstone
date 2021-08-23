from application import db, format_datetime
from datetime import datetime, date
from application.models.basemodel import BaseModel


class Actor(BaseModel):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String(120))
    age = db.Column(db.DateTime(timezone=False), nullable=False)
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    imdb_link = db.Column(db.String(120))

    def __init__(self, name, gender, age, phone, image_link, imdb_link):
        self.name = name,
        self.gender = gender,
        self.age = age,
        self.phone = phone,
        self.image_link = image_link,
        self.imdb_link = imdb_link

    def calculate_age(self):
        today = date.today()
        born = self.age
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "age": self.calculate_age(),
            "phone": self.phone,
            "imdb_link": self.imdb_link,
            "image_link": self.image_link
        }

    def __repr__(self):
        return '<Actor %r>' % self
