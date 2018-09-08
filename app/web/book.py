from flask import request, flash, render_template

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
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
    else:
        flash('搜索关键字不符合要求，请重新输入')
    return render_template('search_result.html', books=books)
