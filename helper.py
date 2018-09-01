def is_isbn_or_key(word):
    '''
    判断word是isbn号还是查询关键字key
    isbn isbn13 由13个0-9在数字组成
    isbn10 由10表0-9表数字组组成，中间可能包含' - '
    :param word:
    :return: key or isbn
    '''
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_q = word.replace('-', '')
    if '-' in word and len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
