from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        img_src='https://i.ytimg.com/vi/7p6JPZf8c8g/hqdefault.jpg',
        clip_title='Don Braden with Freddie Hubbard in Warsaw 1991 - Bolivia',
        clip_description='This performance of Cedar Walton''s "Bolivia" is from Don Braden''s last gig with Freddie '
                         'Hubbard, after a 2-1/2 year stint.  It was performed in Warsaw, Poland in October of 1991, '
                         'and features Jeff Chambers on bass, Ralph Penland on drums, Ronnie Matthews on piano, '
                         'Don on tenor sax, and the Master, Freddie Hubbard on trumpet.',
    )


if __name__ == '__main__':
    app.run()
