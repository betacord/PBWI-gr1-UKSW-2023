from flask import Flask, render_template
from flask_migrate import Migrate

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
# https://i.ytimg.com/vi/7p6JPZf8c8g/hqdefault.jpg


if __name__ == '__main__':
    app.run()
