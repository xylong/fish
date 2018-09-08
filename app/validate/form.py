from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.model.user import User


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='邮箱格式错误')])
    password = PasswordField(validators=[DataRequired(message='密码不能为空'), Length(6, 32)])


class RegisterForm(LoginForm):
    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='2-10个字符')])

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册')

    def validate_phone_number(self, field):
        if User.query.filter_by(phone_number=field.data).first():
            raise ValidationError('手机已注册')
