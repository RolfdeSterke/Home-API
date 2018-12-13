from db import db
from datetime import datetime


class TodoModel(db.Model):
    __tablename__ = '_todo'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255), nullable=False)
    uri = db.Column(db.String(255), nullable=False)
    image_uri = db.Column(db.String(255), nullable=True)
    is_done = db.Column(db.Boolean(), nullable=False)
    is_hidden = db.Column(db.Boolean(), nullable=False)
    creation_timestamp = db.Column(db.Integer, nullable=False)

    def __init__(self, comment, uri, image_uri, is_done, is_hidden):
        self.comment = comment
        self.uri = uri
        self.image_uri = image_uri
        self.is_done = is_done
        self.is_hidden = is_hidden
        self.creation_timestamp = datetime.now().timestamp()

    def to_json(self):
        return {
            'id': self.id,
            'comment': self.comment,
            'uri': self.uri,
            'image_uri': self.image_uri,
            'is_done': self.is_done,
            'is_hidden': self.is_hidden,
            'creation_timestamp': self.creation_timestamp
        }

    def update(self, comment, uri, image_uri, is_done, is_hidden):
        self.comment = comment
        self.uri = uri
        self.image_uri = image_uri
        self.is_done = is_done
        self.is_hidden = is_hidden
        db.session.commit()

    @classmethod
    def find_all(cls):
        todo = cls.query.all()
        return todo

    @classmethod
    def find_all_non_hidden(cls):
        todo = cls.query.filter_by(is_hidden=0).all()
        return todo

    @classmethod
    def find_by_id(cls, todo_id):
        todo = cls.query.filter_by(id=todo_id).first()
        return todo

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Todo Id:{}>".format(self.id)
