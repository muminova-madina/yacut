from datetime import datetime

from yacut import db
from yacut import constants as const


class URLMap(db.Model):
    """Модель URL."""
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String(const.CUSTOM_ID_LENGTH), nullable=False, unique=True, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
