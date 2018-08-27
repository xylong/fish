from flask import Flask
from helper import is_isbn_or_key

__author__ = 'xyl'

app = Flask(__name__)
app.config.from_object('config.app')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    pass


@app.route('/hello')
def hello():
    headers = {
        'content-type': 'text/plain',
        'location': 'https://www.google.com'
    }
    return '<strong>Flask</strong>'
    # return '<strong>Flask</strong>', 301, headers


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
