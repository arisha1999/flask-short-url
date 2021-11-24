from app import db
from hashids import Hashids


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

    def generate_short_url(self, salt):
        hashids = Hashids(min_length=4, salt=salt)
        short_url = hashids.encode(self.id)
        return short_url

