from flask_login import UserMixin
from sqlalchemy import Column, String, Boolean, Integer, Float
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager
from app.lib.helper import is_isbn_or_key
from app.model.base import Base
from app.model.gift import Gift
from app.model.wish import Wish
from app.spider.yushu_book import YuShuBook


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    _password = Column('password', String(128), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        # 检查isbn格式
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        # 检查是否有这本书
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        # 不允许一个用户同时赠送多本相同的图书
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        # 不允许一个用户同时为一本书的赠送者和索要者
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        return not gifting and not wishing


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
