import hashlib
import random
import string
from datetime import datetime
from yacut import constants as const
from yacut import db


class URLMap(db.Model):
    """Модель URL."""
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(
        db.String(const.CUSTOM_ID_LENGTH),
        nullable=False,
        unique=True,
        index=True,
    )
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def generate_short_id(length):
        symbols = string.ascii_letters + string.digits
        return "".join((random.choice(symbols) for _ in range(length)))

    @classmethod
    def is_free_short_id(cls, short_id):
        return cls.query.filter_by(short=short_id).first() is None

    @staticmethod
    def get_unique_short_id(length):
        max_attempts = 10

        for _ in range(max_attempts):
            random_string = ''.join(
                random.choice(string.ascii_letters + string.digits) for _ in range(length))

            short_id = hashlib.sha256(random_string.encode()).hexdigest()[:length]
            if URLMap.is_free_short_id(short_id):
                return short_id
        raise Exception("Невозможно сгенерировать уникальный короткий идентификатор")
