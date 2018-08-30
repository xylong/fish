from flask import jsonify

from helper import is_isbn_or_key
from yushu_book import Book

from . import web

@web.route('/book/search/<q>/<page>')
def search(q, page):
    '''
    搜索书籍路由
    :param q: keyword or isbn
    :param page: 页码
    '''
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = Book.search_by_isbn(q)
    else:
        result = Book.search_by_keyword(q)
    return jsonify(result)