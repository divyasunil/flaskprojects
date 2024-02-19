from flask import Flask

app = Flask(__name__)


@app.route('/new')
def new():
    return '<h1>New Page</h1>'


app.run()
