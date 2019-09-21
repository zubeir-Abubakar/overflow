from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class AddPostForm(FlaskForm):
    post = TextAreaField("Post", validators = [Required()])
    submit = SubmitField("Add Post")

class AddComment(FlaskForm):
    # name = StringField("Name", validators = [Required()])
    comment = TextAreaField("Comment", validators = [Required()])
    submit = SubmitField("Comment")

class EditBio(FlaskForm):
    bio = StringField("Bio")
    submit = SubmitField("Update")

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write something about yourself',validators=[Required()])
    submit = SubmitField('Submit')
