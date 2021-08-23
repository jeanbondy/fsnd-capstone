# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#
from application import db


'''
Extend the base Model class to add common methods
'''


class BaseModel(db.Model):
    __abstract__ = True

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()