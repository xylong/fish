import json

from flask import Flask, jsonify
from book import Book
from helper import is_isbn_or_key

__author__ = 'xyl'

app = Flask(__name__)
app.config.from_object('config.app')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = Book.search_by_isbn(q)
    else
        result = Book.search_by_keyword(q)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
