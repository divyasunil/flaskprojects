from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>hello world</h1>'


@app.route('/new')
def new():
    return '<h1>New Page</h1>'


app.run()
