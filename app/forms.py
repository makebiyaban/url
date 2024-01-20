from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime


class LoginForm(FlaskForm):
    username = StringField('Username or Email or Phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')

class SignUpForm(FlaskForm):
    name = StringField('enter your name', validators=[DataRequired()])
    lastname = StringField('enter your family name', validators=[DataRequired()])
    email = StringField('enter your Email address', validators=[DataRequired()])
    phone = StringField('enter your mobile phone number')
    username = StringField('if you want choose usaername or ...', validators=[DataRequired()])
    password = PasswordField('enter password', validators=[DataRequired()])
    ##datetime = datetime()
    submit = SubmitField('Sign Up')
class LinkForm(FlaskForm):
    link = StringField('link ra vared konid', validators=[DataRequired()])
    submit = SubmitField('link ra kotah kon')