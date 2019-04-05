from wtforms import PasswordField, StringField, validators, SubmitField
from flask_wtf import FlaskForm


class SignupForm(FlaskForm):
    first_name = StringField('first_name', [validators.DataRequired()])
    last_name = StringField('last_name', [validators.DataRequired()])
    username = StringField('username', [validators.DataRequired()])
    password = PasswordField('password', [validators.DataRequired()])
    email = StringField('email', [validators.Email()])
    address = StringField('address', [validators.DataRequired()])
    signup_user = SubmitField('submit')

    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(SignupForm, self).__init__(*args, **kwargs)