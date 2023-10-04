from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp
from yacut import constants as const


class URLMapForm(FlaskForm):
    """Форма для модели URLMap."""
    original_link = StringField(
        'Введите адрес URL',
        description="https://example.com",
        validators=[DataRequired(message='Обязательное поле')],
    )
    custom_id = StringField(
        'Идентификатор ссылки',
        description='Идентификатор ссылки',
        validators=(Length(max=16,
                           message='Длина поля не должна превышать 16 символов.'),
                    Regexp(const.CUSTOM_ID_REGEX,
                           message=(
                               'Идентификатор может состоять только'
                               'из латинских букв и цифр.'),
                           ),
                    ),
    )
    submit = SubmitField('Сократить')
