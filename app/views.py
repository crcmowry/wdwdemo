from flask import render_template
from app import app
from app.forms import PostForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if (form.validate()):
        print ("Successful form!")
    return render_template("index.html", form=form)
