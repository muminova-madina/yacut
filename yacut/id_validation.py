import string
from random import random


def generate_short_id(length):
    symbols = string.ascii_letters + string.digits
    return "".join((random.choice(symbols) for _ in range(length)))


def is_free_short_id(cls, short_id):
    return cls.query.filter_by(short=short_id).first() is None


def get_unique_short_id(cls, length):
    while True:
        short_id = cls.generate_short_id(length)
        if cls.is_free_short_id(short_id):
            break
    return short_id
