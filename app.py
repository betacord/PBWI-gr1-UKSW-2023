from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate

from datetime import datetime

from db import db
from models.clip import ClipModel

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    newest_clips = ClipModel.last_added(3)
    highest_rated = ClipModel.highest_rated(3)

    return render_template(
        'index.html',
        newest_clips=newest_clips,
        highest_rated=highest_rated,
    )


@app.route('/add', methods=['GET', 'POST'])  # 127.0.0.1:5000/add
def add_clip():
    if request.method == 'POST':
        req = request.form

        new_clip = ClipModel(
            title=req['title'],
            description=req['description'],
            link_yt=req['link_yt'],
            link_img=req['link_yt'],
            added=datetime.now().timestamp(),
            score=0,
        )
        new_clip.save()

        return redirect(request.url)

    return render_template('add.html')


if __name__ == '__main__':
    app.run()
