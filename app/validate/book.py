from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=10, message='查询关键字长度必须在1-30之间')])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
