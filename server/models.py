from app import db
import os


class ShortUrl(db.Model):
    __tablename__ = 'short_url'

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String)
    short_url = db.Column(db.String)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def serialize(self):
        return {
            'original_url': self.original_url,
            'short_url': self.short_url,
        }

    def __repr__(self):
        return '<id {}>'.format(self.id)

