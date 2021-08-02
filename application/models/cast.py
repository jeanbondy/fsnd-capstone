from application import db


class Cast(db.Model):
    __tablename__ = 'casts'
    id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('actor.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)

    def data(self):
        data = {
            "movie_id": self.cast_movie.id,
            "movie_name": self.cast_movie.name,
            "movie_image_link": self.cast_movie.image_link,
            "actor_id": self.actor_id,
            "actor_name": self.cast_actor.name,
            "actor_image_link": self.cast_actor.image_link
        }
        return data

    def __repr__(self):
        return '<Cast %r>' % self
