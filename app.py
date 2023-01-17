from flask import Flask

app = Flask(__name__)


@app.route('/')  # http://localhost:5000/
def index():
    return 'to jest strona glowna!'


@app.route('/contact')
def contact():
    return 'tel.: 997, 24/7'


if __name__ == '__main__':
    app.run()
