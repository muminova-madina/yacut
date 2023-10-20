import string
from random import choice

from flask import Response, redirect, render_template, url_for

from yacut import app
from yacut.constants import SHORT_ID_LENGTH
from yacut.form import URLMapForm
from yacut.models import URLMap
from yacut.utils import save


@app.route("/", methods=("GET", "POST"))
def index():
    form = URLMapForm()

    if form.validate_on_submit():
        custom_id = form.custom_id.data

        if not custom_id:
            custom_id = URLMap.get_unique_short_id(SHORT_ID_LENGTH)
        elif not URLMap.is_free_short_id(custom_id):
            error_message = 'Предложенный вариант короткой ссылки уже существует.'
            return render_template("index.html",
                                   form=form,
                                   error_message=error_message)

        urlmap = URLMap(
            original=form.original_link.data,
            short=custom_id,
        )
        save(urlmap)

        form.custom_id.data = None
        return render_template(
            "index.html",
            form=form,
            short_link=url_for(
                "mapping_redirect",
                short_id=urlmap.short,
                _external=True,
            ),
        )

    return render_template("index.html", form=form)


@app.route("/<string:short_id>", strict_slashes=False)
def mapping_redirect(short_id: str) -> Response:
    return redirect(
        URLMap.query.filter_by(short=short_id).first_or_404().original,
    )


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
