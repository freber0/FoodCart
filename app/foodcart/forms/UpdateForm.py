from wtforms import PasswordField, StringField, validators, SubmitField
from flask_wtf import FlaskForm


class UpdateForm(FlaskForm):
    first_name = StringField('first_name', [validators.DataRequired()])
    last_name = StringField('last_name', [validators.DataRequired()])

    password = PasswordField('password')
    email = StringField('email', [validators.Email()])
    address = StringField('address', [validators.DataRequired()])
    update_user = SubmitField('submit')

    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(UpdateForm, self).__init__(*args, **kwargs)