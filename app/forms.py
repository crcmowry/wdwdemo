from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = TextField("title", validators=[DataRequired()])
    post = TextField("post", validators=[DataRequired()])
