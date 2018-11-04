from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    post = "This is my first post!"
    return render_template("index.html", post=post)
