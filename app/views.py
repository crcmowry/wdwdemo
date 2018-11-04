from flask import render_template, redirect, session, url_for, request
from app import app, db
from app.forms import PostForm
from app.models import Post
import datetime

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PostForm(request.form)
    if form.validate():
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        post = Post(body=form.post.data, title=form.title.data, timestamp=time)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    posts = Post.query.all()
    return render_template("index.html",
                           posts=posts, form=form)
