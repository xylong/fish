from flask import current_app

from app.lib.httper import Http


class Book:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        return Http.get(url)

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PRE_PAGE'], cls.calculate_start(page))
        return Http.get(url)

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PRE_PAGE']
