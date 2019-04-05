from wtforms import PasswordField, StringField, validators, SubmitField
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = StringField('username', [validators.DataRequired()])
    password = PasswordField('password', [validators.DataRequired()])
    login_user = SubmitField('submit')

    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(LoginForm, self).__init__(*args, **kwargs)


