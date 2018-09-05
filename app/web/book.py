import json

from flask import jsonify, request

from app.lib.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.validate.book import SearchForm
from app.view_models.book import BookCollection

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

    yushu_book = YuShuBook()
    if isbn_or_key == 'isbn':
        yushu_book.search_by_isbn(q)
    else:
        yushu_book.search_by_keyword(q, page)

    books = BookCollection()
    books.fill(yushu_book, q)
    return json.dumps(books, default=lambda o: o.__dict__)
