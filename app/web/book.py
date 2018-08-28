from flask import jsonify

from app import app
from helper import is_isbn_or_key
from yushu_book import Book


@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = Book.search_by_isbn(q)
    else:
        result = Book.search_by_keyword(q)
    return jsonify(result)