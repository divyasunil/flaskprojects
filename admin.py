from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username, isActive=True)


@app.route('/names')
def name():
    names = ['Divya', 'Deepak', 'Rudra', 'Rohith']
    return render_template('name.html', names=names)


@app.route('/books')
def book():
    books = [
        {'bookname': 'Anna Karenina', 'author': 'Leo Tolstoy', 'cover': 'https://images-na.ssl-images-amazon.com/images/I/51htC41jnKL.jpg'},
        {'bookname': 'Madame Bovary', 'author': 'Gustave Flaubert', 'cover': 'https://pictures.abebooks.com/inventory/22732803445.jpg'},
        {'bookname': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'cover': 'https://i.ebayimg.com/images/g/zxQAAOSwS1pl0ses/s-l500.jpg'},
        {'bookname': 'The Adventures of Huckleberry Finn', 'author': ' Mark Twain', 'cover': 'https://i.pinimg.com/originals/f1/35/0b/f1350b9e5ced0a0fb5515949bedeeddb.jpg'},
    ]
    return render_template('book.html', books=books)


app.run(debug=True)
