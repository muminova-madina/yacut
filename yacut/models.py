from datetime import datetime

from yacut import db
from yacut import constants as const
from yacut.id_validation import generate_short_id, is_free_short_id, get_unique_short_id


class URLMap(db.Model):
    """Модель URL."""
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String(const.CUSTOM_ID_LENGTH), nullable=False, unique=True, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def generate_short_id(length):
        return generate_short_id(length)

    @staticmethod
    def is_free_short_id(short_id):
        return is_free_short_id(short_id)

    @staticmethod
    def get_unique_short_id(length):
        return get_unique_short_id(length)
