class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.pages = book['pages']


class BookCollection:
    def __init__(self):
        self.keyword = ''
        self.total = 0
        self.books = []

    def fill(self, yushu_book, keyword):
        self.keyword = keyword
        self.total = yushu_book.total
        self.books = [BookViewModel(book) for book in yushu_book.books]
