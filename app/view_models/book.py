class BookViewModel:
    def __init__(self, book):
        self.isbn = book['isbn']
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.pubdate = book['pubdate']
        self.binding = book['binding']
        self.pages = book['pages']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        return ' / '.join(intros)


class BookCollection:
    def __init__(self):
        self.keyword = ''
        self.total = 0
        self.books = []

    def fill(self, yushu_book, keyword):
        self.keyword = keyword
        self.total = yushu_book.total
        self.books = [BookViewModel(book) for book in yushu_book.books]
