from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField,PasswordField,ValidationError
from wtforms.validators import Required, EqualTo, Email
from flask_wtf.file import FileField, FileRequired
from ..models import User,Comment,Post

class RegistrationForm(FlaskForm):
    username = StringField("Userame", validators = [Required()])
    email = StringField("Email",validators = [Required(),Email()])
    password = PasswordField("Password", validators = [Required(),EqualTo("pass_confirm", message = "Passwords do not match")])
    pass_confirm = PasswordField("Confirm Password", validators = [Required()])
    submit = SubmitField("Register")

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError("Username is already taken")

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("Email is already taken")


class LoginForm(FlaskForm):
    email = StringField("Enter your email", validators = [Required()])
    password = PasswordField("Enter your password")
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")