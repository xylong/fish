from flask import jsonify, request

from app.validate.book import SearchForm
from helper import is_isbn_or_key
from yushu_book import Book

from . import web


@web.route('/book/search')
def search():
    '''
    搜索书籍路由
    :param q: keyword or isbn
    :param page: 页码
    '''
    form = SearchForm(request.args)
    if not form.validate():
        return jsonify(form.errors)

    q = form.q.data.strip()
    page = form.page.data
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = Book.search_by_isbn(q)
    else:
        result = Book.search_by_keyword(q)
    return jsonify(result)
