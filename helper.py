def is_isbn_or_key(param):
    isbn_or_key = 'key'
    if len(param) == 13 and param.isdigit():
        isbn_or_key = 'isbn'
    short_q = param.replace('-', '')
    if '-' in param and len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
