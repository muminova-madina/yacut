from random import choice
import string

from yacut.models import URLMap


def generate_short_id(length):
    symbols = string.ascii_letters + string.digits
    return "".join(choice(symbols) for _ in range(length))


def is_free_short_id(short_id):
    return URLMap.query.filter_by(short=short_id).first() is None


def get_unique_short_id(length):
    while True:
        short_id = generate_short_id(length)
        if is_free_short_id(short_id):
            break
    return short_id
