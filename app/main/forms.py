from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,RadioField,SelectField
from wtforms.validators import InputRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Whats about yourself.',validators = [InputRequired()])
    submit = SubmitField('Submit')
    
class PostForm(FlaskForm):
    post_title = StringField('Title')
    description = TextAreaField('Description', validators=[InputRequired()])
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a feadback',validators=[InputRequired()])
    submit = SubmitField('comment')